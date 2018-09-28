#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

import sys
import time
import datetime as dt
import Adafruit_DHT as sens
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_Dialog(QtWidgets.QWidget):
    avg_t,avg_h,count=[0,0,0]
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self,Dialog):
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.avg_value)
        self.timer.setInterval(5000)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        self.setAutoFillBackground(True)
        p=self.palette()
        p.setColor(self.backgroundRole(),Qt.green)
        self.setPalette(p)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans Narrow")
        Dialog.setFont(font)

        self.Refresh = QtWidgets.QPushButton(Dialog)
        self.Refresh.setEnabled(True)
        self.Refresh.setGeometry(QtCore.QRect(50, 70, 101, 31))
        self.Refresh.setObjectName("Refresh")

        self.Kelvin = QtWidgets.QPushButton(Dialog)
        self.Kelvin.setEnabled(True)
        self.Kelvin.setGeometry(QtCore.QRect(160, 70, 31, 31))
        self.Kelvin.setObjectName("Kelvin")

        self.Alarm = QtWidgets.QPushButton(Dialog)
        self.Alarm.setEnabled(True)
        self.Alarm.setGeometry(QtCore.QRect(260, 230, 101, 31))
        self.Alarm.setObjectName("Alarm")

        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 30, 191, 33))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(80, 10, 61, 21))
        self.label_1.setObjectName("label_1")

        self.hour_d = QtWidgets.QLCDNumber(Dialog)
        self.hour_d.setGeometry(QtCore.QRect(220, 32, 21, 31))
        self.hour_d.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hour_d.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hour_d.setSmallDecimalPoint(True)
        self.hour_d.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.hour_d.setDigitCount(2)
        self.hour_d.setObjectName("hour")

        self.min_d = QtWidgets.QLCDNumber(Dialog)
        self.min_d.setGeometry(QtCore.QRect(250, 32, 21, 31))
        self.min_d.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.min_d.setFrameShadow(QtWidgets.QFrame.Plain)
        self.min_d.setSmallDecimalPoint(True)
        self.min_d.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.min_d.setDigitCount(2)
        self.min_d.setObjectName("min")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(226, 10, 51, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 230, 71, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 230, 71, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 67, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 210, 67, 21))
        self.label_4.setObjectName("label_4")


        self.Slider_temp = QtWidgets.QSlider(Dialog)
        self.Slider_temp.setGeometry(QtCore.QRect(220, 160, 160, 26))
        self.Slider_temp.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_temp.setObjectName("Slider_temp")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(260, 141, 67, 31))
        self.label_5.setObjectName("label_5")
        self.Slider_Humid = QtWidgets.QSlider(Dialog)
        self.Slider_Humid.setGeometry(QtCore.QRect(220, 200, 160, 26))
        self.Slider_Humid.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Humid.setObjectName("Slider_Humid")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(260, 190, 67, 21))
        self.label_6.setObjectName("label_6")

        self.timer.start()

        self.Refresh.clicked.connect(self.get_temp)
        self.Kelvin.clicked.connect(self.get_temp_k)
        self.Alarm.clicked.connect(self.set_alarm)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Refresh.setText(_translate("Dialog", "Refresh"))
        self.label_1.setText(_translate("Dialog", "Value"))
        self.label_2.setText(_translate("Dialog", "Time"))
        self.Kelvin.setText(_translate("Dialog", "K"))
        self.label_3.setText(_translate("Dialog", "Avg -  T"))
        self.label_4.setText(_translate("Dialog", "Avg - H"))
        self.Alarm.setText(_translate("Dialog", "Set Alarm"))
        self.label_5.setText(_translate("Dialog", "Temp"))
        self.label_6.setText(_translate("Dialog", "Humidity"))

    def avg_value(self):
        _translate = QtCore.QCoreApplication.translate
        temp,humidity = sens.read_retry(22,4)
        if temp==None:
            self.lineEdit_2.setText(_translate("Dialog", "Sensor NC"))
            self.lineEdit_3.setText(_translate("Dialog", "Sensor NC"))
        else:
            self.count = self.count+1
            temp_s = '{0:.2f}'.format(temp)
            humid_s = '{0:.2f}'.format(humidity)
            self.avg_t = ((self.avg_t*(self.count-1)) + float(temp_s)) / self.count
            self.avg_h = ((self.avg_h*(self.count-1)) + float(humid_s)) / self.count
            avg_t = '{0:.2f}'.format(self.avg_t)
            avg_h = '{0:.2f}'.format(self.avg_h)
            self.lineEdit_2.setText(_translate("Dialog", str(avg_t)))
            self.lineEdit_3.setText(_translate("Dialog", str(avg_h)))


    def get_temp(self):
        _translate = QtCore.QCoreApplication.translate
        now=dt.datetime.now()
        self.hour_d.display(now.hour)
        self.min_d.display(now.minute)
        temp,humidity = sens.read_retry(22,4)
        print("Temp Value ",temp)
        if temp==None: 
            self.lineEdit_1.setText(_translate("Dialog", "Sensor Disconnected"))
        else:
            temp_s = '{0:.2f}'.format(temp)
            humid_s = '{0:.2f}'.format(humidity)
            print("Temp value",temp_s)
            print("Humidity  value",humid_s)
            self.lineEdit_1.setText(_translate("Dialog", temp_s) + ' ** ' + _translate("Dialog", humid_s))

    def get_temp_k(self):
        _translate = QtCore.QCoreApplication.translate
        now=dt.datetime.now()
        self.hour_d.display(now.hour)
        self.min_d.display(now.minute)
        temp,humidity = sens.read_retry(22,4)
        print("Temp Value ",temp)
        if temp==None:
            self.lineEdit_1.setText(_translate("Dialog", "Sensor Disconnected"))
        else:
            temp_s = '{0:.2f}'.format(temp)
            temp_s = (temp_s * 9/5.0) + 32
            humid_s = '{0:.2f}'.format(humidity)
            print("Temp value",temp_s)
            print("Humidity  value",humid_s)
            self.lineEdit_1.setText(_translate("Dialog", temp_s) + ' ** ' + _translate("Dialog", humid_s))

    def set_alarm(self):
        pass



if __name__=='__main__':

    app=QtWidgets.QApplication(sys.argv)
    ex=Ui_Dialog()
    ex.show()
    sys.exit(app.exec())
