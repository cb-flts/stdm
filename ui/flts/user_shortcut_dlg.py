"""
/***************************************************************************
Name                 : user Shortcut Dialog
Description          : Dialog for selecting user actions after login.
Date                 : 01/July/2019
copyright            : (C) 2019 by Joseph Kariuki
email                : joehene@gmail.com
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
from PyQt4.QtCore import (
    Qt
)

from PyQt4.QtGui import (
    QDialog,
    QIcon,
    QListWidgetItem,
    QTreeWidgetItem,
    QMessageBox,
    QApplication
)

from stdm.settings.registryconfig import (
    RegistryConfig,
    SHOW_SHORTCUT_DIALOG
)
from stdm.settings.search_config import SearchConfigurationRegistry

from .ui_user_shortcut import Ui_UserShortcutDialog
from ..notification import NotificationBar, ERROR


class UserShortcutDialog(QDialog, Ui_UserShortcutDialog):
    """
    Dialog that provides shortcut actions upon successful login.
    """
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.reg_config = RegistryConfig()
        self.accepted = True

        # Scale widget sizes in the splitter
        self.splitter.setSizes([250, 400])
        self.load_categories()

        # Connect signals
        # On tree item changed
        self.tr_title_category.itemSelectionChanged.connect(
            self.on_category_item_changed
        )
        self.lsw_category_action.itemDoubleClicked.connect(
            self.on_category_list_item_db_clicked
        )

        self.buttonBox.accepted.connect(
            self.accept_dlg
        )

        # Select scheme item in the tree widget
        self.tr_title_category.setCurrentItem(self.lht_scheme_item)

        # Configure notification bar
        self.notif_bar = NotificationBar(self.vlNotification)

        # User selected action code upon accept
        self._action_code = ''

    def check_show_dialog(self):
        """
        Checks if flag in the registry has been set.
        Returns True to show shortcut dialog. If registry key
        is not yet set, show the dialog.
        :rtype: boolean
        """
        show_dlg = 1
        dialog_key = self.reg_config.read(
            [SHOW_SHORTCUT_DIALOG]
        )

        if len(dialog_key) > 0:
            show_dlg = dialog_key[SHOW_SHORTCUT_DIALOG]

        if show_dlg == 1 or show_dlg == unicode(1):
            return True
        elif show_dlg == 0 or show_dlg == unicode(0):
            self.accepted = True
            return False

    @property
    def search_item_prefix(self):
        """
        :return: Returns a prefix code to be appended in search-related
        QListWidgetItems.
        :rtype: str
        """
        return 'SRCH_'

    def show_dialog(self):
        """
        Show shortcut dialog after login if the user has never
        selected to hide dialog.
        :return: None
        :rtype: NoneType
        """
        # validate if to show dialog
        show_dlg = self.check_show_dialog()
        # THe user didn't accept license
        if show_dlg:
            self.exec_()

    @property
    def action_code(self):
        """
        :return:Returns the code representing the user action
        :type: str
        """
        return self._action_code

    def module_icons(self):
        """
        Accessing the module icon file display.
        """
        # Container of list items based on category
        self._scheme_items = []
        self._certificate_items = []
        self._report_items = []
        self._search_items = []

        self.lsi_lodge_scheme = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_lodgement.png'),
            self.tr('Lodgement')
        )
        self.lsi_establish_scheme = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_scheme_establishment.png'),
            self.tr('Establishment')
        )
        self.lsi_first_examination = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_scheme_management_assessment1.png'),
            self.tr('First Examination')
        )
        self.lsi_second_examination = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_scheme_management_assessment2.png'),
            self.tr('Second Examination')
        )
        self.lsi_third_examination = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_scheme_management_assessment3.png'),
            self.tr('Third Examination')
        )
        self.lsi_revision = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_revision.png'),
            self.tr('Revision')
        )
        self.lsi_import_plots = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_scheme_import_plot.png'),
            self.tr('Import Plots')
        )
        self.lsi_design_certificate = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_document_designer.png'),
            self.tr('Design Certificate')
        )
        self.lsi_print_certificate = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_document_generator.png'),
            self.tr('Generate Certificate')
        )
        self.lsi_scan_certificate = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_certificate_scan.png'),
            self.tr('Upload Certificate')
        )
        self.lsi_search = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_search.png'),
            self.tr('Search')
        )
        self.lsi_search_holder = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_search_holder.png'),
            self.tr('Holder')
        )
        self.lsi_search_plot = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_search_plot.png'),
            self.tr('Plot')
        )
        self.lsi_design_report = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_document_designer.png'),
            self.tr('Design Report')
        )
        self.lsi_report = QListWidgetItem(
            QIcon(':/plugins/stdm/images/icons/flts_report.png'),
            self.tr('Generate Report')
        )

        # Assign unique identifier to the list item
        self.lsi_lodge_scheme.setData(Qt.UserRole, 'LDG_SCM')
        self.lsi_establish_scheme.setData(Qt.UserRole, 'EST_SCM')
        self.lsi_first_examination.setData(Qt.UserRole, 'EXM_SCM')
        self.lsi_second_examination.setData(Qt.UserRole, 'EXM2_SCM')
        self.lsi_third_examination.setData(Qt.UserRole, 'EXM3_SCM')
        self.lsi_import_plots.setData(Qt.UserRole, 'PLT_SCM')
        self.lsi_design_certificate.setData(Qt.UserRole, 'D_CRT')
        self.lsi_design_report.setData(Qt.UserRole, 'D_CRT')
        self.lsi_scan_certificate.setData(Qt.UserRole, 'S_CRT')
        self.lsi_report.setData(Qt.UserRole, 'G_RPT')
        self.lsi_search.setData(Qt.UserRole, 'SRC')

        # Assigning items to the scheme items
        self._scheme_items.append(self.lsi_lodge_scheme)
        self._scheme_items.append(self.lsi_establish_scheme)
        self._scheme_items.append(self.lsi_first_examination)
        self._scheme_items.append(self.lsi_second_examination)
        self._scheme_items.append(self.lsi_third_examination)
        self._scheme_items.append(self.lsi_import_plots)

        # Certificate items
        self._certificate_items.append(self.lsi_design_certificate)
        self._certificate_items.append(self.lsi_scan_certificate)

        # Search items adapted from items in the registry
        self._search_items = self._search_list_items()

        # Report items
        self._report_items.append(self.lsi_design_report)
        self._report_items.append(self.lsi_report)

    def _search_list_items(self):
        # Creates a list of QListWidgetItems based on the search
        # configuration items in the search registry.
        search_items = []
        for act in SearchConfigurationRegistry.instance().actions():
            si = QListWidgetItem(
                act.icon(),
                act.text()
            )
            # Code based on search prefix and data source name
            code = self.search_item_prefix + act.data()
            si.setData(Qt.UserRole, code)
            search_items.append(si)

        return search_items

    def load_categories(self):
        # Load items based on category selection
        self.lht_tr_item = QTreeWidgetItem(['Land Hold Title', 'LHT'])
        self.lht_scheme_item = QTreeWidgetItem(['Scheme', 'SCM'])
        self.lht_certificate_item = QTreeWidgetItem(['Certificate', 'CRT'])
        self.lht_search_item = QTreeWidgetItem(['Search', 'SRC'])
        self.lht_report_item = QTreeWidgetItem(['Report', 'RPT'])

        self.tr_title_category.addTopLevelItem(self.lht_tr_item)
        # Hide code column
        self.tr_title_category.hideColumn(1)

        self.lht_tr_item.addChild(self.lht_scheme_item)
        self.lht_tr_item.addChild(self.lht_search_item)
        self.lht_tr_item.addChild(self.lht_certificate_item)
        self.lht_tr_item.addChild(self.lht_report_item)

        # Expand base categories
        self.tr_title_category.expandItem(self.lht_tr_item)

    def _clear_category_items(self):
        # Remove all items without deleting them
        for i in range(self.lsw_category_action.count()):
            row_item = self.lsw_category_action.item(i)
            if row_item != 0:
                self.lsw_category_action.takeItem(i)

    def _load_category_items(self, lst_items):
        for it in lst_items:
            self.lsw_category_action.addItem(it)

    def on_category_item_changed(self):
        # Load list items based on selected category
        # Clear list first
        self.lsw_category_action.clear()

        sel_tr_items = self.tr_title_category.selectedItems()
        if len(sel_tr_items) == 0:
            return

        self.module_icons()
        # Get selected items
        tr_cat_item = sel_tr_items[0]
        cat_code = tr_cat_item.data(1, Qt.DisplayRole)
        if cat_code == 'SCM':
            self._load_category_items(self._scheme_items)
        elif cat_code == 'CRT':
            self._load_category_items(self._certificate_items)
        elif cat_code == 'RPT':
            self._load_category_items(self._report_items)
        elif cat_code == 'SRC':
            self._load_category_items(self._search_items)

    def on_category_list_item_db_clicked(self, item):
        # Load dialog based on specified action
        # get selected items
        data = item.data(Qt.UserRole)
        self._action_code = data
        self.accept_dlg()

    def accept_dlg(self):
        # Check if the user has selected an action from the list widget
        self.notif_bar.clear()

        selected_items = self.lsw_category_action.selectedItems()

        if len(selected_items) == 0:
            self.notif_bar.insertWarningNotification(
                self.tr("Please select an operation to perform"))
            return

        self._action_code = selected_items[0].data(Qt.UserRole)

        if self.chb_donotshow.isChecked():
            self.reg_config.write({SHOW_SHORTCUT_DIALOG: 0})
            self.accepted = True

        self.accept()

