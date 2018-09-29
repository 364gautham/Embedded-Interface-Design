This is the project that involves developing Graphical User Interface using PyQt5.

This project demonstrates **Weather Monitoring Service** Interface. DHT22 Temperature and Humidity
sensor is interfaced to RPI. User interface provides various options to control the 
operatins of the system. _Features_ like getting current Temperature and humidity of the system
along with the _time of request_ , sensor values are fetched in timely manner using timer 
and average of the values collected in shown on UI window, user has a feature to set an alrm
for temperature crossing a threshold value(_higher threshold_). User can also see the plot of the
values got in timely manner (upto 100 values and refreshed). System also saves the image of the plot.

** Installation Instructions**
This software is built using python3.
Install pyqt5 and pyqt5 tools.
1.sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
1.sudo apt-get install qttools5-dev-tools

Basic UI is generated using QTcreator: Command to get .py from .ui file: _pyuic5 file.ui> file.py  

Software needs importing certain python modules for successful operation:
For Sensor Readings : Adafruit_DHT module  [link!](https://github.com/adafruit/Adafruit_Python_DHT)
For Matplotlib :Matplotlib module and required dependencies.[link!](https://matplotlib.org/users/installing.html)

Code can be run using .py file : command is : python3 proj_ui.py

_Project Additions_:  

Basic requirements of getting temperature and humidity values with the time of request is done
Sensor connection state is also checked.

Additons:

1. Computes average of Temperature and Humidity on values got from timer
2. Plot of graph using values got using timer in runtime
3. Alarm Control Setting for user Slider 
4. User can view temperature in Celsius using Refresh button and in Fahrenheit using F Button
