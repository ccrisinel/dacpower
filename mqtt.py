import paho.mqtt.client as mqtt
from calcul import *
from dac import *
from relay import *
from time import sleep
import urllib.request
import os



def internet_off():
    try:
        urllib.request.urlopen('http://google.ch', timeout=1)
        return False
    except urllib.error.URLError as err: 
        return True

while internet_off():
	sleep(1)

relay_off()
switch = "off"
power = "11"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("stove/#")

    client.subscribe("wol")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global switch
    global power
    if msg.topic == "stove/switch/set":
        payload = msg.payload.decode()
        #print(power)
        if payload == "on":
            print("🔥")
            relay_on()
            switch = "on"
            client.publish("stove/switch/state",switch)
        if payload == "off" and power == b"2":
            print("💧")
            relay_off()
            switch = "off"
            client.publish("stove/switch/state",switch)

    if msg.topic == "stove/power/set":
        power=msg.payload
        power_cmd(power)
        client.publish("stove/power/state",str(power.decode()))
        print(power.decode())





client = mqtt.Client()
client.username_pw_set(username="username", password="password")

client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.29", 1883, 60)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
