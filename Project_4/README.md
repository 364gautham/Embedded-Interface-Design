# ECEN5053-002 Embedded Interface Design
# Project 4
* IOT Protocols Timing Performance comparision- AWS SQS and PYQT UI

### Kiran Hegde and Gautham KA

## Installation Instructions 
* Clone this github repository
* Uses sqlite3 as the database
* Uses boto3 AWS Python SDK , can be installed by running `pip3 install boto3`
* Uses matplotlib for plotting graphs , can be installed by running `pip3 install matplotlib`
* Uses paho-MQTT - `pip3 install paho-mqtt` 
* Uses aioCoAP- `pip3 install aiocoap`
* Uses Websocket- `pip3 install websocket websocket-client`
 

### Run Instructions
* run `python3 basicPubSub.py` to start the data publish to AWS
* run `python3 project4_client.py` to start the remote pi QT interface showing the graph of data retrived from SQS queue
* run `python3 server_proj4.py` to start server for protocol interactions - Timing Performance Calculation
* run `python3 proj2_ui.py` to start UI for Sensor Timely readings - fetched from Database 
* run MQTT Publish Broker - mosquitto_sub -h localhost -v -t new_publish
* run MQTT subscribing Broker - mosquitto_sub -h localhost -v -t subscribe_pub


### Files in the directory
* basicPubSub.py reads data from the temperature sensor and publishes to AWS 
* database.py - database operations
* lambda_function.js - AWS lambda code for getting data from 
* project4_client.py - remote pi QT UI that gets data from SQS queue and plots graph 
* proj2_ui.py - Provides server side QT display and sensor data sending to AWS
* server_proj4.py - Provvides Connections For MQTT,COAP and Websocket Server Connection
* project2.db - SQL Database file-[ Table - SENSOR_VAL]



## References
* https://www.eclipse.org/paho/clients/python/
* https://aiocoap.readthedocs.io/en/latest/examples.html
* https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html
* https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-example-sending-receiving-msgs.html
* https://github.com/eclipse/paho.mqtt.python
* Class Slides



