import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import threading
import asyncio
import aiocoap.resource as resource
import aiocoap

 
MQTT_SERVER = "localhost"
MQTT_PATH1 = "new_publish"
MQTT_PATH2 = "subscribe_pub"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH1)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))
    print("Publishing: ")
    client.publish(MQTT_PATH2, (msg.payload))

#websocket server setup
def websock_thread():
    asyncio.set_event_loop(asyncio.new_event_loop())
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ("*** Websocket Server Started at %s***" % myIP)
    tornado.ioloop.IOLoop.instance().start()
    
#handler for websocket connection  
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new websocket connection')

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print ('websocket connection closed')

    def check_origin(self, origin):
        return True
# mqtt connection creation and callbacks definition    
def mqtt_thread():
    client.connect(MQTT_SERVER,1883, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

# Blocking connection for CoAP Server
class BlockResource(resource.Resource):
"""Resource which supports the GET and PUT methods. It sends large
    responses, which trigger blockwise transfer"""
    def set_content(self, content):
        self.content = content

    async def render_put(self, request):
        self.set_content(request.payload)
        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.content)
    
def CoAP_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    root = resource.Site()

    root.add_resource(('.well-known', 'core'),
            resource.WKCResource(root.get_resources_as_linkheader))

    root.add_resource(('other', 'block'), BlockResource())

    asyncio.Task(aiocoap.Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()
    
application = tornado.web.Application([
    (r'/ws', WSHandler),
])

if __name__ == "__main__":
    # threads for 3 protocols
    threads = []
    
    websock = threading.Thread(target=websock_thread)
    threads.append(websock)
    websock.daemon = True
    websock.start()
    
    client = mqtt.Client()
    mqtt_t = threading.Thread(target=mqtt_thread)
    threads.append(mqtt_t)
    mqtt_t.daemon = True
    mqtt_t.start()
    
    coap_t = threading.Thread(target=CoAP_thread)
    threads.append(coap_t)
    coap_t.daemon = True
    coap_t.start()
    
    while True:
        pass


 