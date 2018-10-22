# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT as sens
import sys
import time
import matplotlib.pyplot as plt
import sqlite3 as sq
import datetime


class Ui_MainWindow(object): 
    def setupUi(self, MainWindow):
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.time_cal)
        self.timer.setInterval(5000)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 496)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 90, 111, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(270, 90, 111, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(390, 90, 281, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_13.setGeometry(QtCore.QRect(140, 10, 241, 31))
        self.textBrowser_13.setObjectName("textBrowser_4")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(140, 60, 67, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(290, 60, 67, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(400, 60, 81, 21))
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(180, 60, 118, 26))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 60, 118, 26))
        self.radioButton_2.setObjectName("radioButton_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(390, 130, 281, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(270, 130, 111, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(140, 130, 111, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(390, 170, 281, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(270, 170, 111, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(140, 170, 111, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(390, 210, 281, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_11.setGeometry(QtCore.QRect(270, 210, 111, 31))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_12.setGeometry(QtCore.QRect(140, 210, 111, 31))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(50, 100, 41, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(50, 210, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(50, 180, 71, 20))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 649, 27))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer.start()

    def time_cal(self):
        _trans = QtCore.QCoreApplication.translate
        temp,humidity = sens.read(22,4)
        print("Temp Value ",temp)
        conn = sq.connect('project2.db')
        if temp==None:
            self.textBrowser_13.setText(_trans("Dialog", "Sensor Disconnected"))           
        else:
            self.textBrowser_13.setText(_trans("Dialog", "Sensor Connected"))
            temp = '{0:.2f}'.format(temp)
            temp_f = (float(temp) * (9/5.0)) + 32
            humid = '{0:.2f}'.format(humidity)
            conn.execute("INSERT INTO SENSOR_VAL (TEMP_C, TEMP_F, HUMID, TIMESTAMP) \
             VALUES ('"+str(temp)+"', '"+str(temp_f)+"', '"+str(humid)+"', '"+str(datetime.datetime.now())+"')")
            conn.commit()
            c = conn.cursor()
            if self.radioButton.isChecked() == True:
                #Min
                c.execute("SELECT * FROM SENSOR_VAL WHERE TEMP_C IS (SELECT MIN(TEMP_C) FROM SENSOR_VAL)")
                element=c.fetchone()
                self.textBrowser_9.setText(_trans("Dialog",str(element[0])))
                self.textBrowser_7.setText(_trans("Dialog",str(element[3])))
                #Max
                c.execute("SELECT * FROM SENSOR_VAL WHERE TEMP_C IS (SELECT MAX(TEMP_C) FROM SENSOR_VAL)")
                element=c.fetchone()
                self.textBrowser_6.setText(_trans("Dialog",str(element[0])))
                self.textBrowser_4.setText(_trans("Dialog",str(element[3])))
                #last
                c.execute("SELECT * FROM SENSOR_VAL ORDER BY TIMESTAMP DESC LIMIT 1")
                element=c.fetchone()
                self.textBrowser.setText(_trans("Dialog",str(element[0])))
                self.textBrowser_3.setText(_trans("Dialog",str(element[3])))                
                #Avg
                c.execute("SELECT AVG(TEMP_C) FROM SENSOR_VAL")
                element=c.fetchone()
                self.textBrowser_12.setText(_trans("Dialog",str(element[0])))
                self.textBrowser_10.setText(_trans("Dialog",str(datetime.datetime.now())))
            else:
                #Min
                c.execute("SELECT * FROM SENSOR_VAL WHERE TEMP_F IS (SELECT MIN(TEMP_F) FROM SENSOR_VAL)")
                element=c.fetchone()
                self.textBrowser_9.setText(_trans("Dialog",str(element[1])))
                self.textBrowser_7.setText(_trans("Dialog",str(element[3])))
                #Max
                c.execute("SELECT * FROM SENSOR_VAL WHERE TEMP_F IS (SELECT MAX(TEMP_F) FROM SENSOR_VAL)")
                element=c.fetchone()
                self.textBrowser_6.setText(_trans("Dialog",str(element[1])))
                self.textBrowser_4.setText(_trans("Dialog",str(element[3])))
                #last
                c.execute("SELECT * FROM SENSOR_VAL ORDER BY TIMESTAMP DESC LIMIT 1")
                element=c.fetchone()
                self.textBrowser.setText(_trans("Dialog",str(element[1])))
                self.textBrowser_3.setText(_trans("Dialog",str(element[3])))                
                #Avg
                c.execute("SELECT AVG(TEMP_F) FROM SENSOR_VAL")
                element=c.fetchone()
                self.textBrowser_12.setText(_trans("Dialog",str(element[0])))
                self.textBrowser_10.setText(_trans("Dialog",str(datetime.datetime.now())))
            #humid
            c.execute("SELECT * FROM SENSOR_VAL WHERE HUMID IS (SELECT MIN(HUMID) FROM SENSOR_VAL)")
            element=c.fetchone()
            self.textBrowser_8.setText(_trans("Dialog",str(element[2])))
            c.execute("SELECT * FROM SENSOR_VAL WHERE HUMID IS (SELECT MAX(HUMID) FROM SENSOR_VAL)")
            element=c.fetchone()
            self.textBrowser_5.setText(_trans("Dialog",str(element[2])))
            c.execute("SELECT * FROM SENSOR_VAL ORDER BY TIMESTAMP DESC LIMIT 1")
            element=c.fetchone()
            self.textBrowser_2.setText(_trans("Dialog",str(element[2])))
            c.execute("SELECT AVG(HUMID) FROM SENSOR_VAL")
            element=c.fetchone()
            self.textBrowser_11.setText(_trans("Dialog",str(element[0])))
   
            conn.close()    



            
            
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Temp"))
        self.label_2.setText(_translate("MainWindow", "Humidity"))
        self.label_3.setText(_translate("MainWindow", "Timestamp"))
        self.radioButton.setText(_translate("MainWindow", "C"))
        self.radioButton_2.setText(_translate("MainWindow", "F"))
        self.label_4.setText(_translate("MainWindow", "Last"))
        self.label_5.setText(_translate("MainWindow", "Maximum"))
        self.label_6.setText(_translate("MainWindow", "Average"))
        self.label_7.setText(_translate("MainWindow", "Minimum"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

