# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_sensor.ui'
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
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 90, 211, 551))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(2)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.leManufacturer = QtGui.QLineEdit(self.frame_2)
        self.leManufacturer.setGeometry(QtCore.QRect(130, 170, 80, 21))
        self.leManufacturer.setText(_fromUtf8(""))
        self.leManufacturer.setReadOnly(True)
        self.leManufacturer.setObjectName(_fromUtf8("leManufacturer"))
        self.pbGoShipment = QtGui.QPushButton(self.frame_2)
        self.pbGoShipment.setGeometry(QtCore.QRect(90, 20, 121, 21))
        self.pbGoShipment.setObjectName(_fromUtf8("pbGoShipment"))
        self.lineEdit_9 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(1, 1, 90, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(1, 150, 130, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(1, 20, 90, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.leIdentifier = QtGui.QLineEdit(self.frame_2)
        self.leIdentifier.setGeometry(QtCore.QRect(130, 150, 80, 20))
        self.leIdentifier.setText(_fromUtf8(""))
        self.leIdentifier.setReadOnly(True)
        self.leIdentifier.setObjectName(_fromUtf8("leIdentifier"))
        self.lineEdit_7 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(1, 170, 130, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.leLocation = QtGui.QLineEdit(self.frame_2)
        self.leLocation.setGeometry(QtCore.QRect(90, 1, 120, 20))
        self.leLocation.setText(_fromUtf8(""))
        self.leLocation.setReadOnly(True)
        self.leLocation.setObjectName(_fromUtf8("leLocation"))
        self.listShipments = QtGui.QListWidget(self.frame_2)
        self.listShipments.setGeometry(QtCore.QRect(0, 40, 211, 91))
        self.listShipments.setObjectName(_fromUtf8("listShipments"))
        self.cbShape = QtGui.QComboBox(self.frame_2)
        self.cbShape.setGeometry(QtCore.QRect(130, 230, 81, 20))
        self.cbShape.setObjectName(_fromUtf8("cbShape"))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.lineEdit_10 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(1, 230, 130, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_5 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(1, 210, 130, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_11 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(1, 250, 130, 21))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.sbRotation = QtGui.QSpinBox(self.frame_2)
        self.sbRotation.setGeometry(QtCore.QRect(130, 250, 80, 21))
        self.sbRotation.setReadOnly(True)
        self.sbRotation.setMinimum(-1)
        self.sbRotation.setMaximum(5)
        self.sbRotation.setObjectName(_fromUtf8("sbRotation"))
        self.sbChannels = QtGui.QSpinBox(self.frame_2)
        self.sbChannels.setGeometry(QtCore.QRect(130, 270, 80, 21))
        self.sbChannels.setReadOnly(True)
        self.sbChannels.setMinimum(-1)
        self.sbChannels.setMaximum(2147483647)
        self.sbChannels.setObjectName(_fromUtf8("sbChannels"))
        self.lineEdit_6 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(1, 270, 130, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.leType = QtGui.QLineEdit(self.frame_2)
        self.leType.setGeometry(QtCore.QRect(130, 190, 80, 21))
        self.leType.setText(_fromUtf8(""))
        self.leType.setReadOnly(True)
        self.leType.setObjectName(_fromUtf8("leType"))
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(1, 190, 130, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pbAddComment = QtGui.QPushButton(self.frame_2)
        self.pbAddComment.setGeometry(QtCore.QRect(0, 530, 81, 21))
        self.pbAddComment.setObjectName(_fromUtf8("pbAddComment"))
        self.lineEdit_14 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(1, 310, 100, 21))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.pbDeleteComment = QtGui.QPushButton(self.frame_2)
        self.pbDeleteComment.setGeometry(QtCore.QRect(100, 310, 111, 21))
        self.pbDeleteComment.setObjectName(_fromUtf8("pbDeleteComment"))
        self.pteWriteComment = QtGui.QPlainTextEdit(self.frame_2)
        self.pteWriteComment.setGeometry(QtCore.QRect(1, 460, 209, 71))
        self.pteWriteComment.setObjectName(_fromUtf8("pteWriteComment"))
        self.listComments = QtGui.QListWidget(self.frame_2)
        self.listComments.setGeometry(QtCore.QRect(0, 330, 211, 121))
        self.listComments.setObjectName(_fromUtf8("listComments"))
        self.cbSize = QtGui.QComboBox(self.frame_2)
        self.cbSize.setGeometry(QtCore.QRect(130, 210, 81, 21))
        self.cbSize.setObjectName(_fromUtf8("cbSize"))
        self.cbSize.addItem(_fromUtf8(""))
        self.cbSize.addItem(_fromUtf8(""))
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 211, 71))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.pbSave = QtGui.QPushButton(self.frame_3)
        self.pbSave.setGeometry(QtCore.QRect(80, 30, 61, 21))
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.pbEdit = QtGui.QPushButton(self.frame_3)
        self.pbEdit.setGeometry(QtCore.QRect(0, 50, 71, 21))
        self.pbEdit.setObjectName(_fromUtf8("pbEdit"))
        self.pbCancel = QtGui.QPushButton(self.frame_3)
        self.pbCancel.setGeometry(QtCore.QRect(150, 30, 61, 21))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.lineEdit = QtGui.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(1, 1, 80, 19))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pbNew = QtGui.QPushButton(self.frame_3)
        self.pbNew.setGeometry(QtCore.QRect(0, 30, 71, 21))
        self.pbNew.setObjectName(_fromUtf8("pbNew"))
        self.sbSensorID = QtGui.QSpinBox(self.frame_3)
        self.sbSensorID.setGeometry(QtCore.QRect(80, 1, 130, 19))
        self.sbSensorID.setMaximum(2147483647)
        self.sbSensorID.setObjectName(_fromUtf8("sbSensorID"))
        self.pbGoStepSensor = QtGui.QPushButton(Form)
        self.pbGoStepSensor.setGeometry(QtCore.QRect(430, 150, 41, 21))
        self.pbGoStepSensor.setObjectName(_fromUtf8("pbGoStepSensor"))
        self.pbGoModule = QtGui.QPushButton(Form)
        self.pbGoModule.setGeometry(QtCore.QRect(430, 240, 41, 21))
        self.pbGoModule.setObjectName(_fromUtf8("pbGoModule"))
        self.sbProtomodule = QtGui.QSpinBox(Form)
        self.sbProtomodule.setGeometry(QtCore.QRect(350, 170, 81, 21))
        self.sbProtomodule.setReadOnly(True)
        self.sbProtomodule.setMinimum(-1)
        self.sbProtomodule.setMaximum(2147483647)
        self.sbProtomodule.setObjectName(_fromUtf8("sbProtomodule"))
        self.lineEdit_12 = QtGui.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(260, 170, 91, 21))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_8 = QtGui.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(260, 240, 91, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.sbModule = QtGui.QSpinBox(Form)
        self.sbModule.setGeometry(QtCore.QRect(350, 240, 81, 21))
        self.sbModule.setReadOnly(True)
        self.sbModule.setMinimum(-1)
        self.sbModule.setMaximum(2147483647)
        self.sbModule.setObjectName(_fromUtf8("sbModule"))
        self.lineEdit_13 = QtGui.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(260, 150, 91, 21))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.pbGoProtomodule = QtGui.QPushButton(Form)
        self.pbGoProtomodule.setGeometry(QtCore.QRect(430, 170, 41, 21))
        self.pbGoProtomodule.setObjectName(_fromUtf8("pbGoProtomodule"))
        self.sbStepSensor = QtGui.QSpinBox(Form)
        self.sbStepSensor.setGeometry(QtCore.QRect(350, 150, 81, 21))
        self.sbStepSensor.setReadOnly(True)
        self.sbStepSensor.setMinimum(-1)
        self.sbStepSensor.setMaximum(2147483647)
        self.sbStepSensor.setObjectName(_fromUtf8("sbStepSensor"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 220, 47, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 130, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 70, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_15 = QtGui.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(260, 90, 91, 21))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.cbInspection = QtGui.QComboBox(Form)
        self.cbInspection.setGeometry(QtCore.QRect(350, 90, 121, 21))
        self.cbInspection.setObjectName(_fromUtf8("cbInspection"))
        self.cbInspection.addItem(_fromUtf8(""))
        self.cbInspection.addItem(_fromUtf8(""))

        self.retranslateUi(Form)
        self.cbShape.setCurrentIndex(-1)
        self.cbSize.setCurrentIndex(-1)
        self.cbInspection.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pbGoShipment.setText(_translate("Form", "go to selected", None))
        self.lineEdit_9.setText(_translate("Form", "location", None))
        self.lineEdit_2.setText(_translate("Form", "Identifier", None))
        self.lineEdit_3.setText(_translate("Form", "shipments", None))
        self.lineEdit_7.setText(_translate("Form", "Manufacturer", None))
        self.listShipments.setToolTip(_translate("Form", "ID (date sent) (SENDER to RECEIVER)", None))
        self.cbShape.setItemText(0, _translate("Form", "full", None))
        self.cbShape.setItemText(1, _translate("Form", "half", None))
        self.cbShape.setItemText(2, _translate("Form", "five", None))
        self.cbShape.setItemText(3, _translate("Form", "three", None))
        self.cbShape.setItemText(4, _translate("Form", "semi", None))
        self.cbShape.setItemText(5, _translate("Form", "semi(-)", None))
        self.cbShape.setItemText(6, _translate("Form", "choptwo", None))
        self.lineEdit_10.setText(_translate("Form", "Shape", None))
        self.lineEdit_5.setText(_translate("Form", "Size (inches)", None))
        self.lineEdit_11.setText(_translate("Form", "Rotation", None))
        self.lineEdit_6.setText(_translate("Form", "Channels", None))
        self.lineEdit_4.setText(_translate("Form", "Type", None))
        self.pbAddComment.setText(_translate("Form", "add comment", None))
        self.lineEdit_14.setText(_translate("Form", "Comments", None))
        self.pbDeleteComment.setText(_translate("Form", "delete selected", None))
        self.cbSize.setItemText(0, _translate("Form", "8", None))
        self.cbSize.setItemText(1, _translate("Form", "6", None))
        self.pbSave.setText(_translate("Form", "Save", None))
        self.pbEdit.setText(_translate("Form", "Edit", None))
        self.pbCancel.setText(_translate("Form", "Cancel", None))
        self.lineEdit.setText(_translate("Form", "Sensor ID", None))
        self.pbNew.setText(_translate("Form", "New", None))
        self.pbGoStepSensor.setText(_translate("Form", "Go to", None))
        self.pbGoModule.setText(_translate("Form", "Go to", None))
        self.lineEdit_12.setText(_translate("Form", "On protomodule", None))
        self.lineEdit_8.setText(_translate("Form", "On module", None))
        self.lineEdit_13.setText(_translate("Form", "Placement step", None))
        self.pbGoProtomodule.setText(_translate("Form", "Go to", None))
        self.label.setText(_translate("Form", "module", None))
        self.label_2.setText(_translate("Form", "sensor placement", None))
        self.label_3.setText(_translate("Form", "sensor qualification", None))
        self.lineEdit_15.setText(_translate("Form", "visual inspection", None))
        self.cbInspection.setItemText(0, _translate("Form", "pass", None))
        self.cbInspection.setItemText(1, _translate("Form", "fail", None))

