import json
import paho.mqtt.client as mqtt
import redis

# MQTT 配置
MQTT_BROKER = "192.168.44.128"
MQTT_PORT = 31101
TOPIC = "sensor/temperature"

# Redis 配置
REDIS_HOST = "10.43.126.12"
REDIS_PORT = 6379

# Redis 连接
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

# MQTT 回调函数
def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print("收到:", data)
    r.lpush("temperature_data", data)
    print("已写入 Redis")

# 创建 MQTT 客户端
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(TOPIC)

print("开始监听 MQTT...")
client.loop_forever()
