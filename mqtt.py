import paho.mqtt.client as mqtt
from calcul import *
from dac import *


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("stovekw")
    client.subscribe("stoveonoff")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(str(msg.payload))
    # print(msg.topic+" "+str(msg.payload))
    if msg.topic == "stovekw":
        power_cmd(msg.payload)
    if msg.topic == "stoveonoff":
        
        if int(msg.payload.decode()):
            print("🔥")
        else:
            print("💧")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
