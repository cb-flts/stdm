# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scheme_lodgement.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ldg_wzd(object):
    def setupUi(self, ldg_wzd):
        ldg_wzd.setObjectName(_fromUtf8("ldg_wzd"))
        ldg_wzd.setEnabled(True)
        ldg_wzd.resize(702, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ldg_wzd.sizePolicy().hasHeightForWidth())
        ldg_wzd.setSizePolicy(sizePolicy)
        ldg_wzd.setMinimumSize(QtCore.QSize(255, 400))
        ldg_wzd.setMaximumSize(QtCore.QSize(1500, 900))
        ldg_wzd.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        ldg_wzd.setAcceptDrops(False)
        ldg_wzd.setWizardStyle(QtGui.QWizard.ModernStyle)
        ldg_wzd.setOptions(QtGui.QWizard.NoBackButtonOnStartPage)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.wizardPage1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.vlNotification = QtGui.QVBoxLayout()
        self.vlNotification.setContentsMargins(-1, -1, -1, 10)
        self.vlNotification.setObjectName(_fromUtf8("vlNotification"))
        self.gridLayout_2.addLayout(self.vlNotification, 0, 0, 1, 2)
        self.label_desc = QtGui.QLabel(self.wizardPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_desc.sizePolicy().hasHeightForWidth())
        self.label_desc.setSizePolicy(sizePolicy)
        self.label_desc.setObjectName(_fromUtf8("label_desc"))
        self.gridLayout_2.addWidget(self.label_desc, 1, 0, 1, 2)
        self.label_region = QtGui.QLabel(self.wizardPage1)
        self.label_region.setObjectName(_fromUtf8("label_region"))
        self.gridLayout_2.addWidget(self.label_region, 2, 0, 1, 1)
        self.cbx_region = QtGui.QComboBox(self.wizardPage1)
        self.cbx_region.setObjectName(_fromUtf8("cbx_region"))
        self.gridLayout_2.addWidget(self.cbx_region, 2, 1, 1, 1)
        self.label_rel_auth_type = QtGui.QLabel(self.wizardPage1)
        self.label_rel_auth_type.setObjectName(_fromUtf8("label_rel_auth_type"))
        self.gridLayout_2.addWidget(self.label_rel_auth_type, 3, 0, 1, 1)
        self.cbx_relv_auth = QtGui.QComboBox(self.wizardPage1)
        self.cbx_relv_auth.setObjectName(_fromUtf8("cbx_relv_auth"))
        self.gridLayout_2.addWidget(self.cbx_relv_auth, 3, 1, 1, 1)
        self.label_rel_auth_name = QtGui.QLabel(self.wizardPage1)
        self.label_rel_auth_name.setObjectName(_fromUtf8("label_rel_auth_name"))
        self.gridLayout_2.addWidget(self.label_rel_auth_name, 4, 0, 1, 1)
        self.cbx_relv_auth_name = QtGui.QComboBox(self.wizardPage1)
        self.cbx_relv_auth_name.setObjectName(_fromUtf8("cbx_relv_auth_name"))
        self.gridLayout_2.addWidget(self.cbx_relv_auth_name, 4, 1, 1, 1)
        self.label_schm_num = QtGui.QLabel(self.wizardPage1)
        self.label_schm_num.setObjectName(_fromUtf8("label_schm_num"))
        self.gridLayout_2.addWidget(self.label_schm_num, 5, 0, 1, 1)
        self.lnedit_schm_num = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_schm_num.setReadOnly(True)
        self.lnedit_schm_num.setObjectName(_fromUtf8("lnedit_schm_num"))
        self.gridLayout_2.addWidget(self.lnedit_schm_num, 5, 1, 1, 1)
        self.label_schm_name = QtGui.QLabel(self.wizardPage1)
        self.label_schm_name.setObjectName(_fromUtf8("label_schm_name"))
        self.gridLayout_2.addWidget(self.label_schm_name, 6, 0, 1, 1)
        self.lnedit_schm_nam = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_schm_nam.setObjectName(_fromUtf8("lnedit_schm_nam"))
        self.gridLayout_2.addWidget(self.lnedit_schm_nam, 6, 1, 1, 1)
        self.label_date_apprv = QtGui.QLabel(self.wizardPage1)
        self.label_date_apprv.setObjectName(_fromUtf8("label_date_apprv"))
        self.gridLayout_2.addWidget(self.label_date_apprv, 7, 0, 1, 1)
        self.date_apprv = QtGui.QDateEdit(self.wizardPage1)
        self.date_apprv.setMinimumDate(QtCore.QDate(2009, 9, 22))
        self.date_apprv.setCalendarPopup(True)
        self.date_apprv.setObjectName(_fromUtf8("date_apprv"))
        self.gridLayout_2.addWidget(self.date_apprv, 7, 1, 1, 1)
        self.label_date_establish = QtGui.QLabel(self.wizardPage1)
        self.label_date_establish.setObjectName(_fromUtf8("label_date_establish"))
        self.gridLayout_2.addWidget(self.label_date_establish, 8, 0, 1, 1)
        self.date_establish = QtGui.QDateEdit(self.wizardPage1)
        self.date_establish.setMinimumDate(QtCore.QDate(2019, 9, 14))
        self.date_establish.setCalendarPopup(True)
        self.date_establish.setObjectName(_fromUtf8("date_establish"))
        self.gridLayout_2.addWidget(self.date_establish, 8, 1, 1, 1)
        self.label_lro = QtGui.QLabel(self.wizardPage1)
        self.label_lro.setObjectName(_fromUtf8("label_lro"))
        self.gridLayout_2.addWidget(self.label_lro, 9, 0, 1, 1)
        self.cbx_lro = QtGui.QComboBox(self.wizardPage1)
        self.cbx_lro.setObjectName(_fromUtf8("cbx_lro"))
        self.gridLayout_2.addWidget(self.cbx_lro, 9, 1, 1, 1)
        self.label_twn_name = QtGui.QLabel(self.wizardPage1)
        self.label_twn_name.setObjectName(_fromUtf8("label_twn_name"))
        self.gridLayout_2.addWidget(self.label_twn_name, 10, 0, 1, 1)
        self.lnedit_twnshp = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_twnshp.setObjectName(_fromUtf8("lnedit_twnshp"))
        self.gridLayout_2.addWidget(self.lnedit_twnshp, 10, 1, 1, 1)
        self.label_reg_div = QtGui.QLabel(self.wizardPage1)
        self.label_reg_div.setObjectName(_fromUtf8("label_reg_div"))
        self.gridLayout_2.addWidget(self.label_reg_div, 11, 0, 1, 1)
        self.cbx_reg_div = QtGui.QComboBox(self.wizardPage1)
        self.cbx_reg_div.setObjectName(_fromUtf8("cbx_reg_div"))
        self.gridLayout_2.addWidget(self.cbx_reg_div, 11, 1, 1, 1)
        self.label_blck_area = QtGui.QLabel(self.wizardPage1)
        self.label_blck_area.setObjectName(_fromUtf8("label_blck_area"))
        self.gridLayout_2.addWidget(self.label_blck_area, 12, 0, 1, 1)
        self.dbl_spinbx_block_area = QtGui.QDoubleSpinBox(self.wizardPage1)
        self.dbl_spinbx_block_area.setDecimals(4)
        self.dbl_spinbx_block_area.setMaximum(10000000.0)
        self.dbl_spinbx_block_area.setObjectName(_fromUtf8("dbl_spinbx_block_area"))
        self.gridLayout_2.addWidget(self.dbl_spinbx_block_area, 12, 1, 1, 1)
        ldg_wzd.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.wizardPage2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.vlNotification_2 = QtGui.QVBoxLayout()
        self.vlNotification_2.setContentsMargins(-1, -1, -1, 10)
        self.vlNotification_2.setObjectName(_fromUtf8("vlNotification_2"))
        self.gridLayout_3.addLayout(self.vlNotification_2, 0, 0, 1, 2)
        self.label_desc_2 = QtGui.QLabel(self.wizardPage2)
        self.label_desc_2.setObjectName(_fromUtf8("label_desc_2"))
        self.gridLayout_3.addWidget(self.label_desc_2, 1, 0, 1, 1)
        self.lnEdit_hld_path = QtGui.QLineEdit(self.wizardPage2)
        self.lnEdit_hld_path.setEnabled(True)
        self.lnEdit_hld_path.setObjectName(_fromUtf8("lnEdit_hld_path"))
        self.gridLayout_3.addWidget(self.lnEdit_hld_path, 2, 0, 1, 1)
        self.btn_brws_hld = QtGui.QPushButton(self.wizardPage2)
        self.btn_brws_hld.setDefault(True)
        self.btn_brws_hld.setObjectName(_fromUtf8("btn_brws_hld"))
        self.gridLayout_3.addWidget(self.btn_brws_hld, 2, 1, 1, 1)
        self.label_data_prev = QtGui.QLabel(self.wizardPage2)
        self.label_data_prev.setObjectName(_fromUtf8("label_data_prev"))
        self.gridLayout_3.addWidget(self.label_data_prev, 3, 0, 1, 1)
        self.btn_validate_holders = QtGui.QPushButton(self.wizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_validate_holders.sizePolicy().hasHeightForWidth())
        self.btn_validate_holders.setSizePolicy(sizePolicy)
        self.btn_validate_holders.setObjectName(_fromUtf8("btn_validate_holders"))
        self.gridLayout_3.addWidget(self.btn_validate_holders, 5, 1, 1, 1)
        self.tw_hld_prv = ExcelWorkbookView(self.wizardPage2)
        self.tw_hld_prv.setObjectName(_fromUtf8("tw_hld_prv"))
        # self.tw_hld_prv.setColumnCount(0)
        # self.tw_hld_prv.setRowCount(0)
        self.gridLayout_3.addWidget(self.tw_hld_prv, 4, 0, 1, 2)
        ldg_wzd.addPage(self.wizardPage2)
        self.wizardPage = QtGui.QWizardPage()
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        self.gridLayout = QtGui.QGridLayout(self.wizardPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vlNotification_3 = QtGui.QVBoxLayout()
        self.vlNotification_3.setContentsMargins(-1, -1, -1, 10)
        self.vlNotification_3.setObjectName(_fromUtf8("vlNotification_3"))
        self.gridLayout.addLayout(self.vlNotification_3, 0, 0, 1, 2)
        self.label_desc_3 = QtGui.QLabel(self.wizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_desc_3.sizePolicy().hasHeightForWidth())
        self.label_desc_3.setSizePolicy(sizePolicy)
        self.label_desc_3.setMinimumSize(QtCore.QSize(0, 15))
        self.label_desc_3.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_desc_3.setLineWidth(0)
        self.label_desc_3.setWordWrap(True)
        self.label_desc_3.setObjectName(_fromUtf8("label_desc_3"))
        self.gridLayout.addWidget(self.label_desc_3, 1, 0, 1, 2)
        self.tbw_documents = DocumentTableWidget(self.wizardPage)
        self.tbw_documents.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tbw_documents.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tbw_documents.setObjectName(_fromUtf8("tbw_documents"))
        # self.tbw_documents.setColumnCount(0)
        # self.tbw_documents.setRowCount(0)
        self.gridLayout.addWidget(self.tbw_documents, 2, 0, 1, 2)
        self.label_upld_multi = QtGui.QLabel(self.wizardPage)
        self.label_upld_multi.setObjectName(_fromUtf8("label_upld_multi"))
        self.gridLayout.addWidget(self.label_upld_multi, 3, 0, 1, 1)
        self.btn_upload_dir = QtGui.QPushButton(self.wizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upload_dir.sizePolicy().hasHeightForWidth())
        self.btn_upload_dir.setSizePolicy(sizePolicy)
        self.btn_upload_dir.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_upload_dir.setMaximumSize(QtCore.QSize(5000, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/flts_scheme_docs_dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_upload_dir.setIcon(icon)
        self.btn_upload_dir.setIconSize(QtCore.QSize(16, 16))
        self.btn_upload_dir.setObjectName(_fromUtf8("btn_upload_dir"))
        self.gridLayout.addWidget(self.btn_upload_dir, 3, 1, 1, 1)
        ldg_wzd.addPage(self.wizardPage)
        self.wizardPage_4 = QtGui.QWizardPage()
        self.wizardPage_4.setObjectName(_fromUtf8("wizardPage_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wizardPage_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_desc_4 = QtGui.QLabel(self.wizardPage_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_desc_4.sizePolicy().hasHeightForWidth())
        self.label_desc_4.setSizePolicy(sizePolicy)
        self.label_desc_4.setObjectName(_fromUtf8("label_desc_4"))
        self.verticalLayout_2.addWidget(self.label_desc_4)
        self.tr_summary = SchemeSummaryWidget(self.wizardPage_4)
        self.tr_summary.setUniformRowHeights(True)
        self.tr_summary.setObjectName(_fromUtf8("tr_summary"))
        self.verticalLayout_2.addWidget(self.tr_summary)
        ldg_wzd.addPage(self.wizardPage_4)

        self.retranslateUi(ldg_wzd)
        QtCore.QMetaObject.connectSlotsByName(ldg_wzd)

    def retranslateUi(self, ldg_wzd):
        ldg_wzd.setWindowTitle(_translate("ldg_wzd", "Lodgement of Scheme", None))
        self.label_desc.setText(_translate("ldg_wzd", "<html><head/><body><p>Enter scheme information below. Please note the scheme number will be automatically generated</p></body></html>", None))
        self.label_region.setText(_translate("ldg_wzd", "Region", None))
        self.label_rel_auth_type.setText(_translate("ldg_wzd", "Type of Relevant Authority", None))
        self.label_rel_auth_name.setText(_translate("ldg_wzd", "Name of Relevant Authority", None))
        self.label_schm_num.setText(_translate("ldg_wzd", "Scheme Number", None))
        self.label_schm_name.setText(_translate("ldg_wzd", "Scheme Name", None))
        self.label_date_apprv.setText(_translate("ldg_wzd", "Date of Approval", None))
        self.label_date_establish.setText(_translate("ldg_wzd", "Date of Esablishment", None))
        self.label_lro.setText(_translate("ldg_wzd", "Land Rights Office", None))
        self.label_twn_name.setText(_translate("ldg_wzd", "Township Name", None))
        self.label_reg_div.setText(_translate("ldg_wzd", "Registration Division", None))
        self.label_blck_area.setText(_translate("ldg_wzd", "Block Area", None))
        self.label_desc_2.setText(_translate("ldg_wzd", "Select the Excel file containing holders information", None))
        self.btn_brws_hld.setText(_translate("ldg_wzd", "Browse...", None))
        self.label_data_prev.setText(_translate("ldg_wzd", "Data preview", None))
        self.btn_validate_holders.setText(_translate("ldg_wzd", "Validate", None))
        self.wizardPage.setSubTitle(_translate("ldg_wzd", "Upload the supporting documents for the scheme", None))
        self.label_desc_3.setText(_translate("ldg_wzd", "<html><head/><body><p>Click the \'Browse\' link to add the individual supporting documents </p></body></html>", None))
        self.label_upld_multi.setText(_translate("ldg_wzd", "Add multiple files from a source directory", None))
        self.btn_upload_dir.setText(_translate("ldg_wzd", "Upload From Directory...", None))
        self.label_desc_4.setText(_translate("ldg_wzd", "Confirm the scheme information.Click Back to edit the information or Finish to save.  ", None))

from stdm.ui.customcontrols.documents_table_widget import DocumentTableWidget
from stdm.ui.customcontrols.scheme_summary_widget import SchemeSummaryWidget
from stdm.ui.customcontrols.table_widget import ExcelWorkbookView
from stdm import resources_rc
