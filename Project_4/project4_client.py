# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Execute Protocol test
#
#
# Authors: Kiran Hegde and Gautham KA
# Date: 12/09/2018
# EID Project4 Submission

# importing modules
from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT as sens
import sys
import time
import matplotlib.pyplot as plt
import sqlite3 as sq
import datetime
import json
import boto3
import matplotlib.dates as md
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import threading
from websocket import create_connection
from collections import OrderedDict
import asyncio
from aiocoap import *
import traceback

# global variables 
array_curT = []
array_minT = []
array_maxT = []
array_avgT = []
array_curH = []
array_minH = []
array_maxH = []
array_avgH = []
array_t = []
time_mqtt = []
time_web = []
time_coap = []
array_plot = []
time_dict = {}

unit = " degC"   
NUM_MSG = 30 
SERVER = "128.138.189.249"    #IP address of the server
MQTT_PATH1 = "new_publish"    #topic for MQTT publish
MQTT_PATH2 = "subscribe_pub"  #topic for MQTT subscribe

class Ui_MainWindow(object):
       
    def setupUi(self, MainWindow):
        
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
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(140, 60, 67, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(290, 60, 67, 21))
        self.label_2.setObjectName("label_2")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(270, 130, 111, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(140, 130, 111, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(270, 170, 111, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(140, 170, 111, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_11.setGeometry(QtCore.QRect(270, 210, 111, 31))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_12.setGeometry(QtCore.QRect(140, 210, 111, 31))
        self.textBrowser_12.setObjectName("textBrowser_12")
        
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(450, 240, 97, 21))
        self.label_10.setObjectName("label_10")
        
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_14.setGeometry(QtCore.QRect(450, 210, 191, 31))
        self.textBrowser_14.setObjectName("textBrowser_14")
        
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_16.setGeometry(QtCore.QRect(450, 170, 191, 31))
        self.textBrowser_16.setObjectName("textBrowser_16")
        
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_18.setGeometry(QtCore.QRect(450, 130, 191, 31))
        self.textBrowser_18.setObjectName("textBrowser_18")
        
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(450, 110, 97, 21))
        self.label_12.setObjectName("label_12")
        
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
        
        self.Plot = QtWidgets.QPushButton(MainWindow)
        self.Plot.setEnabled(True)
        self.Plot.setGeometry(QtCore.QRect(150,300,61,31))
        self.Plot.setObjectName("Plot")
        self.Plot.clicked.connect(self.button_clicked)
        
        self.Plot1 = QtWidgets.QPushButton(MainWindow)
        self.Plot1.setEnabled(True)
        self.Plot1.setGeometry(QtCore.QRect(300,300,61,31))
        self.Plot1.setObjectName("Plot")
        self.Plot1.clicked.connect(self.button_clicked1)

        self.Plot2 = QtWidgets.QPushButton(MainWindow)
        self.Plot2.setEnabled(True)
        self.Plot2.setGeometry(QtCore.QRect(450,300,191,31))
        self.Plot2.setObjectName("Plot")
        self.Plot2.clicked.connect(self.button_clicked2)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
              

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Temp"))
        self.label_2.setText(_translate("MainWindow", "Humidity"))
        self.label_4.setText(_translate("MainWindow", "Last"))
        self.label_5.setText(_translate("MainWindow", "Maximum"))
        self.label_6.setText(_translate("MainWindow", "Average"))
        self.label_7.setText(_translate("MainWindow", "Minimum"))
        self.label_12.setText(_translate("MainWindow", "Lowest Time"))
        self.label_10.setText(_translate("MainWindow", "Highest Time"))
        self.Plot.setText(_translate("Dialog", "Plot_F"))
        self.Plot1.setText(_translate("Dialog", "Plot_C"))
        self.Plot2.setText(_translate("Dialog", "Execute Protocol Test"))
        
    #This function fetches data from AWS and fills the list with proper values
    def myFunction(variable):
        global unit
        global NUM_MSG
        msg_len = 0
        response = {}
        response['Messages'] = []
        if variable == 1:
            unit = " degF"
        else:
            unit = " degC"
        #Authentication for AWS boto-client
        sqs = boto3.client('sqs', region_name = 'us-west-2',
                   aws_access_key_id='',
                   aws_secret_access_key='',
                   aws_session_token='')
        
        #get SQS Queue URL info
        url = sqs.get_queue_url(QueueName='project3_q.fifo')        
        try:
            #fetch maximum of 30 values 
            for k in range(0,3):
                response_once = sqs.receive_message(
                   QueueUrl =  url['QueueUrl'],
                   AttributeNames= [
                        'SentTimestamp'
                   ],
                   MaxNumberOfMessages = 10,
                   MessageAttributeNames=[
                        'All'
                   ],
                   VisibilityTimeout = 300,
                   WaitTimeSeconds = 0
                   )
                #check if proper data is received
                if 'Messages' in response_once:
                    entries = [
                        {'Id': msg['MessageId'], 'ReceiptHandle': msg['ReceiptHandle']}
                        for msg in response_once['Messages']
                        ]
        
                    resp = sqs.delete_message_batch(
                        QueueUrl=url['QueueUrl'], Entries=entries
                        )
                    msg_len += len(response_once['Messages'])
                    response['Messages'] += (response_once['Messages'])
           
            print("len of messages", len(response['Messages']))
                    
            #if no message is received, return false
            if not msg_len:
                return False
        
            if msg_len < NUM_MSG:
                NUM_MSG = msg_len
        
            array_plot.clear()
            
            #fill the list for plotting graphs
            for i in range(1, NUM_MSG+1):
                array_plot.append(i)
                
            #split the data from AWS response 
            for i in range (0,NUM_MSG):
                message = response['Messages'][i]
                
                #Spliting string and taking timestamp value
                body = response['Messages'][i]['Body']
                #print('\n The body content is %s' %body)
                x = body.split(",")
                array_t.append(x[0])
                
                #handle degC and degF calculation
                if(variable == 1):
                    a = ((9.0/5.0) * (float(x[1]))) + 32.0
                    array_curT.append(a)
                    b = ((9.0/5.0) * (float(x[2]))) + 32.0
                    array_minT.append(b) 
                    c = ((9.0/5.0) * (float(x[3]))) + 32.0
                    array_avgT.append(c)
                    d = ((9.0/5.0) * (float(x[4]))) + 32.0
                    array_maxT.append(d)
                elif (variable == 2):
                    a = float(x[1])
                    array_curT.append(a)
                    b = float(x[2])
                    array_minT.append(b) 
                    c = float(x[3])
                    array_avgT.append(c)
                    d = float(x[4])
                    array_maxT.append(d)
                
                #humidity data list
                array_curH.append(float(x[5]))
                array_minH.append(float(x[6]))
                array_avgH.append(float(x[7]))
                array_maxH.append(float(x[8]))
            return True
        except Exception:
                #print exception trace, if any
                traceback.print_exc()

    #plots the temperature info in degF along with humidity 
    def button_clicked(self):
        global NUM_MSG
        
        #clear all previous data 
        array_curT.clear()
        array_minT.clear()
        array_maxT.clear()
        array_avgT.clear()
        array_curH.clear()
        array_minH.clear()
        array_maxH.clear()
        array_avgH.clear()
        array_t.clear()
        _trans = QtCore.QCoreApplication.translate
        status = Ui_MainWindow.myFunction(1)
        
        #if no message is received, return
        if not status:
            print("No message\n")
            return
        self.textBrowser.setText(_trans("Dialog",str(array_curT[-1])))
        self.textBrowser_6.setText(_trans("Dialog",str(array_maxT[-1])))
        self.textBrowser_9.setText(_trans("Dialog",str(array_minT[-1])))
        self.textBrowser_12.setText(_trans("Dialog",str(array_avgT[-1])))
        self.textBrowser_8.setText(_trans("Dialog",str(array_minH[-1])))
        self.textBrowser_5.setText(_trans("Dialog",str(array_maxH[-1])))
        self.textBrowser_2.setText(_trans("Dialog",str(array_curH[-1])))
        self.textBrowser_11.setText(_trans("Dialog",str(array_avgH[-1])))
        
        #plot the temperature graph 
        fig = plt.figure()
        fig.suptitle("Messages Received: " + str(NUM_MSG) + "( Start Time:" +str(array_t[0]) +", END Time:"+ str(array_t[NUM_MSG-1]))
        ax = fig.add_subplot(311)
        p1 = ax.plot(array_plot,array_curT,'r-')
        p2 = ax.plot(array_plot,array_minT,'m-')
        p3 = ax.plot(array_plot,array_maxT,'k-')
        p4 = ax.plot(array_plot,array_avgT,'y-')
        #ax.xlabel('Time')
        #ax.ylabel('Temp(F)')
        ax.set_title('Temperature Variance')
        ax.grid()
        #ax.legend(loc = 'best')
        ax.legend((p1[0],p2[0],p3[0],p4[0]), ('Cur Temp','Min Temp','Avg Temp','Max Temp'))
        
        #plot humidity graph
        ax1 = fig.add_subplot(313)
        p1 = ax1.plot(array_plot,array_curH,'r-')
        p2 = ax1.plot(array_plot,array_minH,'m-')
        p3 = ax1.plot(array_plot,array_maxH,'k-')
        p4 = ax1.plot(array_plot,array_avgH,'y-')
        #ax1.xlabel('Time')
        #ax1.ylabel('Humidity(%)')
        ax1.set_title('Humidity Variance')
        ax1.grid()
        #ax1.legend(loc = 'best')
        ax1.legend((p1[0],p2[0],p3[0],p4[0]), ('Cur Hum','Min Hum','Avg Hum','Max Hum'))
        
        plt.show()
        
    #plots the temperature in degC along with humidity 
    def button_clicked1(self):
        global NUM_MSG
        #clear previos data 
        array_curT.clear()
        array_minT.clear()
        array_maxT.clear()
        array_avgT.clear()
        array_curH.clear()
        array_minH.clear()
        array_maxH.clear()
        array_avgH.clear()
        array_t.clear()
        _trans = QtCore.QCoreApplication.translate
        status = Ui_MainWindow.myFunction(2)
        if not status:
            print("No message\n")
            return
        self.textBrowser.setText(_trans("Dialog",str(array_curT[-1])))
        self.textBrowser_6.setText(_trans("Dialog",str(array_maxT[-1])))
        self.textBrowser_9.setText(_trans("Dialog",str(array_minT[-1])))
        self.textBrowser_12.setText(_trans("Dialog",str(array_avgT[-1])))
        self.textBrowser_8.setText(_trans("Dialog",str(array_minH[-1])))
        self.textBrowser_5.setText(_trans("Dialog",str(array_maxH[-1])))
        self.textBrowser_2.setText(_trans("Dialog",str(array_curH[-1])))
        self.textBrowser_11.setText(_trans("Dialog",str(array_avgH[-1])))
        
        #plot temperature graph
        fig = plt.figure()
        fig.suptitle("Messages Received: " + str(NUM_MSG) + "( Start Time:" +str(array_t[0]) +", END Time:"+ str(array_t[NUM_MSG-1]))
        ax = fig.add_subplot(311)
        p1 = ax.plot(array_plot,array_curT,'r-')
        p2 = ax.plot(array_plot,array_minT,'m-')
        p3 = ax.plot(array_plot,array_maxT,'k-')
        p4 = ax.plot(array_plot,array_avgT,'y-')
        #ax.xlabel('Time')
        #ax.ylabel('Temp(F)')
        ax.set_title('Temperature Variance')
        ax.grid()
        #ax.legend(loc = 'best')
        ax.legend((p1[0],p2[0],p3[0],p4[0]), ('Cur Temp','Min Temp','Avg Temp','Max Temp'))
        
        #plot humidity graph
        ax1 = fig.add_subplot(313)
        p1 = ax1.plot(array_plot,array_curH,'r-')
        p2 = ax1.plot(array_plot,array_minH,'m-')
        p3 = ax1.plot(array_plot,array_maxH,'k-')
        p4 = ax1.plot(array_plot,array_avgH,'y-')
        #ax1.xlabel('Time')
        #ax1.ylabel('Humidity(%)')
        ax1.set_title('Humidity Variance')
        ax1.grid()
        #ax1.legend(loc = 'best')
        ax1.legend((p1[0],p2[0],p3[0],p4[0]), ('Cur Hum','Min Hum','Avg Hum','Max Hum'))
        
        plt.show()
        
    #send data to server using CoAP
    async def coapPUT(self, data):
        context = await Context.create_client_context()
        request = Message(code=PUT, payload=bytes(data, 'utf-8'))
        request.opt.uri_host = SERVER
        request.opt.uri_path = ("other", "block")
        response = await context.request(request).response
        #print('Result: %s\n%r'%(response.code, response.payload))
        
    #execute protocol test and graph the timing results
    def button_clicked2(self):
        if not (len(array_t)):
            print("No data to test")
            return
        time_mqtt.clear()
        time_web.clear()
        time_coap.clear()
        final_mesg = ""
        
        #string to send to the
        for max_t,min_t,curr_t,avg_t,max_h,min_h,curr_h,avg_h in zip(array_maxT,\
                array_minT,array_curT, array_avgT, array_maxH,\
                array_minH, array_curH, array_avgH):
            print("\n\n")
            final_mesg +=   "Max Temp: {0:.2f}".format(max_t) + unit + "\n" + \
                                "Min Temp: {0:.2f}".format(min_t) + unit + "\n" + \
                                "Last Temp: {0:.2f}".format(curr_t) + unit + "\n" + \
                                "Avg Temp: {0:.2f}".format(avg_t) + unit + "\n" + \
                                "Max Hum: "+ str(max_h) + "%\n" + \
                                "Min Hum: "+ str(min_h) + "%\n" + \
                                "Last Hum: "+ str(curr_h) + "%\n" +\
                                "Avg Hum: "+ str(avg_h) + "%\n\n"
            
            #calculate timing for MQTT
            t1 = time.time()
            client.publish(MQTT_PATH1, final_mesg)
            data_sem.wait()
            t2 = time.time()
            time_taken = (t2 - t1)
            data_sem.clear()
            print("Time Taken for MQTT : %s seconds"%time_taken)
            time_mqtt.append(time_taken*1000)
        
            #calculate timing for websocket
            t1 = time.time()
            web_s.send(final_mesg)
            rec = web_s.recv()
            t2 = time.time()
            time_taken = (t2 - t1)
            print("Time Taken for WebServer : %s seconds"%time_taken)
            time_web.append(time_taken*1000)
            
            #calculate timing for CoAP
            t3 = time.time()
            asyncio.get_event_loop().run_until_complete(self.coapPUT(final_mesg))
            t4 = time.time()
            time_taken = (t4 - t3)
            print("Time Taken for CoAP : %s seconds"%time_taken)
            time_coap.append(time_taken*1000)
            final_mesg = ""
            
        time_dict["MQTT"] = sum(time_mqtt)
        time_dict["WebSock"] = sum(time_web)
        time_dict["CoAP"] = sum(time_coap)
        
        #sort the items according to timing result
        d_sorted_by_value = OrderedDict(sorted(time_dict.items(), key=lambda x: x[1]))
        key, value = d_sorted_by_value.popitem()
        _trans = QtCore.QCoreApplication.translate
        
        #display the resukt in QT display
        self.textBrowser_14.setText(_trans("Dialog", str(key)+": %04.04f ms"%(value)))
        key, value = d_sorted_by_value.popitem()
        self.textBrowser_16.setText(_trans("Dialog", str(key)+": %04.04f ms"%(value)))
        key, value = d_sorted_by_value.popitem()
        self.textBrowser_18.setText(_trans("Dialog", str(key)+": %04.04f ms"%(value)))
        
        #plot the timing graph
        fig = plt.figure()
        fig.suptitle("Number of Messages: %d "%len(array_t))
        p1 = plt.plot(array_plot, time_web,'r-')
        p2 = plt.plot(array_plot, time_mqtt,'m-')
        p3 = plt.plot(array_plot, time_coap,'b-')
        plt.xlabel("Message Number")
        plt.ylabel("Time(ms)")
        plt.grid()
        plt.legend((p1[0],p2[0], p3[0]), ('WebSock','MQTT', 'CoAP'))
        plt.show()
        

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH2)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data_sem.set()
    
#MQTT server function
def mqtt_server():
    client.connect(SERVER,1883, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
    


# Handler for CoAP protocol
def CoAPhandler(self):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(self.coapPUT(self.final_mesg))
    return 0

if __name__ == "__main__":
    import sys
    client = mqtt.Client()
    threads = []
    data_sem = threading.Event()
    
    #establish web server connection 
    web_s = create_connection("ws://" + SERVER + ":8888/ws")
    
    #launch MQTT thread
    mqtt_thread = threading.Thread(target=mqtt_server)
    threads.append(mqtt_thread)
    mqtt_thread.daemon = True
    mqtt_thread.start()
    
    #launch QT display
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

