# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_str_editor.ui'
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

class Ui_STREditor(object):
    def setupUi(self, STREditor):
        STREditor.setObjectName(_fromUtf8("STREditor"))
        STREditor.resize(937, 554)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(STREditor.sizePolicy().hasHeightForWidth())
        STREditor.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QtGui.QVBoxLayout(STREditor)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.str_notification = QtGui.QVBoxLayout()
        self.str_notification.setObjectName(_fromUtf8("str_notification"))
        self.horizontalLayout.addLayout(self.str_notification)
        self.top_description = QtGui.QStackedWidget(STREditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_description.sizePolicy().hasHeightForWidth())
        self.top_description.setSizePolicy(sizePolicy)
        self.top_description.setObjectName(_fromUtf8("top_description"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.label_6 = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_15.addWidget(self.label_6)
        self.top_description.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_2 = QtGui.QLabel(self.page_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_10.addWidget(self.label_2)
        self.top_description.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_3 = QtGui.QLabel(self.page_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_11.addWidget(self.label_3)
        self.top_description.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_5 = QtGui.QLabel(self.page_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_13.addWidget(self.label_5)
        self.top_description.addWidget(self.page_4)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label = QtGui.QLabel(self.page_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_14.addWidget(self.label)
        self.top_description.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.page_6)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.label_10 = QtGui.QLabel(self.page_6)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_18.addWidget(self.label_10)
        self.top_description.addWidget(self.page_6)
        self.horizontalLayout.addWidget(self.top_description)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(STREditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(300, 300))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.str_tree_view_frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.str_tree_view_frame.sizePolicy().hasHeightForWidth())
        self.str_tree_view_frame.setSizePolicy(sizePolicy)
        self.str_tree_view_frame.setMinimumSize(QtCore.QSize(70, 100))
        self.str_tree_view_frame.setMaximumSize(QtCore.QSize(250, 500000))
        self.str_tree_view_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.str_tree_view_frame.setObjectName(_fromUtf8("str_tree_view_frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.str_tree_view_frame)
        self.verticalLayout.setMargin(1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, -1, 5)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.add_str_btn = QtGui.QToolButton(self.str_tree_view_frame)
        self.add_str_btn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_str_btn.setIcon(icon)
        self.add_str_btn.setObjectName(_fromUtf8("add_str_btn"))
        self.horizontalLayout_2.addWidget(self.add_str_btn)
        self.remove_str_btn = QtGui.QToolButton(self.str_tree_view_frame)
        self.remove_str_btn.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_str_btn.setIcon(icon1)
        self.remove_str_btn.setObjectName(_fromUtf8("remove_str_btn"))
        self.horizontalLayout_2.addWidget(self.remove_str_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtGui.QScrollArea(self.str_tree_view_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(50, 100))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.tree_view_container = QtGui.QWidget()
        self.tree_view_container.setGeometry(QtCore.QRect(0, 0, 220, 388))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_view_container.sizePolicy().hasHeightForWidth())
        self.tree_view_container.setSizePolicy(sizePolicy)
        self.tree_view_container.setMinimumSize(QtCore.QSize(220, 100))
        self.tree_view_container.setObjectName(_fromUtf8("tree_view_container"))
        self.scrollArea.setWidget(self.tree_view_container)
        self.verticalLayout.addWidget(self.scrollArea)
        self.component_container = QtGui.QStackedWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.component_container.sizePolicy().hasHeightForWidth())
        self.component_container.setSizePolicy(sizePolicy)
        self.component_container.setFrameShape(QtGui.QFrame.StyledPanel)
        self.component_container.setMidLineWidth(0)
        self.component_container.setObjectName(_fromUtf8("component_container"))
        self.componentPage1 = QtGui.QWidget()
        self.componentPage1.setObjectName(_fromUtf8("componentPage1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.componentPage1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.str_introduction = QtGui.QLabel(self.componentPage1)
        self.str_introduction.setWordWrap(True)
        self.str_introduction.setObjectName(_fromUtf8("str_introduction"))
        self.verticalLayout_2.addWidget(self.str_introduction)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.component_container.addWidget(self.componentPage1)
        self.componentPage2 = QtGui.QWidget()
        self.componentPage2.setObjectName(_fromUtf8("componentPage2"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.componentPage2)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.party_layout = QtGui.QVBoxLayout()
        self.party_layout.setSpacing(7)
        self.party_layout.setObjectName(_fromUtf8("party_layout"))
        self.verticalLayout_16.addLayout(self.party_layout)
        self.component_container.addWidget(self.componentPage2)
        self.componentPage3 = QtGui.QWidget()
        self.componentPage3.setObjectName(_fromUtf8("componentPage3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.componentPage3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.componentPage3)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.spatial_unit_tab = QtGui.QWidget()
        self.spatial_unit_tab.setObjectName(_fromUtf8("spatial_unit_tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.spatial_unit_tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.spatial_unit_box = QtGui.QWidget(self.spatial_unit_tab)
        self.spatial_unit_box.setObjectName(_fromUtf8("spatial_unit_box"))
        self.verticalLayout_4.addWidget(self.spatial_unit_box)
        self.tabWidget.addTab(self.spatial_unit_tab, _fromUtf8(""))
        self.mirror_map_tab = QtGui.QWidget()
        self.mirror_map_tab.setObjectName(_fromUtf8("mirror_map_tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.mirror_map_tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.mirror_map = SpatialPreview(self.mirror_map_tab)
        self.mirror_map.setObjectName(_fromUtf8("mirror_map"))
        self.verticalLayout_5.addWidget(self.mirror_map)
        self.tabWidget.addTab(self.mirror_map_tab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.component_container.addWidget(self.componentPage3)
        self.componentPage4 = QtGui.QWidget()
        self.componentPage4.setObjectName(_fromUtf8("componentPage4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.componentPage4)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.scrollArea_3 = QtGui.QScrollArea(self.componentPage4)
        self.scrollArea_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.str_type_widget = QtGui.QWidget()
        self.str_type_widget.setEnabled(True)
        self.str_type_widget.setGeometry(QtCore.QRect(0, 0, 671, 426))
        self.str_type_widget.setObjectName(_fromUtf8("str_type_widget"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.str_type_widget)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.str_type_box = QtGui.QVBoxLayout()
        self.str_type_box.setSpacing(0)
        self.str_type_box.setObjectName(_fromUtf8("str_type_box"))
        self.verticalLayout_12.addLayout(self.str_type_box)
        self.scrollArea_3.setWidget(self.str_type_widget)
        self.verticalLayout_8.addWidget(self.scrollArea_3)
        self.component_container.addWidget(self.componentPage4)
        self.componentPage5 = QtGui.QWidget()
        self.componentPage5.setObjectName(_fromUtf8("componentPage5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.componentPage5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.doc_type_cbo = QtGui.QComboBox(self.componentPage5)
        self.doc_type_cbo.setMinimumSize(QtCore.QSize(0, 30))
        self.doc_type_cbo.setMaximumSize(QtCore.QSize(16777215, 32))
        self.doc_type_cbo.setObjectName(_fromUtf8("doc_type_cbo"))
        self.gridLayout_6.addWidget(self.doc_type_cbo, 0, 1, 1, 1)
        self.add_documents_btn = QtGui.QPushButton(self.componentPage5)
        self.add_documents_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.add_documents_btn.setMaximumSize(QtCore.QSize(200, 32))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/document.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_documents_btn.setIcon(icon2)
        self.add_documents_btn.setObjectName(_fromUtf8("add_documents_btn"))
        self.gridLayout_6.addWidget(self.add_documents_btn, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.componentPage5)
        self.label_4.setMaximumSize(QtCore.QSize(100, 32))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_6)
        self.frame_3 = QtGui.QFrame(self.componentPage5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.supporting_doc_box = QtGui.QVBoxLayout()
        self.supporting_doc_box.setSpacing(0)
        self.supporting_doc_box.setObjectName(_fromUtf8("supporting_doc_box"))
        self.verticalLayout_6.addLayout(self.supporting_doc_box)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.component_container.addWidget(self.componentPage5)
        self.componentPage6 = QtGui.QWidget()
        self.componentPage6.setObjectName(_fromUtf8("componentPage6"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.componentPage6)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.componentPage6)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.number_of_year = QtGui.QSpinBox(self.componentPage6)
        self.number_of_year.setMaximum(200)
        self.number_of_year.setObjectName(_fromUtf8("number_of_year"))
        self.horizontalLayout_3.addWidget(self.number_of_year)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_17.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_8 = QtGui.QLabel(self.componentPage6)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.validity_from_date = QtGui.QDateEdit(self.componentPage6)
        self.validity_from_date.setCalendarPopup(True)
        self.validity_from_date.setObjectName(_fromUtf8("validity_from_date"))
        self.horizontalLayout_4.addWidget(self.validity_from_date)
        self.label_9 = QtGui.QLabel(self.componentPage6)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.validity_to_date = QtGui.QDateEdit(self.componentPage6)
        self.validity_to_date.setCalendarPopup(True)
        self.validity_to_date.setObjectName(_fromUtf8("validity_to_date"))
        self.horizontalLayout_4.addWidget(self.validity_to_date)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_17.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_17.addItem(spacerItem4)
        self.component_container.addWidget(self.componentPage6)
        self.verticalLayout_9.addWidget(self.splitter)
        self.buttonBox = QtGui.QDialogButtonBox(STREditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_9.addWidget(self.buttonBox)

        self.retranslateUi(STREditor)
        self.top_description.setCurrentIndex(5)
        self.component_container.setCurrentIndex(5)
        self.tabWidget.setCurrentIndex(0)
        self.mirror_map.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), STREditor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), STREditor.reject)
        QtCore.QMetaObject.connectSlotsByName(STREditor)

    def retranslateUi(self, STREditor):
        STREditor.setWindowTitle(_translate("STREditor", "Create Social Tenure Relationship", None))
        self.label_6.setText(_translate("STREditor", "The Social Tenure Relationship", None))
        self.label_2.setText(_translate("STREditor", "Select the party by searching through the existing record.", None))
        self.label_3.setText(_translate("STREditor", "Select the spatial unit that could be parcel, land or building, structure and so on.", None))
        self.label_5.setText(_translate("STREditor", "Select the type of relationship that the specified party has with the selected spatial unit.", None))
        self.label.setText(_translate("STREditor", "Upload one or more supporting documents under each document types (Optional).", None))
        self.label_10.setText(_translate("STREditor", "Specify the validity number of years or the validity dates.", None))
        self.add_str_btn.setToolTip(_translate("STREditor", "Add Social Tenure Relationship", None))
        self.remove_str_btn.setToolTip(_translate("STREditor", "Remove Social Tenure Relationship", None))
        self.str_introduction.setText(_translate("STREditor", "<html><head/><body><p>Social Tenure Relationship (STR) refers to the right or \'relationship\' between party and spatial unit (which is represented as polygons on the map). The two entities are related through a tenure right. </p><p>This module provides a mechanism to link the two entities with a tenure type and substanciated by supporting documents. </p><p>To begin, click on the \'Party\' item in the left side.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spatial_unit_tab), _translate("STREditor", "Add Spatial Unit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mirror_map_tab), _translate("STREditor", "Preview Spatial Unit", None))
        self.add_documents_btn.setText(_translate("STREditor", "Add Supporting Document", None))
        self.label_4.setText(_translate("STREditor", "Document Type", None))
        self.label_7.setText(_translate("STREditor", "Validity number of years", None))
        self.label_8.setText(_translate("STREditor", "Validity dates from", None))
        self.label_9.setText(_translate("STREditor", "to", None))

from stdm.ui.property_preview import SpatialPreview
from stdm import resources_rc
