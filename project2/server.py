import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import sqlite3 as sq
import datetime

'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
    
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
      
    def on_message(self, message):
        conn = sq.connect('project2.db')
        c = conn.cursor()
        print 'message received:  %s' % message
        # Reverse Message and send it back
        print 'sending back message: %s' % message[::-1]
        if message=="Min_tC":
            c.execute("SELECT * FROM SENSOR_VAL WHERE TEMP_C IS (SELECT MIN(TEMP_C) FROM SENSOR_VAL)")
            element=c.fetchone()
            send_var=(str(element[0]) + ',' + str(element[3]))
        elif message=="Min_tF":
            c.execute("SELECT * FROM SENSOR_VAL WHERE TEMP_F IS (SELECT MIN(TEMP_F) FROM SENSOR_VAL)")
            element=c.fetchone()
            send_var=(str(element[1]) + ',' + str(element[3]))
        elif message=="Max_tC":
            c.execute("SELECT * FROM SENSOR_VAL WHERE TEMP_C IS (SELECT MAX(TEMP_C) FROM SENSOR_VAL)")
            element=c.fetchone()
            send_var=(str(element[0]) + ',' + str(element[3]))
        elif message=="Max_tF":
            c.execute("SELECT * FROM SENSOR_VAL WHERE TEMP_F IS (SELECT MAX(TEMP_F) FROM SENSOR_VAL)")
            element=c.fetchone()
            send_var=(str(element[1]) + ',' + str(element[3]))
        elif message=="Avg_tC":
            c.execute("SELECT AVG(TEMP_C) FROM SENSOR_VAL")
            element=c.fetchone()
            send_var=(str(element[0]) + ',' + str(datetime.datetime.now()))
        elif message=="Avg_tF":
            c.execute("SELECT AVG(TEMP_F) FROM SENSOR_VAL")
            element=c.fetchone()
            send_var=(str(element[0]) + ',' + str(datetime.datetime.now()))
        elif message=="Last_tC":
            c.execute("SELECT * FROM SENSOR_VAL ORDER BY TIMESTAMP DESC LIMIT 1")
            element=c.fetchone()
            send_var=(str(element[0]) + ',' + str(element[3]))
        elif message=="Last_tF":
            c.execute("SELECT * FROM SENSOR_VAL ORDER BY TIMESTAMP DESC LIMIT 1")
            element=c.fetchone()
            send_var=(str(element[1]) + ',' + str(element[3]))
        elif message=="Min_h":
            c.execute("SELECT * FROM SENSOR_VAL WHERE HUMID IS (SELECT MIN(HUMID) FROM SENSOR_VAL)")
            element=c.fetchone()
            send_var=(str(element[2]) + ',' + str(element[3]))
        elif message=="Max_h":
            c.execute("SELECT * FROM SENSOR_VAL WHERE HUMID IS (SELECT MAX(HUMID) FROM SENSOR_VAL)")
            element=c.fetchone()
            send_var=(str(element[2]) + ',' + str(element[3]))
        elif message=="Avg_h":
            c.execute("SELECT AVG(HUMID) FROM SENSOR_VAL")
            element=c.fetchone()
            send_var=(str(element[0]) + ',' + str(datetime.datetime.now()))
        elif message=="Last_h":
            c.execute("SELECT * FROM SENSOR_VAL ORDER BY TIMESTAMP DESC LIMIT 1")
            element=c.fetchone()
            send_var=(str(element[2]) + ',' + str(element[3]))          
        self.write_message(send_var)
        conn.close()
 
    def on_close(self):
        print 'connection closed'
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print '*** Websocket Server Started at %s***' % myIP
    tornado.ioloop.IOLoop.instance().start()


