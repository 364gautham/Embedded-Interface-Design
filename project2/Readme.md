**Raspberry Pi Socket Communication**

This project involves web socket interface for two Raspberry Pi's 

This project demonstrates **Weather Monitoring Service** Interface. DHT22 Temperature and Humidity
sensor is interfaced to RPI. User interface provides various options to control the 
operatins of the system. _Features_ like getting current Temperature and humidity of the system
along with the _time of request_. Readings like Last value. Max value, Minimum Value and Avergae value for temperaturre
and Humidity are updated every 5 seconds on Qt window. They are stored also using SQL database. client user can get
these stored values using web page interface. Webpage Interface also notifies user of Sensor connection status.


**Installation and Pre-requisites**

This software is built using python3
Tornado Server: https://os.mbed.com/cookbook/Websockets-Server
Client webpage uses HTML interface.

Install pyqt5 and pyqt5 tools.

_sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools_

_sudo apt-get install qttools5-dev-tools_

Basic UI is generated using QTcreator: Command to get .py from .ui file: _pyuic5 -x file.ui -o file.py_  

Software needs importing certain python modules for successful operation:
For Sensor Readings : Adafruit_DHT module : (https://github.com/adafruit/Adafruit_Python_DHT)


Code can be run using .py file : 

At server is : _python3 proj2_ui.py_ and _python server.py in two seperate terminals

At Client : open Client.html file in browser and connect to server ip and port

_Project Additions_:  

Login Screen in HTML


**References**:

1. https://www.w3schools.com/html/html_intro.asp

2. https://pythonspot.com/pyqt5/

3. https://www.w3schools.com/howto/howto_css_login_form.asp

4. http://www.sqlitetutorial.net/



