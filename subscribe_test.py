import paho.mqtt.subscribe as subscribe
from gpiozero import LED
from time import sleep

red = LED(17)

print("Subscribe MQTT script running!")

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    status = message.payload.decode()

    if status == "tænd":
        red.on()
    if status == "sluk":
        red.off()

subscribe.callback(on_message_print, "paho/test/topic", hostname="20.82.160.230", userdata={"message_count": 0})