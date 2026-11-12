# Demo chạy thử về nhận và gửi tin nhắn giữa Python và Node-RED thông qua MQTT Broker

import time
import paho.mqtt.client as mqtt

# MQTT broker configuration
broker = "broker.hivemq.com"
port = 1883
topic_publish = "av01/python_to_node"
topic_subscribe = "av01/node_to_python"

# Callback function when connected to MQTT broker
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"\n[SYS] Connected to MQTT Broker ({broker}:{port})!")
        client.subscribe(topic_subscribe)
        print(
            "[SYS] Subscribed to topic:"
            f" '{topic_subscribe}'...\n")
    else:
        print(f"\n[ERR] Connection failed with code {reason_code}...\n")

# Callback function when a message is received from the subcribed topic
def on_message(client, userdata, msg):
    message_received = msg.payload.decode("utf-8")
    print(f"[SUBSCRIBE - Python Nhận] Từ Topic: '{msg.topic}'")
    print(f'"{message_received}"')
    print("Nhập tin nhắn gửi sang Node-RED (hoặc gõ 'exit' để thoát): ", end="")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print(f"[SYS] Connecting to MQTT Broker ({broker}:{port})...")
client.connect(broker, port, 60)

# Run Background thread to handle network events and callbacks
client.loop_start()
time.sleep(1)  # Wait for connection setup

try:
  while True:
    message_send = input(
        "Nhập tin nhắn gửi sang Node-RED (hoặc gõ 'exit' để thoát): "
    )
    if message_send.lower() == "exit":
      break
    if message_send.strip() != "":
      client.publish(topic_publish, message_send)
      print(
          f"[PUBLISH - Python Send] Subscribed to topic: '{topic_publish}'"
          f'"{message_send}"\n'
      )
except KeyboardInterrupt:
  pass

# Stop the MQTT client loop and disconnect
client.loop_stop()
client.disconnect()
print("\n[SYS] Disconnected from MQTT Broker. Exiting...")
        