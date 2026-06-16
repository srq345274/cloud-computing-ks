import paho.mqtt.client as mqtt
import json
import random
import time

BROKER = "192.168.44.128"
PORT = 31101
TOPIC = "sensor/temperature"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

print("开始发送温度数据...")

while True:
    data = {
        "temperature": round(random.uniform(20, 35), 2)
    }

    client.publish(TOPIC, json.dumps(data))

    print("发送:", data)

    time.sleep(5)
