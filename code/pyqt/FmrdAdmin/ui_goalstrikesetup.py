# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/goalstrike_setup.ui'
#
# Created: Mon Aug  8 00:36:21 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_GoalStrikeSetupDlg(object):
    def setupUi(self, GoalStrikeSetupDlg):
        GoalStrikeSetupDlg.setObjectName("GoalStrikeSetupDlg")
        GoalStrikeSetupDlg.resize(620, 140)
        GoalStrikeSetupDlg.setMinimumSize(QtCore.QSize(620, 140))
        GoalStrikeSetupDlg.setMaximumSize(QtCore.QSize(620, 140))
        self.layoutWidget = QtGui.QWidget(GoalStrikeSetupDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 20, 601, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.goalstrikeID_display = QtGui.QLineEdit(self.layoutWidget)
        self.goalstrikeID_display.setMaximumSize(QtCore.QSize(81, 27))
        self.goalstrikeID_display.setStyleSheet("background-color: rgb(194, 190, 186);")
        self.goalstrikeID_display.setReadOnly(True)
        self.goalstrikeID_display.setObjectName("goalstrikeID_display")
        self.horizontalLayout.addWidget(self.goalstrikeID_display)
        spacerItem = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.goalstrikeEdit = QtGui.QLineEdit(self.layoutWidget)
        self.goalstrikeEdit.setMinimumSize(QtCore.QSize(271, 27))
        self.goalstrikeEdit.setObjectName("goalstrikeEdit")
        self.horizontalLayout.addWidget(self.goalstrikeEdit)
        self.layoutWidget_2 = QtGui.QWidget(GoalStrikeSetupDlg)
        self.layoutWidget_2.setGeometry(QtCore.QRect(201, 70, 411, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.addEntry = QtGui.QPushButton(self.layoutWidget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEntry.setIcon(icon)
        self.addEntry.setObjectName("addEntry")
        self.horizontalLayout_3.addWidget(self.addEntry)
        self.saveEntry = QtGui.QPushButton(self.layoutWidget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveEntry.setIcon(icon1)
        self.saveEntry.setObjectName("saveEntry")
        self.horizontalLayout_3.addWidget(self.saveEntry)
        self.deleteEntry = QtGui.QPushButton(self.layoutWidget_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEntry.setIcon(icon2)
        self.deleteEntry.setObjectName("deleteEntry")
        self.horizontalLayout_3.addWidget(self.deleteEntry)
        self.closeButton = QtGui.QPushButton(self.layoutWidget_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.layoutWidget_3 = QtGui.QWidget(GoalStrikeSetupDlg)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 70, 191, 51))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.firstEntry = QtGui.QPushButton(self.layoutWidget_3)
        self.firstEntry.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstEntry.setIcon(icon4)
        self.firstEntry.setObjectName("firstEntry")
        self.horizontalLayout_2.addWidget(self.firstEntry)
        self.prevEntry = QtGui.QPushButton(self.layoutWidget_3)
        self.prevEntry.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevEntry.setIcon(icon5)
        self.prevEntry.setObjectName("prevEntry")
        self.horizontalLayout_2.addWidget(self.prevEntry)
        self.nextEntry = QtGui.QPushButton(self.layoutWidget_3)
        self.nextEntry.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextEntry.setIcon(icon6)
        self.nextEntry.setObjectName("nextEntry")
        self.horizontalLayout_2.addWidget(self.nextEntry)
        self.lastEntry = QtGui.QPushButton(self.layoutWidget_3)
        self.lastEntry.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastEntry.setIcon(icon7)
        self.lastEntry.setObjectName("lastEntry")
        self.horizontalLayout_2.addWidget(self.lastEntry)
        spacerItem3 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label.setBuddy(self.goalstrikeID_display)
        self.label_2.setBuddy(self.goalstrikeEdit)

        self.retranslateUi(GoalStrikeSetupDlg)
        QtCore.QMetaObject.connectSlotsByName(GoalStrikeSetupDlg)

    def retranslateUi(self, GoalStrikeSetupDlg):
        GoalStrikeSetupDlg.setWindowTitle(QtGui.QApplication.translate("GoalStrikeSetupDlg", "Goal Strikes Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GoalStrikeSetupDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;ID</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GoalStrikeSetupDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;Goal Strikes</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.goalstrikeEdit.setToolTip(QtGui.QApplication.translate("GoalStrikeSetupDlg", "Body part used to score goal", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setToolTip(QtGui.QApplication.translate("GoalStrikeSetupDlg", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setText(QtGui.QApplication.translate("GoalStrikeSetupDlg", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setToolTip(QtGui.QApplication.translate("GoalStrikeSetupDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setText(QtGui.QApplication.translate("GoalStrikeSetupDlg", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setToolTip(QtGui.QApplication.translate("GoalStrikeSetupDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setText(QtGui.QApplication.translate("GoalStrikeSetupDlg", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setToolTip(QtGui.QApplication.translate("GoalStrikeSetupDlg", "Close Window", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("GoalStrikeSetupDlg", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.firstEntry.setToolTip(QtGui.QApplication.translate("GoalStrikeSetupDlg", "First Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.prevEntry.setToolTip(QtGui.QApplication.translate("GoalStrikeSetupDlg", "Previous Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.nextEntry.setToolTip(QtGui.QApplication.translate("GoalStrikeSetupDlg", "Next Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.lastEntry.setToolTip(QtGui.QApplication.translate("GoalStrikeSetupDlg", "Last Entry", None, QtGui.QApplication.UnicodeUTF8))

import fmrd_resources_rc
