# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_kapton_step.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1097, 705)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.sbID = QtGui.QSpinBox(Form)
        self.sbID.setGeometry(QtCore.QRect(90, 10, 71, 21))
        self.sbID.setObjectName(_fromUtf8("sbID"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 120, 111, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 140, 111, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 180, 91, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(440, 200, 91, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(440, 220, 91, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(440, 240, 91, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(440, 260, 91, 21))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.sbBaseplate1 = QtGui.QSpinBox(Form)
        self.sbBaseplate1.setGeometry(QtCore.QRect(180, 140, 71, 22))
        self.sbBaseplate1.setMinimum(-1)
        self.sbBaseplate1.setMaximum(2147483647)
        self.sbBaseplate1.setObjectName(_fromUtf8("sbBaseplate1"))
        self.pbGoBaseplate1 = QtGui.QPushButton(Form)
        self.pbGoBaseplate1.setGeometry(QtCore.QRect(250, 140, 51, 21))
        self.pbGoBaseplate1.setObjectName(_fromUtf8("pbGoBaseplate1"))
        self.pbGoBaseplate2 = QtGui.QPushButton(Form)
        self.pbGoBaseplate2.setGeometry(QtCore.QRect(250, 160, 51, 21))
        self.pbGoBaseplate2.setObjectName(_fromUtf8("pbGoBaseplate2"))
        self.sbBaseplate2 = QtGui.QSpinBox(Form)
        self.sbBaseplate2.setGeometry(QtCore.QRect(180, 160, 71, 22))
        self.sbBaseplate2.setMinimum(-1)
        self.sbBaseplate2.setMaximum(2147483647)
        self.sbBaseplate2.setObjectName(_fromUtf8("sbBaseplate2"))
        self.sbBaseplate3 = QtGui.QSpinBox(Form)
        self.sbBaseplate3.setGeometry(QtCore.QRect(180, 180, 71, 22))
        self.sbBaseplate3.setMinimum(-1)
        self.sbBaseplate3.setMaximum(2147483647)
        self.sbBaseplate3.setObjectName(_fromUtf8("sbBaseplate3"))
        self.pbGoBaseplate3 = QtGui.QPushButton(Form)
        self.pbGoBaseplate3.setGeometry(QtCore.QRect(250, 180, 51, 21))
        self.pbGoBaseplate3.setObjectName(_fromUtf8("pbGoBaseplate3"))
        self.pbGoBaseplate6 = QtGui.QPushButton(Form)
        self.pbGoBaseplate6.setGeometry(QtCore.QRect(250, 240, 51, 21))
        self.pbGoBaseplate6.setObjectName(_fromUtf8("pbGoBaseplate6"))
        self.pbGoBaseplate4 = QtGui.QPushButton(Form)
        self.pbGoBaseplate4.setGeometry(QtCore.QRect(250, 200, 51, 21))
        self.pbGoBaseplate4.setObjectName(_fromUtf8("pbGoBaseplate4"))
        self.sbBaseplate6 = QtGui.QSpinBox(Form)
        self.sbBaseplate6.setGeometry(QtCore.QRect(180, 240, 71, 21))
        self.sbBaseplate6.setMinimum(-1)
        self.sbBaseplate6.setMaximum(2147483647)
        self.sbBaseplate6.setObjectName(_fromUtf8("sbBaseplate6"))
        self.pbGoBaseplate5 = QtGui.QPushButton(Form)
        self.pbGoBaseplate5.setGeometry(QtCore.QRect(250, 220, 51, 21))
        self.pbGoBaseplate5.setObjectName(_fromUtf8("pbGoBaseplate5"))
        self.sbBaseplate4 = QtGui.QSpinBox(Form)
        self.sbBaseplate4.setGeometry(QtCore.QRect(180, 200, 71, 22))
        self.sbBaseplate4.setMinimum(-1)
        self.sbBaseplate4.setMaximum(2147483647)
        self.sbBaseplate4.setObjectName(_fromUtf8("sbBaseplate4"))
        self.sbBaseplate5 = QtGui.QSpinBox(Form)
        self.sbBaseplate5.setGeometry(QtCore.QRect(180, 220, 71, 21))
        self.sbBaseplate5.setMinimum(-1)
        self.sbBaseplate5.setMaximum(2147483647)
        self.sbBaseplate5.setObjectName(_fromUtf8("sbBaseplate5"))
        self.leUserPerformed = QtGui.QLineEdit(Form)
        self.leUserPerformed.setGeometry(QtCore.QRect(550, 120, 111, 20))
        self.leUserPerformed.setObjectName(_fromUtf8("leUserPerformed"))
        self.leCureDuration = QtGui.QLineEdit(Form)
        self.leCureDuration.setGeometry(QtCore.QRect(530, 220, 131, 20))
        self.leCureDuration.setReadOnly(True)
        self.leCureDuration.setObjectName(_fromUtf8("leCureDuration"))
        self.leCureTemperature = QtGui.QLineEdit(Form)
        self.leCureTemperature.setGeometry(QtCore.QRect(530, 240, 131, 20))
        self.leCureTemperature.setObjectName(_fromUtf8("leCureTemperature"))
        self.leCureHumidity = QtGui.QLineEdit(Form)
        self.leCureHumidity.setGeometry(QtCore.QRect(530, 260, 131, 21))
        self.leCureHumidity.setObjectName(_fromUtf8("leCureHumidity"))
        self.pbNew = QtGui.QPushButton(Form)
        self.pbNew.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.pbNew.setObjectName(_fromUtf8("pbNew"))
        self.pbEdit = QtGui.QPushButton(Form)
        self.pbEdit.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.pbEdit.setObjectName(_fromUtf8("pbEdit"))
        self.pbCancel = QtGui.QPushButton(Form)
        self.pbCancel.setGeometry(QtCore.QRect(170, 40, 71, 21))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.pbSave = QtGui.QPushButton(Form)
        self.pbSave.setGeometry(QtCore.QRect(90, 40, 71, 21))
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.lineEdit_11 = QtGui.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(10, 310, 131, 21))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(10, 120, 51, 20))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(70, 120, 101, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(180, 120, 121, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_15 = QtGui.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(10, 140, 51, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(Form)
        self.lineEdit_16.setGeometry(QtCore.QRect(10, 160, 51, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.lineEdit_17 = QtGui.QLineEdit(Form)
        self.lineEdit_17.setGeometry(QtCore.QRect(10, 180, 51, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_18 = QtGui.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(10, 200, 51, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_19 = QtGui.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(10, 220, 51, 20))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.lineEdit_20 = QtGui.QLineEdit(Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(10, 240, 51, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.sbTool5 = QtGui.QSpinBox(Form)
        self.sbTool5.setGeometry(QtCore.QRect(70, 220, 51, 22))
        self.sbTool5.setMinimum(-1)
        self.sbTool5.setMaximum(2147483647)
        self.sbTool5.setObjectName(_fromUtf8("sbTool5"))
        self.sbTool1 = QtGui.QSpinBox(Form)
        self.sbTool1.setGeometry(QtCore.QRect(70, 140, 51, 22))
        self.sbTool1.setMinimum(-1)
        self.sbTool1.setMaximum(2147483647)
        self.sbTool1.setObjectName(_fromUtf8("sbTool1"))
        self.sbTool3 = QtGui.QSpinBox(Form)
        self.sbTool3.setGeometry(QtCore.QRect(70, 180, 51, 22))
        self.sbTool3.setMinimum(-1)
        self.sbTool3.setMaximum(2147483647)
        self.sbTool3.setObjectName(_fromUtf8("sbTool3"))
        self.sbTool4 = QtGui.QSpinBox(Form)
        self.sbTool4.setGeometry(QtCore.QRect(70, 200, 51, 22))
        self.sbTool4.setMinimum(-1)
        self.sbTool4.setMaximum(2147483647)
        self.sbTool4.setObjectName(_fromUtf8("sbTool4"))
        self.sbTool2 = QtGui.QSpinBox(Form)
        self.sbTool2.setGeometry(QtCore.QRect(70, 160, 51, 22))
        self.sbTool2.setMinimum(-1)
        self.sbTool2.setMaximum(2147483647)
        self.sbTool2.setObjectName(_fromUtf8("sbTool2"))
        self.sbTool6 = QtGui.QSpinBox(Form)
        self.sbTool6.setGeometry(QtCore.QRect(70, 240, 51, 21))
        self.sbTool6.setMinimum(-1)
        self.sbTool6.setMaximum(2147483647)
        self.sbTool6.setObjectName(_fromUtf8("sbTool6"))
        self.sbBatchAraldite = QtGui.QSpinBox(Form)
        self.sbBatchAraldite.setGeometry(QtCore.QRect(140, 310, 71, 21))
        self.sbBatchAraldite.setMinimum(-1)
        self.sbBatchAraldite.setMaximum(999999)
        self.sbBatchAraldite.setObjectName(_fromUtf8("sbBatchAraldite"))
        self.dtCureStart = QtGui.QDateTimeEdit(Form)
        self.dtCureStart.setGeometry(QtCore.QRect(530, 180, 131, 21))
        self.dtCureStart.setObjectName(_fromUtf8("dtCureStart"))
        self.dtCureStop = QtGui.QDateTimeEdit(Form)
        self.dtCureStop.setGeometry(QtCore.QRect(530, 200, 131, 21))
        self.dtCureStop.setObjectName(_fromUtf8("dtCureStop"))
        self.dPerformed = QtGui.QDateEdit(Form)
        self.dPerformed.setGeometry(QtCore.QRect(550, 140, 111, 21))
        self.dPerformed.setObjectName(_fromUtf8("dPerformed"))
        self.pbGoTool5 = QtGui.QPushButton(Form)
        self.pbGoTool5.setGeometry(QtCore.QRect(120, 220, 51, 21))
        self.pbGoTool5.setObjectName(_fromUtf8("pbGoTool5"))
        self.pbGoTool4 = QtGui.QPushButton(Form)
        self.pbGoTool4.setGeometry(QtCore.QRect(120, 200, 51, 21))
        self.pbGoTool4.setObjectName(_fromUtf8("pbGoTool4"))
        self.pbGoTool1 = QtGui.QPushButton(Form)
        self.pbGoTool1.setGeometry(QtCore.QRect(120, 140, 51, 21))
        self.pbGoTool1.setObjectName(_fromUtf8("pbGoTool1"))
        self.pbGoTool2 = QtGui.QPushButton(Form)
        self.pbGoTool2.setGeometry(QtCore.QRect(120, 160, 51, 21))
        self.pbGoTool2.setObjectName(_fromUtf8("pbGoTool2"))
        self.pbGoTool6 = QtGui.QPushButton(Form)
        self.pbGoTool6.setGeometry(QtCore.QRect(120, 240, 51, 21))
        self.pbGoTool6.setObjectName(_fromUtf8("pbGoTool6"))
        self.pbGoTool3 = QtGui.QPushButton(Form)
        self.pbGoTool3.setGeometry(QtCore.QRect(120, 180, 51, 21))
        self.pbGoTool3.setObjectName(_fromUtf8("pbGoTool3"))
        self.lineEdit_21 = QtGui.QLineEdit(Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(10, 290, 131, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.lineEdit_22 = QtGui.QLineEdit(Form)
        self.lineEdit_22.setGeometry(QtCore.QRect(10, 270, 131, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.sbTrayAssembly = QtGui.QSpinBox(Form)
        self.sbTrayAssembly.setGeometry(QtCore.QRect(140, 290, 71, 21))
        self.sbTrayAssembly.setMinimum(-1)
        self.sbTrayAssembly.setMaximum(999999)
        self.sbTrayAssembly.setObjectName(_fromUtf8("sbTrayAssembly"))
        self.sbTrayComponent = QtGui.QSpinBox(Form)
        self.sbTrayComponent.setGeometry(QtCore.QRect(140, 270, 71, 21))
        self.sbTrayComponent.setMinimum(-1)
        self.sbTrayComponent.setMaximum(999999)
        self.sbTrayComponent.setObjectName(_fromUtf8("sbTrayComponent"))
        self.pbGoTrayAssembly = QtGui.QPushButton(Form)
        self.pbGoTrayAssembly.setGeometry(QtCore.QRect(210, 290, 51, 21))
        self.pbGoTrayAssembly.setObjectName(_fromUtf8("pbGoTrayAssembly"))
        self.pbGoTrayComponent = QtGui.QPushButton(Form)
        self.pbGoTrayComponent.setGeometry(QtCore.QRect(210, 270, 51, 21))
        self.pbGoTrayComponent.setObjectName(_fromUtf8("pbGoTrayComponent"))
        self.pbGoBatchAraldite = QtGui.QPushButton(Form)
        self.pbGoBatchAraldite.setGeometry(QtCore.QRect(210, 310, 51, 21))
        self.pbGoBatchAraldite.setObjectName(_fromUtf8("pbGoBatchAraldite"))
        self.pbDatePerformedNow = QtGui.QPushButton(Form)
        self.pbDatePerformedNow.setGeometry(QtCore.QRect(660, 140, 75, 21))
        self.pbDatePerformedNow.setObjectName(_fromUtf8("pbDatePerformedNow"))
        self.pbCureStartNow = QtGui.QPushButton(Form)
        self.pbCureStartNow.setGeometry(QtCore.QRect(660, 180, 75, 21))
        self.pbCureStartNow.setObjectName(_fromUtf8("pbCureStartNow"))
        self.pbCureStopNow = QtGui.QPushButton(Form)
        self.pbCureStopNow.setGeometry(QtCore.QRect(660, 200, 75, 21))
        self.pbCureStopNow.setObjectName(_fromUtf8("pbCureStopNow"))
        self.listIssues = QtGui.QListWidget(Form)
        self.listIssues.setGeometry(QtCore.QRect(10, 350, 721, 171))
        self.listIssues.setObjectName(_fromUtf8("listIssues"))
        self.lineEdit_23 = QtGui.QLineEdit(Form)
        self.lineEdit_23.setGeometry(QtCore.QRect(10, 520, 51, 20))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.leStatus = QtGui.QLineEdit(Form)
        self.leStatus.setGeometry(QtCore.QRect(60, 520, 171, 20))
        self.leStatus.setText(_fromUtf8(""))
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName(_fromUtf8("leStatus"))
        self.lineEdit_24 = QtGui.QLineEdit(Form)
        self.lineEdit_24.setGeometry(QtCore.QRect(310, 120, 91, 20))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.ckKaptonInspected1 = QtGui.QCheckBox(Form)
        self.ckKaptonInspected1.setGeometry(QtCore.QRect(310, 140, 70, 17))
        self.ckKaptonInspected1.setObjectName(_fromUtf8("ckKaptonInspected1"))
        self.ckKaptonInspected2 = QtGui.QCheckBox(Form)
        self.ckKaptonInspected2.setGeometry(QtCore.QRect(310, 160, 70, 17))
        self.ckKaptonInspected2.setObjectName(_fromUtf8("ckKaptonInspected2"))
        self.ckKaptonInspected4 = QtGui.QCheckBox(Form)
        self.ckKaptonInspected4.setGeometry(QtCore.QRect(310, 200, 70, 17))
        self.ckKaptonInspected4.setObjectName(_fromUtf8("ckKaptonInspected4"))
        self.ckKaptonInspected3 = QtGui.QCheckBox(Form)
        self.ckKaptonInspected3.setGeometry(QtCore.QRect(310, 180, 70, 17))
        self.ckKaptonInspected3.setObjectName(_fromUtf8("ckKaptonInspected3"))
        self.ckKaptonInspected5 = QtGui.QCheckBox(Form)
        self.ckKaptonInspected5.setGeometry(QtCore.QRect(310, 220, 70, 17))
        self.ckKaptonInspected5.setObjectName(_fromUtf8("ckKaptonInspected5"))
        self.ckKaptonInspected6 = QtGui.QCheckBox(Form)
        self.ckKaptonInspected6.setGeometry(QtCore.QRect(310, 240, 70, 17))
        self.ckKaptonInspected6.setObjectName(_fromUtf8("ckKaptonInspected6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lineEdit.setText(_translate("Form", "Kapton step ID", None))
        self.lineEdit_2.setText(_translate("Form", "who performed step", None))
        self.lineEdit_3.setText(_translate("Form", "date performed", None))
        self.lineEdit_5.setText(_translate("Form", "cure start", None))
        self.lineEdit_6.setText(_translate("Form", "cure stop", None))
        self.lineEdit_7.setText(_translate("Form", "cure duration", None))
        self.lineEdit_8.setText(_translate("Form", "cure temperature", None))
        self.lineEdit_9.setText(_translate("Form", "cure humidity", None))
        self.pbGoBaseplate1.setText(_translate("Form", "go to", None))
        self.pbGoBaseplate2.setText(_translate("Form", "go to", None))
        self.pbGoBaseplate3.setText(_translate("Form", "go to", None))
        self.pbGoBaseplate6.setText(_translate("Form", "go to", None))
        self.pbGoBaseplate4.setText(_translate("Form", "go to", None))
        self.pbGoBaseplate5.setText(_translate("Form", "go to", None))
        self.pbNew.setText(_translate("Form", "New", None))
        self.pbEdit.setText(_translate("Form", "Edit", None))
        self.pbCancel.setText(_translate("Form", "Cancel", None))
        self.pbSave.setText(_translate("Form", "Save", None))
        self.lineEdit_11.setText(_translate("Form", "araldite batch", None))
        self.lineEdit_12.setText(_translate("Form", "position", None))
        self.lineEdit_13.setText(_translate("Form", "sensor tool ID", None))
        self.lineEdit_14.setText(_translate("Form", "baseplate ID", None))
        self.lineEdit_15.setText(_translate("Form", "1", None))
        self.lineEdit_16.setText(_translate("Form", "2", None))
        self.lineEdit_17.setText(_translate("Form", "3", None))
        self.lineEdit_18.setText(_translate("Form", "4", None))
        self.lineEdit_19.setText(_translate("Form", "5", None))
        self.lineEdit_20.setText(_translate("Form", "6", None))
        self.pbGoTool5.setText(_translate("Form", "go to", None))
        self.pbGoTool4.setText(_translate("Form", "go to", None))
        self.pbGoTool1.setText(_translate("Form", "go to", None))
        self.pbGoTool2.setText(_translate("Form", "go to", None))
        self.pbGoTool6.setText(_translate("Form", "go to", None))
        self.pbGoTool3.setText(_translate("Form", "go to", None))
        self.lineEdit_21.setText(_translate("Form", "assembly tray", None))
        self.lineEdit_22.setText(_translate("Form", "component tray (sensor)", None))
        self.pbGoTrayAssembly.setText(_translate("Form", "go to", None))
        self.pbGoTrayComponent.setText(_translate("Form", "go to", None))
        self.pbGoBatchAraldite.setText(_translate("Form", "go to", None))
        self.pbDatePerformedNow.setText(_translate("Form", "set to today", None))
        self.pbCureStartNow.setText(_translate("Form", "set to now", None))
        self.pbCureStopNow.setText(_translate("Form", "set to now", None))
        self.listIssues.setToolTip(_translate("Form", "list of issues", None))
        self.lineEdit_23.setText(_translate("Form", "Status:", None))
        self.lineEdit_24.setText(_translate("Form", "kapton inspected", None))
        self.ckKaptonInspected1.setText(_translate("Form", "passed", None))
        self.ckKaptonInspected2.setText(_translate("Form", "passed", None))
        self.ckKaptonInspected4.setText(_translate("Form", "passed", None))
        self.ckKaptonInspected3.setText(_translate("Form", "passed", None))
        self.ckKaptonInspected5.setText(_translate("Form", "passed", None))
        self.ckKaptonInspected6.setText(_translate("Form", "passed", None))

