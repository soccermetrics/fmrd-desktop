# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/country_setup.ui'
#
# Created: Mon Aug  8 00:36:18 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CountrySetupDlg(object):
    def setupUi(self, CountrySetupDlg):
        CountrySetupDlg.setObjectName("CountrySetupDlg")
        CountrySetupDlg.resize(520, 192)
        CountrySetupDlg.setMinimumSize(QtCore.QSize(520, 192))
        CountrySetupDlg.setMaximumSize(QtCore.QSize(520, 192))
        self.layoutWidget = QtGui.QWidget(CountrySetupDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 130, 361, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.firstEntry = QtGui.QPushButton(self.layoutWidget)
        self.firstEntry.setMinimumSize(QtCore.QSize(71, 33))
        self.firstEntry.setMaximumSize(QtCore.QSize(71, 33))
        self.firstEntry.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstEntry.setIcon(icon)
        self.firstEntry.setObjectName("firstEntry")
        self.horizontalLayout_2.addWidget(self.firstEntry)
        self.prevEntry = QtGui.QPushButton(self.layoutWidget)
        self.prevEntry.setMinimumSize(QtCore.QSize(71, 33))
        self.prevEntry.setMaximumSize(QtCore.QSize(71, 33))
        self.prevEntry.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevEntry.setIcon(icon1)
        self.prevEntry.setObjectName("prevEntry")
        self.horizontalLayout_2.addWidget(self.prevEntry)
        self.nextEntry = QtGui.QPushButton(self.layoutWidget)
        self.nextEntry.setMinimumSize(QtCore.QSize(71, 33))
        self.nextEntry.setMaximumSize(QtCore.QSize(71, 33))
        self.nextEntry.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextEntry.setIcon(icon2)
        self.nextEntry.setObjectName("nextEntry")
        self.horizontalLayout_2.addWidget(self.nextEntry)
        self.lastEntry = QtGui.QPushButton(self.layoutWidget)
        self.lastEntry.setMinimumSize(QtCore.QSize(71, 33))
        self.lastEntry.setMaximumSize(QtCore.QSize(71, 33))
        self.lastEntry.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastEntry.setIcon(icon3)
        self.lastEntry.setObjectName("lastEntry")
        self.horizontalLayout_2.addWidget(self.lastEntry)
        self.line = QtGui.QFrame(CountrySetupDlg)
        self.line.setGeometry(QtCore.QRect(380, 10, 20, 171))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(CountrySetupDlg)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 391, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget1 = QtGui.QWidget(CountrySetupDlg)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 361, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setMinimumSize(QtCore.QSize(108, 27))
        self.label.setMaximumSize(QtCore.QSize(108, 27))
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.countryID_display = QtGui.QLineEdit(self.layoutWidget1)
        self.countryID_display.setMinimumSize(QtCore.QSize(81, 27))
        self.countryID_display.setMaximumSize(QtCore.QSize(81, 27))
        self.countryID_display.setStyleSheet("background-color: rgb(194, 190, 186);")
        self.countryID_display.setReadOnly(True)
        self.countryID_display.setObjectName("countryID_display")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.countryID_display)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setMinimumSize(QtCore.QSize(108, 27))
        self.label_2.setMaximumSize(QtCore.QSize(108, 27))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.countryEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.countryEdit.setMinimumSize(QtCore.QSize(231, 27))
        self.countryEdit.setMaximumSize(QtCore.QSize(231, 27))
        self.countryEdit.setObjectName("countryEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.countryEdit)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setMinimumSize(QtCore.QSize(108, 27))
        self.label_3.setMaximumSize(QtCore.QSize(108, 27))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.confedSelect = QtGui.QComboBox(self.layoutWidget1)
        self.confedSelect.setMinimumSize(QtCore.QSize(231, 27))
        self.confedSelect.setMaximumSize(QtCore.QSize(231, 27))
        self.confedSelect.setMaxCount(8)
        self.confedSelect.setObjectName("confedSelect")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.confedSelect)
        self.widget = QtGui.QWidget(CountrySetupDlg)
        self.widget.setGeometry(QtCore.QRect(410, 10, 111, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addEntry = QtGui.QPushButton(self.widget)
        self.addEntry.setMinimumSize(QtCore.QSize(85, 33))
        self.addEntry.setMaximumSize(QtCore.QSize(85, 33))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEntry.setIcon(icon4)
        self.addEntry.setObjectName("addEntry")
        self.verticalLayout.addWidget(self.addEntry)
        self.deleteEntry = QtGui.QPushButton(self.widget)
        self.deleteEntry.setMinimumSize(QtCore.QSize(85, 33))
        self.deleteEntry.setMaximumSize(QtCore.QSize(85, 33))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEntry.setIcon(icon5)
        self.deleteEntry.setObjectName("deleteEntry")
        self.verticalLayout.addWidget(self.deleteEntry)
        self.saveEntry = QtGui.QPushButton(self.widget)
        self.saveEntry.setMinimumSize(QtCore.QSize(85, 33))
        self.saveEntry.setMaximumSize(QtCore.QSize(85, 33))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveEntry.setIcon(icon6)
        self.saveEntry.setObjectName("saveEntry")
        self.verticalLayout.addWidget(self.saveEntry)
        spacerItem = QtGui.QSpacerItem(96, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setMinimumSize(QtCore.QSize(85, 33))
        self.closeButton.setMaximumSize(QtCore.QSize(85, 33))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon7)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)
        self.label.setBuddy(self.countryID_display)
        self.label_2.setBuddy(self.countryEdit)
        self.label_3.setBuddy(self.confedSelect)

        self.retranslateUi(CountrySetupDlg)
        QtCore.QMetaObject.connectSlotsByName(CountrySetupDlg)

    def retranslateUi(self, CountrySetupDlg):
        CountrySetupDlg.setWindowTitle(QtGui.QApplication.translate("CountrySetupDlg", "Country Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.firstEntry.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "First Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.prevEntry.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "Previous Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.nextEntry.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "Next Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.lastEntry.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "Last Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CountrySetupDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;ID</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CountrySetupDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">Cou&amp;ntry</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.countryEdit.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "Name of country", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CountrySetupDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Con&amp;federation</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.confedSelect.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "Country\'s confederation", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setText(QtGui.QApplication.translate("CountrySetupDlg", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setText(QtGui.QApplication.translate("CountrySetupDlg", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setText(QtGui.QApplication.translate("CountrySetupDlg", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setToolTip(QtGui.QApplication.translate("CountrySetupDlg", "Close Window", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("CountrySetupDlg", "&Close", None, QtGui.QApplication.UnicodeUTF8))

import fmrd_resources_rc
