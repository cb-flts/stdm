"""
/***************************************************************************
Name                 : Social Tenure Domain Model
Description          : QGIS Entry Point for Social Tenure Domain Model
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
import sys
import os

import logging
from logging.handlers import TimedRotatingFileHandler

# Import qgis.core so that the correct SIP versions are loaded in tests
from qgis.core import *

from PyQt4.QtGui import (
    QDesktopServices
)
from PyQt4.QtCore import (
    QDir,
    QFile
)

# Load third party libraries
third_party_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               "third_party"))
font_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        "third_party/fontTools"))
STYLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'styles'))

if third_party_dir not in sys.path:
    sys.path.append(third_party_dir)
    sys.path.append(font_dir)

# Root to the path plugin directory
USER_PLUGIN_DIR = QDesktopServices.storageLocation(QDesktopServices.HomeLocation) \
                  + '/.stdm'

# Setup logging
LOG_DIR = u'{0}/logs'.format(USER_PLUGIN_DIR)
LOG_FILE_PATH = LOG_DIR + '/stdm_log'

# Search
SEARCH_DIR = u'{0}/search'.format(USER_PLUGIN_DIR)

# Templates directory
TEMPLATES_DIR = u'{0}/reports/templates'.format(USER_PLUGIN_DIR)


def setup_logger():
    from stdm.settings.registryconfig import debug_logging

    logger = logging.getLogger('stdm')
    logger.setLevel(logging.ERROR)

    # Create log directory if it does not exist
    log_folder = QDir()
    if not log_folder.exists(LOG_DIR):
        status = log_folder.mkpath(LOG_DIR)

        # Log directory could not be created
        if not status:
            raise IOError('Log directory for STDM could not be created.')

    # File handler for logging debug messages
    file_handler = TimedRotatingFileHandler(LOG_FILE_PATH, when='D',
                                            interval=1, backupCount=14)
    file_handler.setLevel(logging.DEBUG)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(file_handler)

    # Enable/disable debugging. Defaults to ERROR level.
    lvl = debug_logging()
    if lvl:
        file_handler.setLevel(logging.DEBUG)
    else:
        file_handler.setLevel(logging.ERROR)


def copy_core_configuration():
    """
    Copies the basic STDM configuration to the user directory if there is none.
    """
    core_config_path = u'{0}/templates/configuration.stc'.format(
        os.path.dirname(__file__)
    )

    # Exit if the core configuration does not exist
    if not QFile.exists(core_config_path):
        return

    # File name of previous configuration
    v1_1_config_path = u'{0}/stdmConfig.xml'.format(USER_PLUGIN_DIR)

    # Only copy the new one if there is no copy of the previous version
    # since the version updater will automatically handle the upgrade.
    if QFile.exists(v1_1_config_path):
        # Version update will handle the migration
        return

    # Copy config assuming that the plugin user folder has no previous
    # configuration.
    conf_file = QFile(core_config_path)
    conf_dest = u'{0}/configuration.stc'.format(USER_PLUGIN_DIR)

    copy_status = conf_file.copy(conf_dest)


def copy_holders_configuration():
    """
    Copies the default configuration for holders data source to destination
    mapping if there is none in the .stdm folder.
    """
    holders_config_path = u'{0}/templates/holders_config.ini'.format(
        os.path.dirname(__file__)
    )

    # Exit if the holder config mapping does not exist
    if not QFile.exists(holders_config_path):
        return

    # Copy mapping file if none existed in USER_PLUGIN_DIR
    holders_conf_file = QFile(holders_config_path)
    holders_conf_dest = u'{0}/holders_config.ini'.format(USER_PLUGIN_DIR)

    copy_status = holders_conf_file.copy(holders_conf_dest)


def setup_templates_folder():
    # Create reports directory and templates sub-directory if it does not
    # exist
    reports_folder = QDir()
    if not reports_folder.exists(TEMPLATES_DIR):
        status = reports_folder.mkpath(TEMPLATES_DIR)

        # Log directory could not be created
        if not status:
            raise IOError('Reports directory for FLTS could not be created.')


def setup_search():
    # Create search directory if it does not exist
    search_folder = QDir()
    if not search_folder.exists(SEARCH_DIR):
        status = search_folder.mkpath(SEARCH_DIR)

        # Log directory could not be created
        if not status:
            raise IOError('Search directory for FLTS could not be created.')


def copy_search_configuration():
    """
    Copies the configuration file containing the search settings to the
    user's ./stdm/search folder.
    """
    search_conf_path = u'{0}/templates/search/configuration.ini'.format(
        os.path.dirname(__file__)
    )

    # Exit if the search config file does not exist
    if not QFile.exists(search_conf_path):
        return

    # Copy settings file if none existed in USER_PLUGIN_DIR
    search_conf_file = QFile(search_conf_path)
    search_conf_dest = u'{0}/search/configuration.ini'.format(USER_PLUGIN_DIR)

    copy_status = search_conf_file.copy(search_conf_dest)


def classFactory(iface):
    """
    Load STDMQGISLoader class.
    """
    setup_logger()

    # Copy the basic configuration to the user folder if None exists
    copy_core_configuration()

    # Copy the holders mapping config file
    copy_holders_configuration()

    # Create Search folder
    setup_templates_folder()

    # Create Search folder
    setup_search()

    # Copy the search settings file
    copy_search_configuration()

    from stdm.plugin import STDMQGISLoader
    return STDMQGISLoader(iface)
