# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/card_setup.ui'
#
# Created: Thu Dec 29 23:31:15 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CardSetupDlg(object):
    def setupUi(self, CardSetupDlg):
        CardSetupDlg.setObjectName("CardSetupDlg")
        CardSetupDlg.resize(600, 140)
        CardSetupDlg.setMinimumSize(QtCore.QSize(600, 140))
        CardSetupDlg.setMaximumSize(QtCore.QSize(600, 140))
        self.layoutWidget = QtGui.QWidget(CardSetupDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 20, 581, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cardID_display = QtGui.QLineEdit(self.layoutWidget)
        self.cardID_display.setMaximumSize(QtCore.QSize(81, 27))
        self.cardID_display.setStyleSheet("background-color: rgb(194, 190, 186);")
        self.cardID_display.setReadOnly(True)
        self.cardID_display.setObjectName("cardID_display")
        self.horizontalLayout.addWidget(self.cardID_display)
        spacerItem = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cardtypeEdit = QtGui.QLineEdit(self.layoutWidget)
        self.cardtypeEdit.setMinimumSize(QtCore.QSize(271, 27))
        self.cardtypeEdit.setObjectName("cardtypeEdit")
        self.horizontalLayout.addWidget(self.cardtypeEdit)
        self.layoutWidget1 = QtGui.QWidget(CardSetupDlg)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 201, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.firstEntry = QtGui.QPushButton(self.layoutWidget1)
        self.firstEntry.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstEntry.setIcon(icon)
        self.firstEntry.setObjectName("firstEntry")
        self.horizontalLayout_2.addWidget(self.firstEntry)
        self.prevEntry = QtGui.QPushButton(self.layoutWidget1)
        self.prevEntry.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevEntry.setIcon(icon1)
        self.prevEntry.setObjectName("prevEntry")
        self.horizontalLayout_2.addWidget(self.prevEntry)
        self.nextEntry = QtGui.QPushButton(self.layoutWidget1)
        self.nextEntry.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextEntry.setIcon(icon2)
        self.nextEntry.setObjectName("nextEntry")
        self.horizontalLayout_2.addWidget(self.nextEntry)
        self.lastEntry = QtGui.QPushButton(self.layoutWidget1)
        self.lastEntry.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastEntry.setIcon(icon3)
        self.lastEntry.setObjectName("lastEntry")
        self.horizontalLayout_2.addWidget(self.lastEntry)
        spacerItem1 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.layoutWidget2 = QtGui.QWidget(CardSetupDlg)
        self.layoutWidget2.setGeometry(QtCore.QRect(210, 70, 381, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.addEntry = QtGui.QPushButton(self.layoutWidget2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEntry.setIcon(icon4)
        self.addEntry.setObjectName("addEntry")
        self.horizontalLayout_3.addWidget(self.addEntry)
        self.saveEntry = QtGui.QPushButton(self.layoutWidget2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveEntry.setIcon(icon5)
        self.saveEntry.setObjectName("saveEntry")
        self.horizontalLayout_3.addWidget(self.saveEntry)
        self.deleteEntry = QtGui.QPushButton(self.layoutWidget2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEntry.setIcon(icon6)
        self.deleteEntry.setObjectName("deleteEntry")
        self.horizontalLayout_3.addWidget(self.deleteEntry)
        self.closeButton = QtGui.QPushButton(self.layoutWidget2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon7)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.label.setBuddy(self.cardID_display)
        self.label_2.setBuddy(self.cardtypeEdit)

        self.retranslateUi(CardSetupDlg)
        QtCore.QMetaObject.connectSlotsByName(CardSetupDlg)

    def retranslateUi(self, CardSetupDlg):
        CardSetupDlg.setWindowTitle(QtGui.QApplication.translate("CardSetupDlg", "Disciplinary Card Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CardSetupDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;ID</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CardSetupDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ca&amp;rd Description</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cardtypeEdit.setToolTip(QtGui.QApplication.translate("CardSetupDlg", "Caution card type", None, QtGui.QApplication.UnicodeUTF8))
        self.firstEntry.setToolTip(QtGui.QApplication.translate("CardSetupDlg", "First Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.prevEntry.setToolTip(QtGui.QApplication.translate("CardSetupDlg", "Previous Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.nextEntry.setToolTip(QtGui.QApplication.translate("CardSetupDlg", "Next Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.lastEntry.setToolTip(QtGui.QApplication.translate("CardSetupDlg", "Last Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setToolTip(QtGui.QApplication.translate("CardSetupDlg", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setText(QtGui.QApplication.translate("CardSetupDlg", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setToolTip(QtGui.QApplication.translate("CardSetupDlg", "Save Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setText(QtGui.QApplication.translate("CardSetupDlg", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setToolTip(QtGui.QApplication.translate("CardSetupDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setText(QtGui.QApplication.translate("CardSetupDlg", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setToolTip(QtGui.QApplication.translate("CardSetupDlg", "Close Window", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("CardSetupDlg", "&Close", None, QtGui.QApplication.UnicodeUTF8))

import fmrd_resources_rc
