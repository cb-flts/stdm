# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scheme_lodgement.ui'
#
# Created: Sun Apr 19 07:18:00 2020
#      by: PyQt4 UI code generator 4.10
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
        ldg_wzd.resize(755, 657)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ldg_wzd.sizePolicy().hasHeightForWidth())
        ldg_wzd.setSizePolicy(sizePolicy)
        ldg_wzd.setMinimumSize(QtCore.QSize(255, 400))
        ldg_wzd.setMaximumSize(QtCore.QSize(1500, 900))
        ldg_wzd.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        ldg_wzd.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/flts_lodgement.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ldg_wzd.setWindowIcon(icon)
        ldg_wzd.setWizardStyle(QtGui.QWizard.ModernStyle)
        ldg_wzd.setOptions(QtGui.QWizard.NoBackButtonOnStartPage)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.gridLayout_4 = QtGui.QGridLayout(self.wizardPage1)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_desc = QtGui.QLabel(self.wizardPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_desc.sizePolicy().hasHeightForWidth())
        self.label_desc.setSizePolicy(sizePolicy)
        self.label_desc.setObjectName(_fromUtf8("label_desc"))
        self.gridLayout_4.addWidget(self.label_desc, 1, 0, 1, 2)
        self.label_region = QtGui.QLabel(self.wizardPage1)
        self.label_region.setObjectName(_fromUtf8("label_region"))
        self.gridLayout_4.addWidget(self.label_region, 2, 0, 1, 1)
        self.cbx_region = QtGui.QComboBox(self.wizardPage1)
        self.cbx_region.setObjectName(_fromUtf8("cbx_region"))
        self.gridLayout_4.addWidget(self.cbx_region, 2, 1, 1, 1)
        self.label_rel_auth_type = QtGui.QLabel(self.wizardPage1)
        self.label_rel_auth_type.setObjectName(_fromUtf8("label_rel_auth_type"))
        self.gridLayout_4.addWidget(self.label_rel_auth_type, 3, 0, 1, 1)
        self.cbx_relv_auth = QtGui.QComboBox(self.wizardPage1)
        self.cbx_relv_auth.setObjectName(_fromUtf8("cbx_relv_auth"))
        self.gridLayout_4.addWidget(self.cbx_relv_auth, 3, 1, 1, 1)
        self.label_rel_auth_name = QtGui.QLabel(self.wizardPage1)
        self.label_rel_auth_name.setObjectName(_fromUtf8("label_rel_auth_name"))
        self.gridLayout_4.addWidget(self.label_rel_auth_name, 4, 0, 1, 1)
        self.cbx_relv_auth_name = QtGui.QComboBox(self.wizardPage1)
        self.cbx_relv_auth_name.setObjectName(_fromUtf8("cbx_relv_auth_name"))
        self.gridLayout_4.addWidget(self.cbx_relv_auth_name, 4, 1, 1, 1)
        self.label_reg_div = QtGui.QLabel(self.wizardPage1)
        self.label_reg_div.setObjectName(_fromUtf8("label_reg_div"))
        self.gridLayout_4.addWidget(self.label_reg_div, 5, 0, 1, 1)
        self.cbx_reg_div = QtGui.QComboBox(self.wizardPage1)
        self.cbx_reg_div.setObjectName(_fromUtf8("cbx_reg_div"))
        self.gridLayout_4.addWidget(self.cbx_reg_div, 5, 1, 1, 1)
        self.label_schm_num = QtGui.QLabel(self.wizardPage1)
        self.label_schm_num.setObjectName(_fromUtf8("label_schm_num"))
        self.gridLayout_4.addWidget(self.label_schm_num, 6, 0, 1, 1)
        self.lnedit_schm_num = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_schm_num.setInputMask(_fromUtf8(""))
        self.lnedit_schm_num.setText(_fromUtf8(""))
        self.lnedit_schm_num.setReadOnly(True)
        self.lnedit_schm_num.setObjectName(_fromUtf8("lnedit_schm_num"))
        self.gridLayout_4.addWidget(self.lnedit_schm_num, 6, 1, 1, 1)
        self.label_landhold_num = QtGui.QLabel(self.wizardPage1)
        self.label_landhold_num.setObjectName(_fromUtf8("label_landhold_num"))
        self.gridLayout_4.addWidget(self.label_landhold_num, 7, 0, 1, 1)
        self.lnedit_landhold_num = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_landhold_num.setInputMask(_fromUtf8(""))
        self.lnedit_landhold_num.setText(_fromUtf8(""))
        self.lnedit_landhold_num.setReadOnly(False)
        self.lnedit_landhold_num.setObjectName(_fromUtf8("lnedit_landhold_num"))
        self.gridLayout_4.addWidget(self.lnedit_landhold_num, 7, 1, 1, 1)
        self.label_sg_num = QtGui.QLabel(self.wizardPage1)
        self.label_sg_num.setObjectName(_fromUtf8("label_sg_num"))
        self.gridLayout_4.addWidget(self.label_sg_num, 8, 0, 1, 1)
        self.lnedit_sg_num = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_sg_num.setInputMask(_fromUtf8(""))
        self.lnedit_sg_num.setReadOnly(False)
        self.lnedit_sg_num.setObjectName(_fromUtf8("lnedit_sg_num"))
        self.gridLayout_4.addWidget(self.lnedit_sg_num, 8, 1, 1, 1)
        self.label_schm_name = QtGui.QLabel(self.wizardPage1)
        self.label_schm_name.setObjectName(_fromUtf8("label_schm_name"))
        self.gridLayout_4.addWidget(self.label_schm_name, 9, 0, 1, 1)
        self.lnedit_schm_nam = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_schm_nam.setText(_fromUtf8(""))
        self.lnedit_schm_nam.setObjectName(_fromUtf8("lnedit_schm_nam"))
        self.gridLayout_4.addWidget(self.lnedit_schm_nam, 9, 1, 1, 1)
        self.label_date_apprv = QtGui.QLabel(self.wizardPage1)
        self.label_date_apprv.setObjectName(_fromUtf8("label_date_apprv"))
        self.gridLayout_4.addWidget(self.label_date_apprv, 10, 0, 1, 1)
        self.date_apprv = QtGui.QDateEdit(self.wizardPage1)
        self.date_apprv.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_apprv.setMinimumDate(QtCore.QDate(2010, 1, 1))
        self.date_apprv.setCalendarPopup(True)
        self.date_apprv.setObjectName(_fromUtf8("date_apprv"))
        self.gridLayout_4.addWidget(self.date_apprv, 10, 1, 1, 1)
        self.label_date_establish = QtGui.QLabel(self.wizardPage1)
        self.label_date_establish.setObjectName(_fromUtf8("label_date_establish"))
        self.gridLayout_4.addWidget(self.label_date_establish, 11, 0, 1, 1)
        self.date_establish = QtGui.QDateEdit(self.wizardPage1)
        self.date_establish.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_establish.setMinimumDate(QtCore.QDate(2010, 1, 1))
        self.date_establish.setCalendarPopup(True)
        self.date_establish.setObjectName(_fromUtf8("date_establish"))
        self.gridLayout_4.addWidget(self.date_establish, 11, 1, 1, 1)
        self.label_lro = QtGui.QLabel(self.wizardPage1)
        self.label_lro.setObjectName(_fromUtf8("label_lro"))
        self.gridLayout_4.addWidget(self.label_lro, 12, 0, 1, 1)
        self.cbx_lro = QtGui.QComboBox(self.wizardPage1)
        self.cbx_lro.setObjectName(_fromUtf8("cbx_lro"))
        self.gridLayout_4.addWidget(self.cbx_lro, 12, 1, 1, 1)
        self.label_title_deed_num = QtGui.QLabel(self.wizardPage1)
        self.label_title_deed_num.setObjectName(_fromUtf8("label_title_deed_num"))
        self.gridLayout_4.addWidget(self.label_title_deed_num, 13, 0, 1, 1)
        self.lnedit_title_deed_num = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_title_deed_num.setObjectName(_fromUtf8("lnedit_title_deed_num"))
        self.gridLayout_4.addWidget(self.lnedit_title_deed_num, 13, 1, 1, 1)
        self.label_constitution_ref_num = QtGui.QLabel(self.wizardPage1)
        self.label_constitution_ref_num.setObjectName(_fromUtf8("label_constitution_ref_num"))
        self.gridLayout_4.addWidget(self.label_constitution_ref_num, 14, 0, 1, 1)
        self.lnedit_constitution_ref_num = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_constitution_ref_num.setText(_fromUtf8(""))
        self.lnedit_constitution_ref_num.setObjectName(_fromUtf8("lnedit_constitution_ref_num"))
        self.gridLayout_4.addWidget(self.lnedit_constitution_ref_num, 14, 1, 1, 1)
        self.label_scheme_description = QtGui.QLabel(self.wizardPage1)
        self.label_scheme_description.setObjectName(_fromUtf8("label_scheme_description"))
        self.gridLayout_4.addWidget(self.label_scheme_description, 15, 0, 1, 1)
        self.lnedit_scheme_description = QtGui.QLineEdit(self.wizardPage1)
        self.lnedit_scheme_description.setText(_fromUtf8(""))
        self.lnedit_scheme_description.setObjectName(_fromUtf8("lnedit_scheme_description"))
        self.gridLayout_4.addWidget(self.lnedit_scheme_description, 15, 1, 1, 1)
        self.label_num_plots = QtGui.QLabel(self.wizardPage1)
        self.label_num_plots.setObjectName(_fromUtf8("label_num_plots"))
        self.gridLayout_4.addWidget(self.label_num_plots, 16, 0, 1, 1)
        self.dbl_spinbx_num_plots = QtGui.QDoubleSpinBox(self.wizardPage1)
        self.dbl_spinbx_num_plots.setDecimals(0)
        self.dbl_spinbx_num_plots.setMaximum(200.0)
        self.dbl_spinbx_num_plots.setObjectName(_fromUtf8("dbl_spinbx_num_plots"))
        self.gridLayout_4.addWidget(self.dbl_spinbx_num_plots, 16, 1, 1, 1)
        self.gbx_block_area = QtGui.QGroupBox(self.wizardPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbx_block_area.sizePolicy().hasHeightForWidth())
        self.gbx_block_area.setSizePolicy(sizePolicy)
        self.gbx_block_area.setObjectName(_fromUtf8("gbx_block_area"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gbx_block_area)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_blck_area_units = QtGui.QLabel(self.gbx_block_area)
        self.label_blck_area_units.setObjectName(_fromUtf8("label_blck_area_units"))
        self.gridLayout_2.addWidget(self.label_blck_area_units, 0, 0, 1, 1)
        self.radio_hectares = QtGui.QRadioButton(self.gbx_block_area)
        self.radio_hectares.setObjectName(_fromUtf8("radio_hectares"))
        self.gridLayout_2.addWidget(self.radio_hectares, 0, 2, 1, 1)
        self.radio_sq_meters = QtGui.QRadioButton(self.gbx_block_area)
        self.radio_sq_meters.setObjectName(_fromUtf8("radio_sq_meters"))
        self.gridLayout_2.addWidget(self.radio_sq_meters, 0, 1, 1, 1)
        self.dbl_spinbx_block_area = QtGui.QDoubleSpinBox(self.gbx_block_area)
        self.dbl_spinbx_block_area.setDecimals(4)
        self.dbl_spinbx_block_area.setMaximum(10000000.0)
        self.dbl_spinbx_block_area.setObjectName(_fromUtf8("dbl_spinbx_block_area"))
        self.gridLayout_2.addWidget(self.dbl_spinbx_block_area, 1, 1, 1, 2)
        self.gridLayout_4.addWidget(self.gbx_block_area, 17, 0, 1, 2)
        self.label_mandatory = QtGui.QLabel(self.wizardPage1)
        self.label_mandatory.setObjectName(_fromUtf8("label_mandatory"))
        self.gridLayout_4.addWidget(self.label_mandatory, 18, 0, 1, 1)
        self.vlNotification = QtGui.QVBoxLayout()
        self.vlNotification.setContentsMargins(-1, -1, -1, 10)
        self.vlNotification.setObjectName(_fromUtf8("vlNotification"))
        self.gridLayout_4.addLayout(self.vlNotification, 0, 0, 1, 2)
        ldg_wzd.addPage(self.wizardPage1)
        self.wizardPage = QtGui.QWizardPage()
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        self.gridLayout = QtGui.QGridLayout(self.wizardPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
        self.label_desc_3.setMargin(1)
        self.label_desc_3.setObjectName(_fromUtf8("label_desc_3"))
        self.gridLayout.addWidget(self.label_desc_3, 1, 0, 1, 2)
        self.label_upld_multi = QtGui.QLabel(self.wizardPage)
        self.label_upld_multi.setObjectName(_fromUtf8("label_upld_multi"))
        self.gridLayout.addWidget(self.label_upld_multi, 3, 0, 1, 1)
        self.tbw_documents = DocumentTableWidget(self.wizardPage)
        self.tbw_documents.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tbw_documents.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tbw_documents.setObjectName(_fromUtf8("tbw_documents"))
        self.gridLayout.addWidget(self.tbw_documents, 2, 0, 1, 2)
        self.vlNotification_docs = QtGui.QVBoxLayout()
        self.vlNotification_docs.setContentsMargins(-1, -1, -1, 10)
        self.vlNotification_docs.setObjectName(_fromUtf8("vlNotification_docs"))
        self.gridLayout.addLayout(self.vlNotification_docs, 0, 0, 1, 2)
        self.btn_upload_dir = QtGui.QPushButton(self.wizardPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upload_dir.sizePolicy().hasHeightForWidth())
        self.btn_upload_dir.setSizePolicy(sizePolicy)
        self.btn_upload_dir.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_upload_dir.setMaximumSize(QtCore.QSize(5000, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/flts_scheme_docs_dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_upload_dir.setIcon(icon1)
        self.btn_upload_dir.setIconSize(QtCore.QSize(16, 16))
        self.btn_upload_dir.setObjectName(_fromUtf8("btn_upload_dir"))
        self.gridLayout.addWidget(self.btn_upload_dir, 3, 1, 1, 1)
        ldg_wzd.addPage(self.wizardPage)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.wizardPage2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tw_hld_prv = HoldersTableView(self.wizardPage2)
        self.tw_hld_prv.setObjectName(_fromUtf8("tw_hld_prv"))
        self.gridLayout_3.addWidget(self.tw_hld_prv, 4, 0, 1, 3)
        self.lnEdit_hld_path = QtGui.QLineEdit(self.wizardPage2)
        self.lnEdit_hld_path.setEnabled(True)
        self.lnEdit_hld_path.setObjectName(_fromUtf8("lnEdit_hld_path"))
        self.gridLayout_3.addWidget(self.lnEdit_hld_path, 2, 0, 1, 1)
        self.btn_brws_hld = QtGui.QPushButton(self.wizardPage2)
        self.btn_brws_hld.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/flts_open_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_brws_hld.setIcon(icon2)
        self.btn_brws_hld.setDefault(True)
        self.btn_brws_hld.setObjectName(_fromUtf8("btn_brws_hld"))
        self.gridLayout_3.addWidget(self.btn_brws_hld, 2, 1, 1, 1)
        self.vlNotification_holders = QtGui.QVBoxLayout()
        self.vlNotification_holders.setContentsMargins(-1, -1, -1, 10)
        self.vlNotification_holders.setObjectName(_fromUtf8("vlNotification_holders"))
        self.gridLayout_3.addLayout(self.vlNotification_holders, 0, 0, 1, 3)
        self.label_desc_2 = QtGui.QLabel(self.wizardPage2)
        self.label_desc_2.setObjectName(_fromUtf8("label_desc_2"))
        self.gridLayout_3.addWidget(self.label_desc_2, 1, 0, 1, 2)
        self.chk_holders_validate = QtGui.QCheckBox(self.wizardPage2)
        self.chk_holders_validate.setChecked(True)
        self.chk_holders_validate.setObjectName(_fromUtf8("chk_holders_validate"))
        self.gridLayout_3.addWidget(self.chk_holders_validate, 3, 0, 1, 1)
        self.btn_reload_holders = QtGui.QPushButton(self.wizardPage2)
        self.btn_reload_holders.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reload_holders.setIcon(icon3)
        self.btn_reload_holders.setObjectName(_fromUtf8("btn_reload_holders"))
        self.gridLayout_3.addWidget(self.btn_reload_holders, 2, 2, 1, 1)
        self.lbl_validation_description = QtGui.QLabel(self.wizardPage2)
        self.lbl_validation_description.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_validation_description.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lbl_validation_description.setFrameShadow(QtGui.QFrame.Plain)
        self.lbl_validation_description.setText(_fromUtf8(""))
        self.lbl_validation_description.setWordWrap(True)
        self.lbl_validation_description.setMargin(10)
        self.lbl_validation_description.setObjectName(_fromUtf8("lbl_validation_description"))
        self.gridLayout_3.addWidget(self.lbl_validation_description, 6, 0, 1, 3)
        self.label = QtGui.QLabel(self.wizardPage2)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 3)
        ldg_wzd.addPage(self.wizardPage2)
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
        self.label_desc.setText(_translate("ldg_wzd", "<html><head/><body><p>Enter scheme information below. Please note the scheme and SG numbers will be automatically generated</p></body></html>", None))
        self.label_region.setText(_translate("ldg_wzd", "<html><head/><body><p>Region <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_rel_auth_type.setText(_translate("ldg_wzd", "<html><head/><body><p>Type of Relevant Authority <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_rel_auth_name.setText(_translate("ldg_wzd", "<html><head/><body><p>Name of Relevant Authority <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_reg_div.setText(_translate("ldg_wzd", "<html><head/><body><p>Registration Division <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_schm_num.setText(_translate("ldg_wzd", "<html><head/><body><p>Scheme Number <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_landhold_num.setText(_translate("ldg_wzd", "<html><head/><body><p>Land Hold Plan Number <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.lnedit_landhold_num.setPlaceholderText(_translate("ldg_wzd", "Enter the Land Hold Plan number", None))
        self.label_sg_num.setText(_translate("ldg_wzd", "<html><head/><body><p>Surveyor General Number <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.lnedit_sg_num.setText(_translate("ldg_wzd", "SG ", None))
        self.lnedit_sg_num.setPlaceholderText(_translate("ldg_wzd", "Enter Surveyor General Number", None))
        self.label_schm_name.setText(_translate("ldg_wzd", "<html><head/><body><p>Scheme Name <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.lnedit_schm_nam.setPlaceholderText(_translate("ldg_wzd", "Enter name of the Scheme", None))
        self.label_date_apprv.setText(_translate("ldg_wzd", "<html><head/><body><p>Date of Approval (RA) <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_date_establish.setText(_translate("ldg_wzd", "<html><head/><body><p>Date of Establishment (RoD) <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_lro.setText(_translate("ldg_wzd", "<html><head/><body><p>Land Rights Office <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_title_deed_num.setText(_translate("ldg_wzd", "<html><head/><body><p>Title Deed Number <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.lnedit_title_deed_num.setText(_translate("ldg_wzd", "T", None))
        self.lnedit_title_deed_num.setPlaceholderText(_translate("ldg_wzd", "Enter Title Deed Number", None))
        self.label_constitution_ref_num.setText(_translate("ldg_wzd", "<html><head/><body><p>Constitution Ref. Number</p></body></html>", None))
        self.lnedit_constitution_ref_num.setPlaceholderText(_translate("ldg_wzd", "Enter Consitution Reference Number", None))
        self.label_scheme_description.setText(_translate("ldg_wzd", "<html><head/><body><p>Scheme Description <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.lnedit_scheme_description.setPlaceholderText(_translate("ldg_wzd", "Erf Number, Township Name", None))
        self.label_num_plots.setText(_translate("ldg_wzd", "<html><head/><body><p>Number of Plots <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.gbx_block_area.setTitle(_translate("ldg_wzd", "Block Area", None))
        self.label_blck_area_units.setText(_translate("ldg_wzd", "<html><head/><body><p>Units <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.radio_hectares.setText(_translate("ldg_wzd", "Hectares (Ha)", None))
        self.radio_sq_meters.setText(_translate("ldg_wzd", "Square Meters (Sq.m)", None))
        self.label_mandatory.setText(_translate("ldg_wzd", "<html><head/><body><p><span style=\" font-style:italic;\">(</span><span style=\" font-style:italic; color:#ff0000;\">*</span><span style=\" font-style:italic;\">) Mandatory field</span></p></body></html>", None))
        self.wizardPage.setSubTitle(_translate("ldg_wzd", "Upload the supporting documents for the scheme", None))
        self.label_desc_3.setText(_translate("ldg_wzd", "<html><head/><body><p>Click the \'Browse\' link to add the individual supporting documents </p></body></html>", None))
        self.label_upld_multi.setText(_translate("ldg_wzd", "Add multiple files from a source directory", None))
        self.btn_upload_dir.setText(_translate("ldg_wzd", "Upload From Directory...", None))
        self.lnEdit_hld_path.setPlaceholderText(_translate("ldg_wzd", "Path to the Holders Excel or CSV file...", None))
        self.btn_brws_hld.setToolTip(_translate("ldg_wzd", "Browse file", None))
        self.label_desc_2.setText(_translate("ldg_wzd", "Select the Excel or CSV file containing the holders information", None))
        self.chk_holders_validate.setText(_translate("ldg_wzd", "Perform validation upon loading data", None))
        self.btn_reload_holders.setToolTip(_translate("ldg_wzd", "Reload file", None))
        self.label.setText(_translate("ldg_wzd", "<html><head/><body><p><span style=\" font-weight:600;\">Validation Result</span></p></body></html>", None))
        self.label_desc_4.setText(_translate("ldg_wzd", "Confirm the scheme information.Click Back to edit the information or Finish to save.  ", None))

from stdm.ui.customcontrols.scheme_summary_widget import SchemeSummaryWidget
from stdm.ui.customcontrols.table_widget import HoldersTableView
from stdm.ui.customcontrols.documents_table_widget import DocumentTableWidget
from stdm import resources_rc
