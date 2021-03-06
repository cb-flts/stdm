"""
/***************************************************************************
Name                 : FLTS QGIS Loader
Description          : FLTS QGIS Loader
Date                 : 04-01-2015
copyright            : (C) 2015 by UN-Habitat and implementing partners.
                       See the accompanying file CONTRIBUTORS.txt in the root
email                : stdm@unhabitat.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import glob
import logging
import os.path
import platform
import shutil
import stdm.data
from collections import OrderedDict

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *
import qgis.utils
from sqlalchemy.exc import SQLAlchemyError
from stdm.settings.config_serializer import ConfigurationFileSerializer
from stdm.settings import current_profile, save_current_profile
from stdm.settings.startup_handler import copy_startup
from stdm.data.configfile_paths import FilePaths
from stdm.data.configuration.exception import ConfigurationException
from stdm.data.configuration.stdm_configuration import StdmConfiguration
from stdm.settings.config_file_updater import ConfigurationFileUpdater
from stdm.data.configuration.config_updater import ConfigurationSchemaUpdater
from stdm.data.configuration.column_updaters import varchar_updater

from stdm.ui.change_pwd_dlg import changePwdDlg
from stdm.ui.doc_generator_dlg import (
    CertificateGeneratorDialogWrapper,
    ReportGeneratorDialogWrapper,
    EntityConfig
)
from stdm.data.database import alchemy_table
from stdm.ui.login_dlg import loginDlg
from stdm.ui.manage_accounts_dlg import manageAccountsDlg
from stdm.ui.content_auth_dlg import contentAuthDlg
from stdm.ui.options_base import OptionsDialog

from ui.flts.user_shortcut_dlg import UserShortcutDialog
from ui.flts.scheme_lodgement import LodgementWizard
from ui.flts.workflow_manager.dock_widget_factory import DockWidgetFactory
from ui.flts.workflow_manager.workflow_manager_widget import WorkflowManagerWidget
from stdm.ui.flts.search.default_search_config import FltsSearchConfigurationLoader
from stdm.ui.flts.search.search_widgets import FltsSearchDockWidget
from stdm.ui.flts.certificate_upload.certificate_upload_widget import CertificateUploadWidget
from stdm.settings.search_config import SearchConfigurationRegistry

from stdm.ui.view_str import ViewSTRWidget
from stdm.ui.admin_unit_selector import AdminUnitSelector
from stdm.ui.entity_browser import (
    EntityBrowserWithEditor
)
from stdm.ui.about import AboutSTDMDialog
from stdm.ui.stdmdialog import DeclareMapping

from stdm.ui.wizard.wizard import ConfigWizard

from stdm.ui.import_data import ImportData
from stdm.ui.export_data import ExportData

from stdm.ui.spatial_unit_manager import SpatialUnitManagerDockWidget

import data

from stdm.data.database import (
    Base,
    NoPostGISError,
    STDMDb
)
from stdm.data.pg_utils import (
    pg_table_exists,
    spatial_tables,
    postgis_exists,
    create_postgis,
    table_column_names
)
from stdm.settings.registryconfig import (
    RegistryConfig,
    WIZARD_RUN,
    STDM_VERSION,
    CONFIG_UPDATED,
    HOST,
    composer_template_path,
    set_entity_browser_record_limit

)
from stdm.ui.license_agreement import LicenseAgreement

from navigation import (
    STDMAction,
    QtContainerLoader,
    ContentGroup,
    TableContentGroup
)

from stdm.utils.util import simple_dialog
from stdm.ui.change_log import ChangeLog
from stdm.settings.template_updater import TemplateFileUpdater

from stdm.utils.util import (
    getIndex,
    db_user_tables,
    format_name,
    setComboCurrentIndexWithText,
    version_from_metadata
)
from mapping.utils import pg_layerNamesIDMapping

from composer import ComposerWrapper
from stdm.ui.progress_dialog import STDMProgressDialog
from stdm.ui.feature_details import DetailsTreeView, DetailsDockWidget
from stdm.ui.social_tenure.str_editor import STREditor

from stdm.ui.geoodk_converter_dialog import GeoODKConverter
from stdm.ui.geoodk_profile_importer import ProfileInstanceRecords

from stdm.security.privilege_provider import SinglePrivilegeProvider
from stdm.security.roleprovider import RoleProvider

LOGGER = logging.getLogger('stdm')


class STDMQGISLoader(object):
    viewSTRWin = None

    def __init__(self, iface):
        self.iface = iface

        # Initialize loader
        self.toolbarLoader = None
        self.menubarLoader = None

        # Setup locale
        self.plugin_dir = os.path.dirname(__file__)
        localePath = ""
        locale = QSettings().value("locale/userLocale")[0:2]
        if QFileInfo(self.plugin_dir).exists():
            # Replace forward slash with backslash
            self.plugin_dir = self.plugin_dir.replace("\\", "/")
            localePath = self.plugin_dir + "/i18n/stdm_%s.qm" % (locale,)
        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # STDM Tables
        self.stdmTables = []
        self.entity_formatters = {}
        self.entity_table_model = {}
        self.stdm_config = StdmConfiguration.instance()
        self.reg_config = RegistryConfig()
        self.spatialLayerMangerDockWidget = None

        self._user_logged_in = False
        self.current_profile = None
        # Profile status label showing the current profile
        # self.profile_status_label = None
        self.flts_status_label = None
        LOGGER.debug('FLTS plugin has been initialized.')
        self.entity_browser = None
        # Load configuration file
        self.config_path = QDesktopServices.storageLocation(
            QDesktopServices.HomeLocation) \
                           + '/.stdm/configuration.stc'
        self.config_serializer = ConfigurationFileSerializer(self.config_path)
        self.configuration_file_updater = ConfigurationFileUpdater(self.iface)
        copy_startup()
        self.dock_widget = None
        self.search_dock_widget = None
        self.cert_upload_widget = None
        set_entity_browser_record_limit(1000)

    def initGui(self):
        # Initial actions on starting up the application
        self._menu_items()
        self.loginAct = STDMAction(QIcon(":/plugins/stdm/images/icons/flts_login.png"),
                                   QApplication.translate("LoginToolbarAction",
                                                          "Login"),
                                   self.iface.mainWindow(),
                                   "CAA4F0D9-727F-4745-A1FC-C2173101F711")
        self.loginAct.setShortcut(QKeySequence(Qt.Key_F2))

        self.aboutAct = STDMAction(QIcon(":/plugins/stdm/images/icons/flts_about.png"),
                                   QApplication.translate("AboutToolbarAction", "About"), self.iface.mainWindow(),
                                   "137FFB1B-90CD-4A6D-B49E-0E99CD46F784")
        # Define actions that are available to all logged in users
        self.logoutAct = STDMAction(QIcon(":/plugins/stdm/images/icons/flts_logout.png"), \
                                    QApplication.translate("LogoutToolbarAction", "Logout"), self.iface.mainWindow(),
                                    "EF3D96AF-F127-4C31-8D9F-381C07E855DD")

        self.changePasswordAct = STDMAction(QIcon(":/plugins/stdm/images/icons/flts_password_change.png"), \
                                            QApplication.translate("ChangePasswordToolbarAction", "Change Password"),
                                            self.iface.mainWindow(),
                                            "8C425E0E-3761-43F5-B0B2-FB8A9C3C8E4B")
        self.helpAct = STDMAction(QIcon(":/plugins/stdm/images/icons/flts_help.png"), \
                                  QApplication.translate("STDMQGISLoader", "Help Contents"), self.iface.mainWindow(),
                                  "7A61CEA9-2A64-45F6-A40F-D83987D416EB")
        self.helpAct.setShortcut(Qt.Key_F10)

        # connect the actions to their respective methods
        self.loginAct.triggered.connect(self.login)
        self.changePasswordAct.triggered.connect(self.changePassword)
        self.logoutAct.triggered.connect(self.logout)
        self.aboutAct.triggered.connect(self.about)
        self.helpAct.triggered.connect(self.help_contents)
        self.initToolbar()
        self.initMenuItems()

    def _menu_items(self):
        # Create menu and menu items on the menu bar
        self.stdmMenu = QMenu()
        self.stdmMenu.setTitle(
            QApplication.translate(
                "STDMQGISLoader", "FLTS"
            )
        )
        # Initialize the menu bar item
        self.menu_bar = self.iface.mainWindow().menuBar()
        # Create actions
        actions = self.menu_bar.actions()
        currAction = actions[len(actions) - 1]
        # add actions to the menu bar
        self.menu_bar.insertMenu(
            currAction,
            self.stdmMenu
        )
        self.stdmMenu.setToolTip(
            QApplication.translate(
                "STDMQGISLoader",
                "FLTS plugin menu"
            )
        )

    def getThemeIcon(self, theName):
        # get the icon from the best available theme
        myCurThemePath = QgsApplication.activeThemePath() + "/plugins/" + theName
        myDefThemePath = QgsApplication.defaultThemePath() + "/plugins/" + theName
        myQrcPath = ":/plugins/stdm/" + theName
        if QFile.exists(myCurThemePath):
            return QIcon(myCurThemePath)
        elif QFile.exists(myDefThemePath):
            return QIcon(myDefThemePath)
        elif QFile.exists(myQrcPath):
            return QIcon(myQrcPath)
        else:
            return QIcon()

    def initToolbar(self):
        # Load initial STDM toolbar
        self.stdmInitToolbar = self.iface.addToolBar("flts")
        self.stdmInitToolbar.setObjectName("flts")
        # Add actions to the toolbar
        self.stdmInitToolbar.addAction(self.loginAct)

        self.stdmInitToolbar.addSeparator()
        self.stdmInitToolbar.addAction(self.helpAct)
        self.stdmInitToolbar.addAction(self.aboutAct)

        self.git_branch = QLabel(self.iface.mainWindow())
        self.git_branch.setText(self.active_branch_name())
        self.stdmInitToolbar.addWidget(self.git_branch)

    def active_branch_name(self):
        try:
            home = QDesktopServices.storageLocation(QDesktopServices.HomeLocation)
            branch_file = '{}/.stdm/.branch'.format(home)
            name = '(' + [line.strip() for line in open(branch_file)][0] + ')'
        except:
            name = ''
        return name

    def initMenuItems(self):
        self.stdmMenu.addAction(self.loginAct)
        self.stdmMenu.addSeparator()
        self.stdmMenu.addAction(self.helpAct)
        self.stdmMenu.addAction(self.aboutAct)

    def unload(self):
        # Remove the STDM toolbar
        del self.stdmInitToolbar
        # Remove connection info
        self.logoutCleanUp()

    def login(self):
        """
        Show login dialog
        """
        frmLogin = loginDlg(self.iface.mainWindow())
        retstatus = frmLogin.exec_()

        if retstatus == QDialog.Accepted:
            # Assign the connection object
            data.app_dbconn = frmLogin.dbConn

            # Initialize the whole STDM database

            db = STDMDb.instance()

            if not db.postgis_state:
                if postgis_exists():
                    create_postgis()
                else:
                    err_msg = QApplication.translate(
                        "FLTS",
                        "FLTS cannot be loaded because the system has "
                        "detected that the PostGIS extension is missing "
                        "in '{0}' database.\nCheck that PostGIS has been "
                        "installed. Please contact the system "
                        "administrator for more information.".format(
                            frmLogin.dbConn.Database)
                    )
                    QMessageBox.critical(
                        self.iface.mainWindow(),
                        QApplication.translate(
                            "FLTS", "Spatial Extension Error"
                        ),
                        err_msg
                    )

                    return

            # Checks if the license is accepted and stops loading
            # modules if the terms and conditions are never accepted.
            license_status = self.load_license_agreement()
            if not license_status:
                return

            # Load logout and change password actions
            self.stdmInitToolbar.insertAction(self.loginAct,
                                              self.logoutAct)
            self.stdmInitToolbar.insertAction(self.loginAct,
                                              self.changePasswordAct)

            self.stdmMenu.insertAction(self.loginAct, self.logoutAct)
            self.stdmMenu.insertAction(self.loginAct, self.changePasswordAct)

            self.loginAct.setEnabled(False)

            # Fetch STDM tables
            self.stdmTables = spatial_tables()

            # Load the configuration from file
            config_load_status = self.load_configuration_from_file(
                self.iface.mainWindow()
            )

            # Exit if the load failed
            if not config_load_status:
                return

            # try:
            # self.show_change_log()
            # Set current profile
            self.current_profile = current_profile()
            self._user_logged_in = True
            if self.current_profile is None:
                result = self.default_profile()
                if not result:
                    return
            self.create_custom_tenure_dummy_col()

            self.init_search_registry()
            self.loadModules()
            self.default_profile()
            self.run_wizard()
            self.copy_designer_template()

            # self.load_shortcut_dlg()
            shortcut_dlg_status = self.load_shortcut_dlg()
            if not shortcut_dlg_status:
                return

        if retstatus != QDialog.Accepted:
            warn_msg = QApplication.translate("STDMQGISLoader",
                                              "You must login to use the"
                                              " application.")
            QMessageBox.warning(
                self.iface.mainWindow(),
                QApplication.translate(
                    "STDMQGISLoader", "Login Warning"
                ),
                warn_msg
            )

    def create_custom_tenure_dummy_col(self):
        """
        Creates custom tenure entity dummy column if it does not exist.
        :return:
        :rtype:
        """
        social_tenure = self.current_profile.social_tenure
        for spatial_unit in social_tenure.spatial_units:
            custom_entity = social_tenure.spu_custom_attribute_entity(
                spatial_unit
            )
            if custom_entity is None:
                continue
            if pg_table_exists(custom_entity.name):
                custom_ent_cols = table_column_names(custom_entity.name)

                if social_tenure.CUSTOM_TENURE_DUMMY_COLUMN \
                        not in custom_ent_cols:
                    dummy_col = custom_entity.columns[
                        social_tenure.CUSTOM_TENURE_DUMMY_COLUMN]
                    custom_table = alchemy_table(custom_entity.name)
                    varchar_updater(dummy_col, custom_table,
                                    custom_ent_cols)

    def minimum_table_checker(self):

        title = QApplication.translate(
            "STDMQGISLoader",
            'Database Table Error'
        )

        message = QApplication.translate(
            "STDMQGISLoader",
            'The system has detected that database tables \n'
            'required in this module are missing.\n'
            'Do you want to re-run the Configuration Wizard now?'
        )

        database_check = QMessageBox.critical(
            self.iface.mainWindow(),
            title,
            message,
            QMessageBox.Yes,
            QMessageBox.No
        )
        if database_check == QMessageBox.Yes:
            self.load_config_wizard()

    def entity_table_checker(self, entity):
        """
        Checks if the database table for a given entity exists.
        In case the table doesn't exists, it shows an error message.
        :param entity: Entity
        :type entity: Object
        :return: True if there is no missing table and false
        if there is a missing table.
        :rtype: Boolean
        """
        title = QApplication.translate(
            "STDMQGISLoader",
            'Database Table Error'
        )

        if not pg_table_exists(entity.name):
            message = QApplication.translate(
                "STDMQGISLoader",
                u'The system has detected that '
                'a required database table - \n'
                '{} is missing. \n'
                'Do you want to re-run the '
                'Configuration Wizard now?'.format(
                    entity.short_name
                ),
                None,
                QCoreApplication.UnicodeUTF8
            )
            database_check = QMessageBox.critical(
                self.iface.mainWindow(),
                title,
                message,
                QMessageBox.Yes,
                QMessageBox.No
            )
            if database_check == QMessageBox.Yes:
                self.load_config_wizard()
            else:
                return False
        else:
            return True

    def run_wizard(self):
        """
        Checks if the configuration wizard was run before.
        :return:
        :rtype:
        """
        host = self.reg_config.read([HOST])
        host_val = host[HOST]

        if host_val != u'localhost':
            if host_val != u'127.0.0.1':
                return

        wizard_key = self.reg_config.read(
            [WIZARD_RUN]
        )

        title = QApplication.translate(
            "STDMQGISLoader",
            'Configuration Wizard Error'
        )
        message = QApplication.translate(
            "STDMQGISLoader",
            'The system has detected that you did not run \n'
            'the Configuration Wizard so far. \n'
            'Do you want to run it now? '
        )
        if len(wizard_key) > 0:
            wizard_value = wizard_key[WIZARD_RUN]

            if wizard_value == 0 or wizard_value == '0':

                default_profile = QMessageBox.critical(
                    self.iface.mainWindow(),
                    title,
                    message,
                    QMessageBox.Yes,
                    QMessageBox.No
                )

                if default_profile == QMessageBox.Yes:
                    self.load_config_wizard()

        else:
            default_profile = QMessageBox.critical(
                self.iface.mainWindow(),
                title,
                message,
                QMessageBox.Yes,
                QMessageBox.No
            )

            if default_profile == QMessageBox.Yes:
                self.load_config_wizard()

    def default_profile(self):
        """
        Checks if the current profile exists.
        If there is only one profile, it sets
        it and run reload_plugin(). If there
        is more than one profile, it asks the
        user the set a profile using Options.
        If no profile exists, it asks the user
        to run Configuration Wizard.
        :return: None
        :rtype: NoneType
        """
        if self.current_profile is None:
            profiles = self.stdm_config.profiles

            title = QApplication.translate(
                "STDMQGISLoader",
                'Default Profile Error'
            )
            if len(profiles) > 0:
                profile_name = profiles.keys()[0]
                save_current_profile(profile_name)
                self.reload_plugin(profile_name)

            else:
                solution = 'Do you want to run the ' \
                           'Configuration Wizard now?'

                message = QApplication.translate(
                    "STDMQGISLoader",
                    'The system has detected Fthat there '
                    'is no default profile. \n {}'.format(
                        solution
                    )

                )
                default_profile = QMessageBox.critical(
                    self.iface.mainWindow(),
                    title,
                    message,
                    QMessageBox.Yes,
                    QMessageBox.No
                )

                if default_profile == QMessageBox.Yes:

                    self.load_config_wizard()
                    return True
                else:
                    return False

    def on_update_progress(self, message):
        """
        A slot raised when update_progress signal is emitted
        in ConfigurationSerializer, ConfigurationUpdater and
        and of the Updaters.
        :param message: The progress message.
        :type message: String
        :return:
        :rtype:
        """
        self.progress.show()
        self.progress.setRange(0, 0)
        self.progress.progress_message(message)

    def on_update_complete(self, document):
        """
        A slot raised when the update_complete signal is emitted.
        It runs post update tasks such as closing progress dialog
        and showing a success message.
        :param document: The updated dom document
        :type document: QDomDocument
        """
        # TODO remove this line below when schema updater is refactored
        self.config_serializer.on_version_updated(document)

        self.reg_config.write(
            {WIZARD_RUN: 1}
        )

        self.progress.hide()
        self.progress.cancel()

    def load_configuration_to_serializer(self):
        try:
            self.config_serializer.update_complete.connect(
                self.on_update_complete
            )
            self.config_serializer.update_progress.connect(
                self.on_update_progress
            )
            self.config_serializer.db_update_progress.connect(
                self.on_update_progress
            )
            self.config_serializer.load()

            return True

        except IOError as io_err:
            QMessageBox.critical(self.iface.mainWindow(),
                                 QApplication.translate(
                                     'STDM', 'Load Configuration Error'
                                 ),
                                 unicode(io_err))

            return False

        except ConfigurationException as c_ex:
            QMessageBox.critical(
                self.iface.mainWindow(),
                QApplication.translate(
                    'STDM',
                    'Load Configuration Error'
                ),
                unicode(c_ex)
            )

            return False

    def stdm_reg_version(self, metadata_version):
        """
        Checks and set STDM registry version using metadata version.
        :param metadata_version: The metadata version
        :type metadata_version: String
        :return: Result of the check or update.
        If reg_version is different from metadata returns 'updated'
        If reg_version is same as metadata returns 'non-updated'
        :rtype: String
        """
        reg_version_dict = self.reg_config.read(
            [STDM_VERSION]
        )

        if STDM_VERSION in reg_version_dict.keys():
            reg_version = reg_version_dict[STDM_VERSION]

        else:
            reg_version = None

        if reg_version is None:
            self.reg_config.write(
                {STDM_VERSION: metadata_version}
            )
            return 'updated'
        elif metadata_version != reg_version:
            self.reg_config.write(
                {STDM_VERSION: metadata_version}
            )
            # compare major versions and mark it return 'updated' if major update.
            md_major_version = metadata_version.rsplit('.', 1)[0]
            reg_major_version = reg_version.rsplit('.', 1)[0]

            if md_major_version != reg_major_version:
                return 'updated'
            else:
                return 'non-updated'
        elif metadata_version == reg_version:
            return 'non-updated'

    def show_change_log(self):
        """
        Shows the change log the new version of STDM.
        """
        version = version_from_metadata()
        # Get the big releases only not minor ones.
        major_version = version.rsplit('.', 1)[0]
        result = self.stdm_reg_version(version)

        if result == 'updated':
            title = QApplication.translate(
                'ConfigurationFileUpdater',
                'Upgrade Information'
            )

            message = QApplication.translate(
                'ConfigurationFileUpdater',
                'Would you like to view the '
                'new features and changes of FLTS {}?'.format(major_version)
            )

            result, checkbox_result = simple_dialog(
                self.iface.mainWindow(),
                title,
                message
            )
            if result:
                change_log = ChangeLog(self.iface.mainWindow())
                change_log.show_change_log(self.plugin_dir)

    def copy_designer_template(self):
        """
        Copies designer templates from the templates folder in the plugin.
        :return:
        :rtype:
        """
        file_handler = FilePaths()

        template_files = glob.glob(u'{0}*.sdt'.format(
            file_handler.defaultConfigPath()
        ))
        templates_path = composer_template_path()

        for temp_file in template_files:

            destination_file = u'{}/{}'.format(
                templates_path, os.path.basename(temp_file))

            if not os.path.isfile(u'{}/{}'.format(
                    templates_path, os.path.basename(temp_file))):
                shutil.copyfile(temp_file, destination_file)

    def load_configuration_from_file(self, parent, manual=False):
        """
        Load configuration object from the file.
        :return: True if the file was successfully
        loaded. Otherwise, False.
        :rtype: bool
        """
        self.progress = STDMProgressDialog(parent)
        self.progress.overall_progress('Upgrading FLTS Configuration...')

        home = QDesktopServices.storageLocation(QDesktopServices.HomeLocation)

        config_path = '{}/.stdm/configuration.stc'.format(home)

        if manual:
            parent.upgradeButton.setEnabled(False)
            upgrade_status = self.configuration_file_updater.load(
                self.progress, True
            )

        else:
            upgrade_status = self.configuration_file_updater.load(
                self.progress
            )

        if upgrade_status:
            # Append configuration_upgraded.stc profiles
            if os.path.isfile(config_path):
                self.progress.progress_message(
                    'Appending the upgraded profile', ''
                )

                self.configuration_file_updater. \
                    append_profile_to_config_file(
                    'configuration_upgraded.stc',
                    'configuration.stc'
                )

            load_result = self.load_configuration_to_serializer()

            if load_result:
                config_updater = ConfigurationSchemaUpdater()
                config_updater.exec_()
                profile_details_dict = \
                    self.configuration_file_updater.backup_data()

                profile_details = {}
                # upgrade profile for each profiles
                for profile, tables in profile_details_dict.iteritems():
                    profile_details[profile] = tables
                    upgrade_template = TemplateFileUpdater(
                        self.plugin_dir, profile_details, self.progress
                    )

                    upgrade_template.process_update(True)

                QMessageBox.information(
                    self.iface.mainWindow(),
                    QApplication.translate(
                        'STDMQGISLoader',
                        'Upgrade STDM Configuration'
                    ),
                    QApplication.translate(
                        'STDMQGISLoader',
                        'Your configuration has been '
                        'successfully upgraded!'
                    )
                )
                # Upgrade from options behavior
                first_profile = profile_details_dict.keys()[0]
                if manual:
                    parent.upgradeButton.setEnabled(True)
                    parent.close()
                    self.reload_plugin(first_profile)
                else:
                    save_current_profile(first_profile)

                self.configuration_file_updater.reg_config.write(
                    {CONFIG_UPDATED: '1'}
                )
                self.configuration_file_updater.reg_config.write(
                    {WIZARD_RUN: 1}
                )
                self.configuration_file_updater.append_log(
                    'Successfully migrated STDM '
                    'Configuration to version 1.2!'
                )
                return True

        else:
            if manual:
                parent.upgradeButton.setEnabled(False)
                parent.manage_upgrade()
            self.configuration_file_updater. \
                _copy_config_file_from_template()
            result = self.load_configuration_to_serializer()
            return result

    def loadModules(self):
        '''
        Define and add modules to the menu and/or toolbar using the module loader
        '''
        self.toolbarLoader = QtContainerLoader(self.iface.mainWindow(),
                                               self.stdmInitToolbar, self.logoutAct)
        self.menubarLoader = QtContainerLoader(self.iface.mainWindow(),
                                               self.stdmMenu, self.logoutAct)

        # Define containers for grouping actions
        adminBtn = QToolButton()
        adminObjName = QApplication.translate("ToolbarLhtSettings", "Admin Settings")
        # Required by module loader for those widgets that need to be inserted into the container
        adminBtn.setObjectName(adminObjName)
        adminBtn.setToolTip(adminObjName)
        adminBtn.setIcon(QIcon(":/plugins/stdm/images/icons/flts_settings.png"))
        adminBtn.setPopupMode(QToolButton.InstantPopup)

        adminMenu = QMenu(adminBtn)
        adminBtn.setMenu(adminMenu)

        # Settings menu container in STDM's QGIS menu
        fltsAdminMenu = QMenu(self.stdmMenu)
        fltsAdminMenu.setIcon(QIcon(":/plugins/stdm/images/icons/flts_settings.png"))
        fltsAdminMenu.setObjectName("FLTSAdminSettings")
        fltsAdminMenu.setTitle(QApplication.translate("ToolbarLhtSettings", "Admin Settings"))

        # FLTS
        # Define containers for grouping actions
        lhtBtn = QToolButton()
        lhtObjName = QApplication.translate("ToolbarLhtSettings", "Land Hold Title")
        # Required by module loader for those widgets that need to be inserted into the container
        lhtBtn.setObjectName(lhtObjName)
        lhtBtn.setToolTip(lhtObjName)
        lhtBtn.setIcon(QIcon(":/plugins/stdm/images/icons/flts_scheme_assessment.png"))
        lhtBtn.setPopupMode(QToolButton.InstantPopup)

        lhtMenu = QMenu(lhtBtn)
        lhtBtn.setMenu(lhtMenu)

        # Settings menu container in FLTS's QGIS menu
        lhtAdminMenu = QMenu(self.stdmMenu)
        lhtAdminMenu.setIcon(QIcon(":/plugins/stdm/images/icons/flts_scheme_assessment.png"))
        lhtAdminMenu.setObjectName("FLTSsettings")
        lhtAdminMenu.setTitle(QApplication.translate("ToolbarLhtSettings", "Land Hold Title"))

        # Scheme
        schemeBtn = QToolButton()
        schemeObjName = QApplication.translate("ToolbarSchemeSettings", "Scheme Management")
        # Required by module loader for those widgets that need to be inserted into the container
        schemeBtn.setObjectName(schemeObjName)
        schemeBtn.setToolTip(schemeObjName)
        schemeBtn.setIcon(QIcon(":/plugins/stdm/images/icons/flts_scheme_management2.png"))
        schemeBtn.setPopupMode(QToolButton.InstantPopup)

        schemeMenu = QMenu(schemeBtn)
        schemeBtn.setMenu(schemeMenu)

        # Settings menu container in flts's QGIS menu
        schemeAdminMenu = QMenu(self.stdmMenu)
        schemeAdminMenu.setIcon(QIcon(":/plugins/stdm/images/icons/flts_scheme_management2.png"))
        schemeAdminMenu.setObjectName("FLTSAdminSettings")
        schemeAdminMenu.setTitle(QApplication.translate("ToolbarSchemeSettings", "Scheme Management"))

        # Certificate
        certBtn = QToolButton()
        certObjName = QApplication.translate("ToolbarCertSettings", "Certificate Settings")
        # Required by module loader for those widgets that need to be inserted into the container
        certBtn.setObjectName(certObjName)
        certBtn.setToolTip(certObjName)
        certBtn.setIcon(QIcon(":/plugins/stdm/images/icons/flts_certificate.png"))
        certBtn.setPopupMode(QToolButton.InstantPopup)

        certMenu = QMenu(certBtn)
        certBtn.setMenu(certMenu)

        # Settings menu container in STDM's QGIS menu
        certAdminMenu = QMenu(self.stdmMenu)
        certAdminMenu.setIcon(QIcon(":/plugins/stdm/images/flts_certificate.png"))
        certAdminMenu.setObjectName("STDMAdminSettings")
        certAdminMenu.setTitle(QApplication.translate("ToolbarCertSettings", "Certificate Settings"))

        # Search
        search_btn = QToolButton()
        search_btn.setObjectName('SearchBtn')
        search_btn.setPopupMode(QToolButton.InstantPopup)
        search_btn.setAutoRaise(True)
        search_btn.setCheckable(True)
        search_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        search_btn.triggered.connect(self.show_search_widget)

        # Settings menu container in STDM's QGIS menu
        fltsSearchMenu = QMenu(self.stdmMenu)
        fltsSearchMenu.setIcon(QIcon(":/plugins/stdm/images/icons/flts_search.png"))
        fltsSearchMenu.setObjectName("FLTSSearchSettings")
        fltsSearchMenu.setTitle(QApplication.translate("ToolbarSearchSettings", "Search Settings"))

        # Report
        reportBtn = QToolButton()
        reportObjName = QApplication.translate("ToolbarReportSettings", "Report Settings")
        # Required by module loader for those widgets that need to be inserted into the container
        reportBtn.setObjectName(reportObjName)
        reportBtn.setToolTip(reportObjName)
        reportBtn.setIcon(QIcon(":/plugins/stdm/images/icons/flts_report.png"))
        reportBtn.setPopupMode(QToolButton.InstantPopup)

        reportMenu = QMenu(reportBtn)
        reportBtn.setMenu(reportMenu)

        # Settings menu container in STDM's QGIS menu
        fltsReportMenu = QMenu(self.stdmMenu)
        fltsReportMenu.setIcon(QIcon(":/plugins/stdm/images/icons/flts_report.png"))
        fltsReportMenu.setObjectName("FLTSReportSettings")
        fltsReportMenu.setTitle(QApplication.translate("ToolbarReportSettings", "Report Settings"))

        # Define actions
        self.contentAuthAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_content_auth.png"),
            QApplication.translate(
                "ContentAuthorizationToolbarAction",
                "Content Authorization"
            ),
            self.iface.mainWindow()
        )

        self.usersAct = QAction(QIcon(":/plugins/stdm/images/icons/flts_users_manage.png"), \
                                QApplication.translate("ManageUsersToolbarAction", "Manage Users-Roles"),
                                self.iface.mainWindow())

        self.options_act = QAction(QIcon(":/plugins/stdm/images/icons/flts_options.png"), \
                                   QApplication.translate("OptionsToolbarAction", "Options"),
                                   self.iface.mainWindow())

        self.docDesignerAct = QAction(QIcon(":/plugins/stdm/images/icons/flts_document_designer.png"), \
                                      QApplication.translate("DocumentDesignerAction", "Document Designer"),
                                      self.iface.mainWindow())

        self.docGeneratorAct = QAction(QIcon(":/plugins/stdm/images/icons/flts_document_generator.png"), \
                                       QApplication.translate("DocumentGeneratorAction", "Certificate Generator"),
                                       self.iface.mainWindow())

        self.reportGeneratorAct = QAction(QIcon(":/plugins/stdm/images/icons/flts_report.png"), \
                                          QApplication.translate("ReportGeneratorAction", "Report Generator"),
                                          self.iface.mainWindow())

        self.wzdAct = QAction(QIcon(":/plugins/stdm/images/icons/flts_database_designer.png"), \
                              QApplication.translate("ConfigWizard", "Configuration Wizard"), self.iface.mainWindow())
        self.wzdAct.setShortcut(Qt.Key_F7)

        # Add current profiles to profiles combobox
        # self.load_profiles_combobox()

        # FLTS
        self.schemeLodgementAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_lodgement.png"),
            QApplication.translate("SchemeLodgementToolbarAction", "Scheme Lodgement"),
            self.iface.mainWindow())

        self.schemeEstablishmentAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_scheme_establishment.png"),
            QApplication.translate(
                "SchemeEstablishmentToolbarAction",
                "Scheme Establishment"
            ),
            self.iface.mainWindow()
        )

        self.firstExaminationAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_scheme_management_assessment1.png"),
            QApplication.translate(
                "FirstExaminationToolbarAction",
                "First Examination"
            ),
            self.iface.mainWindow()
        )

        self.secondExaminationAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_scheme_management_assessment2.png"),
            QApplication.translate(
                "SecondExaminationToolbarAction",
                "Second Examination"
            ),
            self.iface.mainWindow()
        )

        self.thirdExaminationAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_scheme_management_assessment3.png"),
            QApplication.translate(
                "ThirdExaminationToolbarAction",
                "Third Examination"
            ),
            self.iface.mainWindow()
        )

        self.printCertificateAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_print.png"),
            QApplication.translate(
                "PrintCertificateToolbarAction",
                "Print Certificate"
            ),
            self.iface.mainWindow()
        )

        self.scanCertificateAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_scan.png"),
            QApplication.translate(
                "ScanCertificateToolbarAction",
                "Scan Certificate"
            ),
            self.iface.mainWindow()
        )

        self.importPlotsAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_import_plot.png"),
            QApplication.translate(
                "ImportPlotsToolbarAction",
                "Import Plots"
            ),
            self.iface.mainWindow()
        )

        self.schemeRevisionAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_scheme_management.png"),
            QApplication.translate(
                "SchemeRevisionToolbarAction",
                "Scheme Revision"
            ),
            self.iface.mainWindow()
        )

        self.searchAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_search.png"),
            QApplication.translate(
                "SearchToolbarAction",
                "Search"
            ),
            self.iface.mainWindow()
        )

        self.reportAct = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_report.png"),
            QApplication.translate(
                "ReportToolbarAction",
                "Report"
            ),
            self.iface.mainWindow()
        )

        self.cert_upload_act = QAction(
            QIcon(":/plugins/stdm/images/icons/flts_certificate_upload.png"),
            QApplication.translate(
                "ReportToolbarAction",
                "Certificate Upload"
            ),
            self.iface.mainWindow()
        )

        # Connect the slots for the actions above
        self.contentAuthAct.triggered.connect(self.contentAuthorization)
        self.usersAct.triggered.connect(self.manageAccounts)
        self.options_act.triggered.connect(self.on_sys_options)
        self.docDesignerAct.triggered.connect(self.onDocumentDesigner)
        self.docGeneratorAct.triggered.connect(self.onDocumentGenerator)
        self.reportGeneratorAct.triggered.connect(self.onReportGenerator)
        self.cert_upload_act.triggered.connect(self.on_cert_upload)
        self.wzdAct.triggered.connect(self.load_config_wizard)
        # self.viewSTRAct.triggered.connect(self.onViewSTR)

        # flts
        self.schemeLodgementAct.triggered.connect(self.lodge_scheme)
        self.schemeEstablishmentAct.triggered.connect(self.establish_scheme)
        self.firstExaminationAct.triggered.connect(self.first_examination)
        self.secondExaminationAct.triggered.connect(self.second_examination)
        self.thirdExaminationAct.triggered.connect(self.third_examination)
        self.importPlotsAct.triggered.connect(self.import_plots)
        self.schemeRevisionAct.triggered.connect(self.revise_scheme)
        # self.printCertificateAct.triggered.connect(self.print_certificate)
        # self.scanCertificateAct.triggered.connect(self.scan_certificate)
        # self.searchAct.triggered.connect(self.flts_search)
        # self.reportAct.triggered.connect(self.flts_report)

        # Create content items
        # STDM
        contentAuthCnt = ContentGroup.contentItemFromQAction(self.contentAuthAct)
        contentAuthCnt.code = "E59F7CC1-0D0E-4EA2-9996-89DACBD07A83"

        userRoleMngtCnt = ContentGroup.contentItemFromQAction(self.usersAct)
        userRoleMngtCnt.code = "0CC4FB8F-70BA-4DE8-8599-FD344A564EB5"

        options_cnt = ContentGroup.contentItemFromQAction(self.options_act)
        options_cnt.code = "1520B989-03BA-4B05-BC50-A4C3EC7D79B6"

        documentDesignerCnt = ContentGroup.contentItemFromQAction(self.docDesignerAct)
        documentDesignerCnt.code = "C4826C19-2AE3-486E-9FF0-32C00A0A517F"

        documentGeneratorCnt = ContentGroup.contentItemFromQAction(self.docGeneratorAct)
        documentGeneratorCnt.code = "4C0C7EF2-5914-4FDE-96CB-089D44EDDA5A"

        reportGeneratorCnt = ContentGroup.contentItemFromQAction(self.reportGeneratorAct)
        reportGeneratorCnt.code = "8F5DB287-4295-40F7-A826-EA2F5868196B"

        certUploadCnt = ContentGroup.contentItemFromQAction(self.cert_upload_act)
        certUploadCnt.code = "4JDFB3C3-N4UP-A200-A826-SYGPFV6B2OT4"

        wzdConfigCnt = ContentGroup.contentItemFromQAction(self.wzdAct)
        wzdConfigCnt.code = "F16CA4AC-3E8C-49C8-BD3C-96111EA74206"

        # FLTS
        schemeLodgementCnt = ContentGroup.contentItemFromQAction(self.schemeLodgementAct)
        schemeLodgementCnt.code = "97EB2313-AA9C-4478-83F8-896E30E8FA78"

        schemeEstablishmentCnt = ContentGroup.contentItemFromQAction(self.schemeEstablishmentAct)
        schemeEstablishmentCnt.code = "03B3EC1D-B494-4B1A-9B77-D62FC2D6A579"

        schemeRevisionCnt = ContentGroup.contentItemFromQAction(self.schemeRevisionAct)
        schemeRevisionCnt.code = "23BCF2D8-51B9-4A3B-9E5E-8C584D7633D6"

        firstExaminationCnt = ContentGroup.contentItemFromQAction(self.firstExaminationAct)
        firstExaminationCnt.code = "6FC69F4F-3C38-4F4C-986A-C82702A56DB3"

        secondExaminationCnt = ContentGroup.contentItemFromQAction(self.secondExaminationAct)
        secondExaminationCnt.code = "B77A758E-C571-4E02-80F6-5F679B1186A3"

        thirdExaminationCnt = ContentGroup.contentItemFromQAction(self.thirdExaminationAct)
        thirdExaminationCnt.code = "E9116F3F-EF17-4D84-9FDF-5E65455503D2"

        importPlotsCnt = ContentGroup.contentItemFromQAction(self.importPlotsAct)
        importPlotsCnt.code = "FEC81DCE-FF7E-4253-B6CE-30D0504D4G16"

        username = data.app_dbconn.User.UserName

        if username == 'postgres':
            self.grant_privilege_base_tables(username)

        self.moduleCntGroup = None
        self.moduleContentGroups = []
        self._moduleItems = OrderedDict()
        self._reportModules = OrderedDict()

        for attrs in self.user_entities():
            self._moduleItems[attrs[2]] = attrs[0]

        for k, v in self._moduleItems.iteritems():
            moduleCntGroup = self._create_table_content_group(
                k, username, 'table.png'
            )
            self._reportModules[k] = v
            self.moduleContentGroups.append(moduleCntGroup)

        # create a separator
        tbSeparator = QAction(self.iface.mainWindow())
        tbSeparator.setSeparator(True)

        # Create content groups and add items

        self.contentAuthCntGroup = ContentGroup(username)
        self.contentAuthCntGroup.addContentItem(contentAuthCnt)
        self.contentAuthCntGroup.setContainerItem(self.contentAuthAct)
        self.contentAuthCntGroup.register()

        self.userRoleCntGroup = ContentGroup(username)
        self.userRoleCntGroup.addContentItem(userRoleMngtCnt)
        self.userRoleCntGroup.setContainerItem(self.usersAct)
        self.userRoleCntGroup.register()

        self.options_content_group = ContentGroup(username)
        self.options_content_group.addContentItem(options_cnt)
        self.options_content_group.setContainerItem(self.options_act)
        self.options_content_group.register()

        self.wzdConfigCntGroup = ContentGroup(username, self.wzdAct)
        self.wzdConfigCntGroup.addContentItem(wzdConfigCnt)
        self.wzdConfigCntGroup.register()

        self.docDesignerCntGroup = ContentGroup(username, self.docDesignerAct)
        self.docDesignerCntGroup.addContentItem(documentDesignerCnt)
        self.docDesignerCntGroup.register()

        self.docGeneratorCntGroup = ContentGroup(username, self.docGeneratorAct)
        self.docGeneratorCntGroup.addContentItem(documentGeneratorCnt)
        self.docGeneratorCntGroup.register()

        # Register search items
        search_actions = SearchConfigurationRegistry.instance().actions()

        # Notify user if there are no search actions defined
        if len(search_actions) == 0:
            self.iface.messageBar().pushMessage(
                'FLTS Search',
                'No search configuration found.',
                QgsMessageBar.WARNING,
                15
            )

        search_content_grp = SearchConfigurationRegistry.instance().content_group(
            username,
            search_btn
        )
        search_content_grp.register()
        search_group = QActionGroup(self.iface.mainWindow())
        for sa in search_actions:
            search_group.addAction(sa)

        self.reportGeneratorCntGroup = ContentGroup(username, self.reportGeneratorAct)
        self.reportGeneratorCntGroup.addContentItem(reportGeneratorCnt)
        self.reportGeneratorCntGroup.register()

        self.certUploadCntGroup = ContentGroup(username, self.cert_upload_act)
        self.certUploadCntGroup.addContentItem(certUploadCnt)
        self.certUploadCntGroup.register()

        adminSettingsCntGroups = []
        adminSettingsCntGroups.append(self.contentAuthCntGroup)
        adminSettingsCntGroups.append(self.userRoleCntGroup)
        adminSettingsCntGroups.append(self.options_content_group)
        adminSettingsCntGroups.append(self.wzdConfigCntGroup)

        # Create content groups and add items
        self.schemeLodgementCntGroup = ContentGroup(username)
        self.schemeLodgementCntGroup.addContentItem(schemeLodgementCnt)
        self.schemeLodgementCntGroup.setContainerItem(self.schemeLodgementAct)
        self.schemeLodgementCntGroup.register()

        self.schemeEstablishmentCntGroup = ContentGroup(username)
        self.schemeEstablishmentCntGroup.addContentItem(schemeEstablishmentCnt)
        self.schemeEstablishmentCntGroup.setContainerItem(self.schemeEstablishmentAct)
        self.schemeEstablishmentCntGroup.register()

        self.schemeRevisionCntGroup = ContentGroup(username)
        self.schemeRevisionCntGroup.addContentItem(schemeRevisionCnt)
        self.schemeRevisionCntGroup.setContainerItem(self.schemeRevisionAct)
        self.schemeRevisionCntGroup.register()

        self.firstExaminationCntGroup = ContentGroup(username)
        self.firstExaminationCntGroup.addContentItem(firstExaminationCnt)
        self.firstExaminationCntGroup.setContainerItem(self.firstExaminationAct)
        self.firstExaminationCntGroup.register()

        self.secondExaminationCntGroup = ContentGroup(username)
        self.secondExaminationCntGroup.addContentItem(secondExaminationCnt)
        self.secondExaminationCntGroup.setContainerItem(self.secondExaminationAct)
        self.secondExaminationCntGroup.register()

        self.importPlotsCntGroup = ContentGroup(username)
        self.importPlotsCntGroup.addContentItem(importPlotsCnt)
        self.importPlotsCntGroup.setContainerItem(self.importPlotsAct)
        self.importPlotsCntGroup.register()

        self.thirdExaminationCntGroup = ContentGroup(username)
        self.thirdExaminationCntGroup.addContentItem(thirdExaminationCnt)
        self.thirdExaminationCntGroup.setContainerItem(self.thirdExaminationAct)
        self.thirdExaminationCntGroup.register()

        # Group scheme settings content groups

        schemeSettingsCntGroups = []
        schemeSettingsCntGroups.append(self.schemeLodgementCntGroup)
        schemeSettingsCntGroups.append(self.schemeEstablishmentCntGroup)
        schemeSettingsCntGroups.append(self.firstExaminationCntGroup)
        schemeSettingsCntGroups.append(self.secondExaminationCntGroup)
        schemeSettingsCntGroups.append(self.thirdExaminationCntGroup)
        schemeSettingsCntGroups.append(self.importPlotsCntGroup)
        schemeSettingsCntGroups.append(self.schemeRevisionCntGroup)

        certSettingsCntGroups = []
        certSettingsCntGroups.append(self.docGeneratorCntGroup)
        certSettingsCntGroups.append(self.docDesignerCntGroup)
        certSettingsCntGroups.append(self.certUploadCntGroup)

        searchReportCntgroups = []
        # toolbar items
        self.toolbarLoader.addContent(self.wzdConfigCntGroup,
                                      [adminMenu, adminBtn]
                                      )

        self.toolbarLoader.addContent(self.contentAuthCntGroup,
                                      [adminMenu, adminBtn]
                                      )

        self.toolbarLoader.addContent(self.userRoleCntGroup,
                                      [adminMenu, adminBtn]
                                      )

        self.toolbarLoader.addContent(self.options_content_group,
                                      [adminMenu, adminBtn]
                                      )

        self.toolbarLoader.addContent(self.schemeLodgementCntGroup)
        self.toolbarLoader.addContent(self.schemeEstablishmentCntGroup)
        self.toolbarLoader.addContent(self.firstExaminationCntGroup)
        self.toolbarLoader.addContent(self.secondExaminationCntGroup)
        self.toolbarLoader.addContent(self.importPlotsCntGroup)
        self.toolbarLoader.addContent(self.thirdExaminationCntGroup)
        self.toolbarLoader.addContent(self.schemeRevisionCntGroup)

        self.toolbarLoader.addContent(self._action_separator())

        # Add search items to toolbar
        self.toolbarLoader.addContent(
            search_content_grp,
            (search_actions, search_btn)
        )

        # self.toolbarLoader.addContent(self.printCertCntGroup)
        # self.toolbarLoader.addContent(self.scanCertCntGroup)
        self.toolbarLoader.addContent(self._action_separator())

        self.toolbarLoader.addContent(self.docDesignerCntGroup)
        self.toolbarLoader.addContent(self.docGeneratorCntGroup)
        self.toolbarLoader.addContent(self.reportGeneratorCntGroup)
        self.toolbarLoader.addContent(self.certUploadCntGroup)

        # menubar items
        self.menubarLoader.addContents(schemeSettingsCntGroups,
                                       [lhtAdminMenu, lhtAdminMenu]
                                       )

        self.menubarLoader.addContents(certSettingsCntGroups,
                                       [lhtAdminMenu, lhtAdminMenu]
                                       )

        self.menubarLoader.addContents(searchReportCntgroups,
                                       [lhtAdminMenu, lhtAdminMenu]
                                       )

        # Load all the content in the container
        self.toolbarLoader.loadContent()
        self.menubarLoader.loadContent()

        self.current_user_status_message()

    def grant_privilege_base_tables(self, username):
        roles = []
        roleProvider = RoleProvider()
        roles = roleProvider.GetSysRoles()

        privilege_provider = SinglePrivilegeProvider('', current_profile())
        for role in roles:
            privilege_provider.grant_privilege_base_table(role)

    def init_search_registry(self):
        # Configure search registry
        search_config_file = QDesktopServices.storageLocation(
            QDesktopServices.HomeLocation
        ) + '/.stdm/search/configuration.ini'

        # Initialize registry
        SearchConfigurationRegistry.instance(
            files=[search_config_file],
            loader_cls=FltsSearchConfigurationLoader
        )

    def load_profiles_combobox(self):
        """
        Create a combobox and load existing profiles.
        """
        self.profiles_combobox = QComboBox(self.iface.mainWindow())
        if self.current_profile is None:
            return

        profile_names = self.stdm_config.profiles.keys()

        self.profiles_combobox.clear()

        self.profiles_combobox.addItems(profile_names)

        self.profiles_combobox.setStyleSheet(
            """
        QComboBox {
                border: 2px solid #4b85ca;
                border-radius: 0px;
                padding: 1px 3px 1px 3px;
                min-width: 6em;
            }
         QComboBox:editable {
             background: white;
         }

         QComboBox:!editable, QComboBox::drop-down:editable {
                 background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                            stop: 0 #f8f8f8, stop: 0.4 #eeeeee,
                                          stop: 0.5 #e6e6e6, stop: 1.0 #cecece);
         }

         /* QComboBox gets the "on" state when the popup is open */
         QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                    stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                                    stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
         }

         QComboBox:on { /* shift the text when the popup opens */
             padding-top: 3px;
             padding-left: 4px;
         }

         QComboBox::drop-down {
             subcontrol-origin: padding;
             subcontrol-position: top right;
             width: 15px;

             border-left-width: 1px;
             border-left-color: darkgray;
             border-left-style: solid; /* just a single line */
             border-top-right-radius: 3px; /* same radius as the QComboBox */
             border-bottom-right-radius: 3px;
         }

         QComboBox::down-arrow {
             image: url(:/plugins/stdm/images/icons/down_arrow.png);
         }

         QComboBox::down-arrow:on { /* shift the arrow when popup is open */
             top: 1px;
             left: 1px;
         }
            """
        )
        setComboCurrentIndexWithText(
            self.profiles_combobox, self.current_profile.name
        )
        self.profiles_combobox.currentIndexChanged[str].connect(
            self.reload_plugin
        )

    def _create_table_content_group(self, k, username, icon):
        content_action = QAction(
            QIcon(":/plugins/stdm/images/icons/{}".format(icon)),
            k,
            self.iface.mainWindow()
        )
        moduleCntGroup = TableContentGroup(username, k, content_action)
        moduleCntGroup.register()
        return moduleCntGroup

    def show_search_by_datasource(self, data_source):
        """
        Shows the search widget based on the name of the data source in the
        search registry.
        :param data_source: Data source name.
        :type data_source: str
        """
        if not data_source:
            return

        if not self.search_dock_widget:
            self.search_dock_widget = FltsSearchDockWidget(
                self.iface.mainWindow()
            )
            self.iface.addDockWidget(
                Qt.BottomDockWidgetArea,
                self.search_dock_widget
            )

        self.search_dock_widget.show()
        self.search_dock_widget.raise_()
        status = self.search_dock_widget.show_search_widget(data_source)
        if not status:
            self.iface.messageBar().pushMessage(
                'FLTS Search',
                u'No search configuration found for \'{0}\' data source'.format(data_source),
                QgsMessageBar.WARNING,
                15
            )

    def show_search_widget(self, action):
        """
        Slot raised when one of the search actions is clicked.
        :param action: Action that triggered the signal.
        :type action: QAction
        """
        data_source = action.data()
        if not data_source:
            return

        self.show_search_by_datasource(data_source)

    def check_spatial_tables(self, show_message=False):
        """
        Checks if spatial tables exist in the database.
        :param show_message: If true, shows an error message.
        :type show_message: Boolean
        :return: True if spatial tables exist and False with or
        without error message if it doesn't exist.
        :rtype: Boolean
        """
        # Get entities containing geometry
        # columns based on the config info
        if not self.current_profile is None:
            config_entities = self.current_profile.entities
            self.geom_entities = [
                ge for ge in config_entities.values()
                if ge.TYPE_INFO == 'ENTITY' and
                   ge.has_geometry_column()
            ]

            self.sp_tables = spatial_tables()
            # Check whether the geometry tables
            # specified in the config exist
            missing_tables = [
                geom_entity.name
                for geom_entity in self.geom_entities
                if not geom_entity.name in self.sp_tables
            ]

            # Notify user of missing tables
            if len(missing_tables) > 0:
                if show_message:
                    msg = QApplication.translate(
                        'Spatial Unit Manager',
                        'The following spatial tables '
                        'are missing in the database:'
                        '\n {0}\n Do you want to re-run the '
                        'Configuration Wizard now?'.format(
                            '\n'.join(
                                missing_tables
                            )
                        )
                    )
                    title = QApplication.translate(
                        'STDMQGISLoader',
                        'Spatial Table Error'
                    )
                    database_check = QMessageBox.critical(
                        self.iface.mainWindow(),
                        title,
                        msg,
                        QMessageBox.Yes,
                        QMessageBox.No
                    )
                    if database_check == QMessageBox.Yes:
                        self.load_config_wizard()

                return False
            else:
                return True

    def create_spatial_unit_manager(
            self, menu_enable=False
    ):
        """
        Loads spatial unit manager after checking if
        spatial tables exist. If enabled from STDM toolbar
        and spatial tables don't exist show error message.
        :param menu_enable: Weather it is activated from the
        Menu or not. If True, an error could be show if spatial
        tables don't exist.
        :type menu_enable: Boolean
        :return: None
        :rtype: NoneType
        """
        self.remove_spatial_unit_mgr()
        if self.check_spatial_tables():
            self.spatialLayerMangerDockWidget = \
                SpatialUnitManagerDockWidget(
                    self.iface, self
                )
            self.spatialLayerMangerDockWidget.setWindowTitle(
                QApplication.translate(
                    "STDMQGISLoader",
                    'Spatial Unit Manager'
                )
            )
            self.iface.addDockWidget(
                Qt.LeftDockWidgetArea,
                self.spatialLayerMangerDockWidget
            )

            self.spatialLayerMangerDockWidget.show()
            # self.spatialLayerManager.setChecked(True)
        else:
            if menu_enable:
                # self.spatialLayerManager.setChecked(False)
                self.check_spatial_tables(True)

    def onActionAuthorised(self, name):
        """
        This slot is raised when a toolbar action
        is authorised for access by the currently
        logged in user.
        """
        pass

    def manageAccounts(self):
        """
        Slot for showing the user and
        role accounts management window
        """
        frmUserAccounts = manageAccountsDlg(self)
        frmUserAccounts.exec_()

    def contentAuthorization(self):
        """
        Slot for showing the content authorization dialog
        """
        frmAuthContent = contentAuthDlg(self)
        frmAuthContent.exec_()

    def on_sys_options(self):
        """
        Loads the dialog for settings STDM options.
        """
        opt_dlg = OptionsDialog(self.iface)
        opt_dlg._apply_btn.clicked.connect(
            lambda: self.reload_plugin(None)
        )
        opt_dlg.buttonBox.accepted.connect(
            lambda: self.reload_plugin(None)
        )

        opt_dlg.exec_()

    def current_user_status_message(self):
        """
        Shows the name of the current user who is logged in
        QGIS status bar.
        :return: None
        :rtype: NoneType
        """
        if self.current_profile is None:
            return
        if self.flts_status_label is None:
            self.flts_status_label = QLabel()
        # FOR NOW
        current_user_name = format_name(
            stdm.data.app_dbconn.User.UserName
        )
        message = QApplication.translate(
            'STDMPlugin',
            'Logged in as {}'.format(
                current_user_name
            )
        )

        if self.flts_status_label.parent() is None:
            self.iface.mainWindow().statusBar().insertPermanentWidget(
                0,
                self.flts_status_label,
                10
            )
        self.flts_status_label.setText(message)

    def reload_plugin(self, sel_profile, load_from_stc=False):
        """
        Reloads STDM plugin without logging out.
        This is to allow modules capture changes
        made by the Configuration Wizard and Options.
        :param sel_profile: the selected profile name
        on the configuration wizard.
        :type: string
        """
        if not self._user_logged_in:
            return
        if self.toolbarLoader is not None:
            self.toolbarLoader.unloadContent()
            # Clear current profile combobox
            # self.profiles_combobox.deleteLater()
            # self.profiles_combobox = None

        if self.menubarLoader is not None:
            self.menubarLoader.unloadContent()
            self.stdmMenu.clear()
        if self.entity_browser is not None:
            self.entity_browser.close()

        self.logoutCleanUp(True)
        if load_from_stc:
            self.config_serializer.load()
        # Set current profile based on the selected
        # profile in the wizard
        if sel_profile is not None:
            if len(sel_profile) > 1:
                save_current_profile(sel_profile)

        self.current_profile = current_profile()

        if not self.current_profile is None:
            LOGGER.debug(
                'Successfully changed '
                'the current profile to {}'.format(
                    self.current_profile.name
                )
            )
        try:
            self.loadModules()

            LOGGER.debug(
                'Successfully reloaded all modules.'
            )
        except SQLAlchemyError as ex:
            LOGGER.debug(
                str(ex)
            )
            STDMDb.instance().session.rollback()
            self.loadModules()

        except Exception as ex:
            LOGGER.debug(
                'Error Loading Modules: {}'.format(str(ex))
            )
            self.loadModules()

    def load_config_wizard(self):
        """
        Load the configuration wizard.
        """
        self.wizard = ConfigWizard(
            self.iface.mainWindow()
        )

        # Reload all modules
        self.wizard.wizardFinished.connect(self.reload_plugin)
        try:
            self.wizard.exec_()
        except Exception as ex:
            QMessageBox.critical(self.iface.mainWindow(),
                                 QApplication.translate(
                                     "STDMPlugin",
                                     "Error Loading the Configuration Wizard"
                                 ),
                                 unicode(ex)
                                 )

    def changePassword(self):
        """
        Slot for changing password
        """
        # Load change password dialog
        frmPwdDlg = changePwdDlg(self)
        frmPwdDlg.exec_()

    def newSTR(self):
        """
        Slot for showing the wizard for
        defining a new social
        tenure relationship
        """
        try:

            str_editor = STREditor()
            str_editor.open()

        except Exception as ex:
            QMessageBox.critical(
                self.iface.mainWindow(),
                QApplication.translate(
                    'STDMQGISLoader',
                    'Error Loading the STR Editor'
                ),
                str(ex)
            )

    def onManageAdminUnits(self):
        """
        Slot for showing administrative
        unit selector dialog.
        """

        if self.current_profile is None:
            self.default_profile()
            return
        admin_spatial_unit = [
            e
            for e in
            self.current_profile.entities.values()
            if e.TYPE_INFO == 'ADMINISTRATIVE_SPATIAL_UNIT'
        ]
        db_status = self.entity_table_checker(
            admin_spatial_unit[0]
        )

        if db_status:
            frmAdminUnitSelector = AdminUnitSelector(
                self.iface.mainWindow()
            )
            frmAdminUnitSelector.setManageMode(True)
            frmAdminUnitSelector.exec_()
        else:
            return

    def onDocumentDesigner(self):
        """
        Slot raised to show new print
        composer with additional tools for designing
        map-based documents.
        """
        status, tables = self.check_module_tables(
            ['scheme', 'holder']
        )
        if status:
            if self.current_profile is None:
                self.default_profile()
                return
            if len(db_user_tables(self.current_profile)) < 1:
                self.minimum_table_checker()
                return
            title = QApplication.translate(
                "STDMPlugin",
                "FLTS Document Designer"
            )
            documentComposer = self.iface.createNewComposer(
                title
            )
            # Embed STDM customizations
            composerWrapper = ComposerWrapper(
                documentComposer, self.iface
            )
            composerWrapper.configure()

    def onDocumentGenerator(self):
        """
        Document generator by person dialog.
        """
        status, tables = self.check_module_tables(
            ['scheme', 'holder', 'certificate', 'plot']
        )
        if status:
            if self.current_profile is None:
                self.default_profile()
                return
            if len(db_user_tables(self.current_profile)) < 1:
                self.minimum_table_checker()
                return
            doc_gen_wrapper = CertificateGeneratorDialogWrapper(
                self.iface,
                self.iface.mainWindow(),
                plugin=self
            )
            doc_gen_wrapper.exec_()

    def onReportGenerator(self):
        """
        Report generator for CB-FLTS
        """
        status, tables = self.check_module_tables(
            ['scheme', 'holder']
        )
        if status:
            if self.current_profile is None:
                self.default_profile()
                return
            if len(db_user_tables(self.current_profile)) < 1:
                self.minimum_table_checker()
                return
            report_gen_wrapper = ReportGeneratorDialogWrapper(
                self.iface,
                self.iface.mainWindow(),
                plugin=self
            )
            report_gen_wrapper.exec_()

    def onImportData(self):
        """
        Show import data wizard.
        """
        if self.current_profile is None:
            self.default_profile()
            return

        if len(db_user_tables(self.current_profile)) < 1:
            self.minimum_table_checker()
            return
        try:
            importData = ImportData(
                self.iface.mainWindow()
            )
            status = importData.exec_()
            if status == 1:
                if importData.geomClm.isEnabled():
                    canvas = self.iface.mapCanvas()
                    active_layer = self.iface.activeLayer()
                    if not active_layer is None:
                        canvas.zoomToFullExtent()
                        extent = active_layer.extent()
                        canvas.setExtent(extent)
        except Exception as ex:
            LOGGER.debug(unicode(ex))

    def onExportData(self):
        """
        Show export data dialog.
        """
        if self.current_profile is None:
            self.default_profile()
            return
        if len(db_user_tables(self.current_profile)) < 1:
            self.minimum_table_checker()
            return
        exportData = ExportData(self.iface.mainWindow())
        exportData.exec_()

    def onToggleSpatialUnitManger(self, toggled):
        """
        Slot raised on toggling to activate/deactivate
        editing, and load corresponding
        spatial tools.
        """
        self.spatialLayerManager.setChecked(False)
        pass

    def onViewSTR(self):
        """
        Slot for showing widget that enables users to browse
        existing STRs.
        """
        if self.current_profile == None:
            self.default_profile()
            return
        db_status = self.entity_table_checker(
            self.current_profile.social_tenure
        )

        if db_status:
            if self.viewSTRWin is None:
                self.viewSTRWin = ViewSTRWidget(self)
                self.viewSTRWin.show()
            else:
                self.viewSTRWin.showNormal()
                self.viewSTRWin.setFocus()

    def isSTDMLayer(self, layer):
        """
        Return whether the layer is an STDM layer.
        """
        if layer.id() in pg_layerNamesIDMapping().reverse:
            return True
        return False

    def widgetLoader(self, QAction):
        # Method to load custom forms
        tbList = self._moduleItems.values()

        dispName = QAction.text()
        if dispName == QApplication.translate(
                'STDMQGISLoader',
                'New Social Tenure Relationship'
        ):

            if self.current_profile is None:
                self.default_profile()
                return

            database_status = self.entity_table_checker(
                self.current_profile.social_tenure
            )

            if database_status:
                self.newSTR()


        else:
            table_name = self._moduleItems[dispName]
            if self.current_profile is None:
                self.default_profile()
                return
            sel_entity = self.current_profile.entity_by_name(
                table_name
            )

            database_status = self.entity_table_checker(
                sel_entity
            )
            QApplication.processEvents()
            try:
                if table_name in tbList and database_status:
                    cnt_idx = getIndex(
                        self._reportModules.keys(), dispName
                    )
                    self.entity_browser = EntityBrowserWithEditor(
                        sel_entity,
                        self.iface.mainWindow(),
                        plugin=self
                    )
                    if sel_entity.has_geometry_column():
                        self.entity_browser.show()
                    else:
                        self.entity_browser.exec_()

                else:
                    return

            except Exception as ex:
                QMessageBox.critical(
                    self.iface.mainWindow(),
                    QApplication.translate(
                        "STDMPlugin", "Error Loading Entity Browser"
                    ),
                    QApplication.translate(
                        "STDMPlugin",
                        "Unable to load the entity in the browser. "
                        "Check if the entity is configured correctly. "
                        "Error: %s") % unicode(ex.message))
            finally:
                STDMDb.instance().session.rollback()

    def about(self):
        """
        STDM Description
        """
        plugin_manager = self.iface.pluginManagerInterface()
        stdm_metadata = plugin_manager.pluginMetadata('stdm')
        abtDlg = AboutSTDMDialog(self.iface.mainWindow(), stdm_metadata)
        abtDlg.exec_()

    def load_license_agreement(self):
        """
        Loads the license agreement dialog if the user
        have never accepted the terms and conditions.
        :return: True if the license agreement is
        accepted already and false if not accepted.
        :rtype: Boolean
        """
        license_agreement = LicenseAgreement(
            self.iface.mainWindow()
        )
        license_agreement.show_license()
        if license_agreement.accepted:
            return True
        else:
            return False

    def logout(self):
        """
        Logout the user and remove default user buttons when logged in
        """
        for name, widget in DockWidgetFactory.saved_widgets.items():
            if widget:
                widget.close()
                # TODO state when layer is dirty
                # if no:
                # return

        try:
            self.stdmInitToolbar.removeAction(self.logoutAct)
            self.stdmInitToolbar.removeAction(self.changePasswordAct)
            self.stdmInitToolbar.removeAction(self.wzdAct)
            self.stdmInitToolbar.removeAction(self.contentAuthAct)
            self.stdmInitToolbar.removeAction(self.options_act)
            self.stdmInitToolbar.removeAction(self.docDesignerAct)
            self.stdmInitToolbar.removeAction(self.docGeneratorAct)
            self.stdmInitToolbar.removeAction(self.schemeLodgementAct)
            self.stdmInitToolbar.removeAction(self.schemeEstablishmentAct)
            self.stdmInitToolbar.removeAction(self.schemeRevisionAct)
            self.stdmInitToolbar.removeAction(self.firstExaminationAct)
            self.stdmInitToolbar.removeAction(self.secondExaminationAct)
            self.stdmInitToolbar.removeAction(self.thirdExaminationAct)
            self.stdmInitToolbar.removeAction(self.printCertificateAct)
            self.stdmInitToolbar.removeAction(self.scanCertificateAct)
            self.stdmInitToolbar.removeAction(self.searchAct)
            self.stdmInitToolbar.removeAction(self.cert_upload_act)
            self.stdmInitToolbar.removeAction(self.reportAct)
            # Clear current user name from status bar
            self.flts_status_label.clear()

            if self.toolbarLoader is not None:
                self.toolbarLoader.unloadContent()
            if self.menubarLoader is not None:
                self.menubarLoader.unloadContent()
                self.stdmMenu.clear()

            self.logoutCleanUp()
            self.initMenuItems()
            self.loginAct.setEnabled(True)
            self._user_logged_in = False
        except Exception as ex:
            LOGGER.debug(unicode(ex))

    def removeSTDMLayers(self):
        """
        Remove all STDM layers from the map registry.
        """
        mapLayers = QgsMapLayerRegistry.instance().mapLayers().values()

        for layer in mapLayers:
            if self.isSTDMLayer(layer):
                QgsMapLayerRegistry.instance().removeMapLayer(layer.id())

        self.stdmTables = []

    def logoutCleanUp(self, reload_plugin=False):
        """
        Clear database connection references and content items.
        :param reload_plugin: A boolean determining if the cleanup is
        called from reload_plugin method or not.
        :type reload_plugin: Boolean
        """
        try:
            if not self._user_logged_in:
                return

            # Remove STDM layers
            self.removeSTDMLayers()

            # Remove Spatial Unit Manager
            self.remove_spatial_unit_mgr()

            # Close search dock widget
            if self.search_dock_widget:
                self.search_dock_widget.close()
                self.search_dock_widget.clear()

            self.details_dock.close_dock()

            if not reload_plugin:
                self.profile_status_label.deleteLater()
                self.profile_status_label = None
                # Clear current profile combobox
                self.profiles_combobox.deleteLater()
                self.profiles_combobox = None
                # Clear singleton ref for SQLAlchemy connections
                if not data.app_dbconn is None:
                    STDMDb.cleanUp()
                    DeclareMapping.cleanUp()
                # Remove database reference
                data.app_dbconn = None
            else:
                self.profile_status_label.setText('')

            # Reset View STR Window
            if not self.viewSTRWin is None:
                del self.viewSTRWin
                self.viewSTRWin = None

            self.current_profile = None

        except Exception as ex:
            LOGGER.debug(unicode(ex))

    def remove_spatial_unit_mgr(self):
        """
        Removes spatial Unit Manger DockWidget.
        :return: None
        :rtype: NoneType
        """
        # if self.spatialLayerMangerDockWidget:
        #     self.spatialLayerManager.setChecked(False)
        #     self.spatialLayerMangerDockWidget.close()
        #     self.spatialLayerMangerDockWidget.deleteLater()
        # self.spatialLayerMangerDockWidget = None
        pass

    def user_entities(self):
        """
        Create a handler to read the current profile
        and return the table list
        """
        entities = []
        if self.current_profile is not None:
            entities = [
                (e.name, e.short_name, e.ui_display())
                for e in
                self.current_profile.entities.values()
                if (e.TYPE_INFO == 'ENTITY') and (e.user_editable)
            ]
        return entities

    def help_contents(self):
        """
        Load and open documentation manual
        """
        help_manual = u'{0}/flts.chm'.format(self.plugin_dir)
        try:
            os.startfile(
                help_manual, 'open'
            )
        except Exception as ex:
            QMessageBox.critical(
                self.iface.mainWindow(),
                QApplication.translate(
                    "STDMQGISLoader",
                    'Open Error'
                ),
                unicode(ex)
            )

    def reset_content_modules_id(self, title, message_text):
        return QMessageBox.critical(
            self.iface.mainWindow(), title,
            QApplication.translate(
                "STDMQGISLoader",
                unicode(message_text)
            )
        )

    def _action_separator(self):
        """
        :return: Toolbar or menu separator
        :rtype: QAction
        """
        separator = QAction(self.iface.mainWindow())
        separator.setSeparator(True)

        return separator

    def spatialLayerMangerActivate(self):
        if self.spatialLayerMangerDockWidget is None:
            self.create_spatial_unit_manager(True)
        else:
            if self.spatialLayerMangerDockWidget.isVisible():
                self.spatialLayerMangerDockWidget.hide()
            else:
                self.spatialLayerMangerDockWidget.show()

    def mobile_form_generator(self):
        """
        Load the dialog to generate form for mobile data collection
        :return:
        """
        converter_dlg = GeoODKConverter(self.iface.mainWindow())
        converter_dlg.exec_()

    def mobile_form_importer(self):
        """
        Load the dialog to generate form for mobile data collection
        :return:
        """
        importer_dialog = ProfileInstanceRecords(self.iface.mainWindow())
        importer_dialog.exec_()

    def default_config_version(self):
        handler = self.config_loader()
        config_version = handler.read_config_version()
        if float(config_version) < 1.2:
            msg_title = QApplication.translate("STDMQGISLoader",
                                               "Config file version")
            msg = QApplication.translate("STDMQGISLoader",
                                         "Your configuration file is "
                                         "older than the current stdm "
                                         "version, do you want to backup"
                                         "the configuration and database"
                                         "data")
            if QMessageBox.information(None, msg_title, msg,
                                       QMessageBox.Yes |
                                       QMessageBox.No) == QMessageBox.Yes:
                pass

        if config_version is None:
            msg_title = QApplication.translate("STDMQGISLoader",
                                               "Update config file")
            msg = QApplication.translate("STDMQGISLoader", "The config "
                                                           "version installed is old and "
                                                           "outdated STDM will try to "
                                                           "apply the required updates")
            if QMessageBox.information(None, msg_title, msg,
                                       QMessageBox.Yes |
                                       QMessageBox.No) == QMessageBox.Yes:
                handler.update_config_file()
            else:
                err_msg = QApplication.translate("STDMQGISLoader",
                                                 "STDM has detected that "
                                                 "the version of config "
                                                 "installed is old and "
                                                 "outdated. Delete "
                                                 "existing configuration "
                                                 "folder or xml file and "
                                                 "restart QGIS.")
                raise ConfigVersionException(err_msg)

    def load_shortcut_dlg(self):
        """
        Load the dialog for user to select actions.
        """
        shortcut_dlg = UserShortcutDialog(self.iface.mainWindow())
        shortcut_dlg.show_dialog()
        if shortcut_dlg.accepted:
            action_code = shortcut_dlg.action_code
            if action_code == 'LDG_SCM':
                self.lodge_scheme()
            elif action_code == 'EST_SCM':
                self.establish_scheme()
            elif action_code == 'EXM_SCM':
                self.first_examination()
            elif action_code == 'EXM2_SCM':
                self.second_examination()
            elif action_code == 'EXM3_SCM':
                self.third_examination()
            elif action_code == 'PLT_SCM':
                self.import_plots()
            elif action_code == 'D_CRT':
                self.onDocumentDesigner()
            elif action_code == 'G_CRT':
                self.onDocumentGenerator()
            elif action_code == 'G_RPT':
                self.onReportGenerator()
            # For search-related items, extract the data source name
            elif action_code.find(shortcut_dlg.search_item_prefix) != -1:
                data_source = action_code.split(shortcut_dlg.search_item_prefix)
                if len(data_source) > 1:
                    self.show_search_by_datasource(data_source[1])
            return True
        else:
            return False

    def lodge_scheme(self):
        """
        Load the wizard for lodgement of scheme.
        """
        status, tables = self.check_module_tables(
            ['scheme', 'holder', 'relevant_authority']
        )
        if status:
            lodge_wizard = LodgementWizard(self.iface.mainWindow())
            lodge_wizard.exec_()

    def establish_scheme(self):
        """
        Docks Scheme establishment workflow manager widget
        """
        workflow_manager = WorkflowManagerWidget(
            "Scheme Establishment",
            "schemeEstablishment",
            Qt.BottomDockWidgetArea
        )
        status, tables = self.check_module_tables(
            ['scheme', 'holder', 'scheme_workflow']
        )
        if status:
            self.dock_widget = DockWidgetFactory(workflow_manager, self.iface)
            self.dock_widget.show_dock_widget()

    def first_examination(self):
        """
        Docks First Examination workflow manager widget
        """
        workflow_manager = WorkflowManagerWidget(
            "First Examination",
            "firstExamination",
            Qt.BottomDockWidgetArea
        )
        status, tables = self.check_module_tables(
            ['scheme', 'holder', 'scheme_workflow']
        )
        if status:
            self.dock_widget = DockWidgetFactory(workflow_manager, self.iface)
            self.dock_widget.show_dock_widget()

    def second_examination(self):
        """
        Docks Second Examination workflow manager widget
        """
        workflow_manager = WorkflowManagerWidget(
            "Second Examination",
            "secondExamination",
            Qt.BottomDockWidgetArea
        )
        status, tables = self.check_module_tables(
            ['scheme', 'holder', 'scheme_workflow']
        )
        if status:
            self.dock_widget = DockWidgetFactory(workflow_manager, self.iface)
            self.dock_widget.show_dock_widget()

    def third_examination(self):
        """
        Docks Third Examination workflow manager widget
        """
        workflow_manager = WorkflowManagerWidget(
            "Third Examination",
            "thirdExamination",
            Qt.LeftDockWidgetArea
        )
        status, tables = self.check_module_tables(
            ['scheme', 'holder', 'scheme_workflow', 'plot']
        )
        if status:
            self.dock_widget = DockWidgetFactory(workflow_manager, self.iface)
            self.dock_widget.show_dock_widget()

    def revise_scheme(self):
        """
        Docks Revise Scheme workflow manager widget
        """
        workflow_manager = WorkflowManagerWidget(
            "Scheme Revision",
            "schemeLodgement",
            Qt.BottomDockWidgetArea
        )
        status, tables = self.check_module_tables(
            ['scheme', 'holder']
        )
        if status:
            self.dock_widget = DockWidgetFactory(workflow_manager, self.iface)
            self.dock_widget.show_dock_widget()

    def import_plots(self):
        """
        Docks Import Plot workflow manager widget
        """
        workflow_manager = WorkflowManagerWidget(
            "Plot Import",
            "importPlot",
            Qt.LeftDockWidgetArea
        )
        status, tables = self.check_module_tables(
            ['scheme', 'holder', 'scheme_workflow', 'plot']
        )
        if status:
            self.dock_widget = DockWidgetFactory(workflow_manager, self.iface)
            self.dock_widget.show_dock_widget()

    def on_cert_upload(self):
        """
        Certificate upload
        """
        status, tables = self.check_module_tables(
            ['scheme', 'holder', 'scheme_workflow', 'plot', 'certificate']
        )
        if status:
            if not self.cert_upload_widget:
                self.cert_upload_widget = CertificateUploadWidget()

            self.cert_upload_widget.show()
            self.cert_upload_widget.raise_()

    def check_module_tables(self, entities, show_err=True):
        """
        Check entities
        """
        tables_not_exist = []
        # get the current profile
        cp = self.current_profile
        if not cp:
            return False, tables_not_exist

        # get profile prefix
        prefix = cp.prefix
        for ent in entities:
            ent_name = '{0}_{1}'.format(prefix, ent)
            # check which tables exist
            if not pg_table_exists(ent_name):
                tables_not_exist.append(ent_name)

        if len(tables_not_exist) > 0:
            if show_err:
                tables_msg = '\n- '.join(tables_not_exist)
                QMessageBox.critical(
                    self.iface.mainWindow(),
                    'Missing Tables',
                    'The following tables do not exist:\n- {0}\n{1}'.format(
                        tables_msg,
                        'Please contact the system administrator to re-run configuration.'
                    )
                )
            return False, tables_not_exist
        else:
            return True, tables_not_exist
