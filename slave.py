import time
import random
import json
import paho.mqtt.client as mqtt

# MQTT settings
broker_address = "your_broker_address"
broker_port = 1883
topic = "sensor_data"

# Simulate sensor data (replace this with actual sensor readings)
def read_sensor_data():
    temperature = random.uniform(20, 30)
    humidity = random.uniform(40, 60)
    return {"temperature": temperature, "humidity": humidity}

# Function to establish MQTT connection and publish sensor data
def publish_sensor_data():
    client = mqtt.Client()
    client.connect(broker_address, broker_port)

    while True:
        sensor_data = read_sensor_data()
        payload = json.dumps(sensor_data)
        client.publish(topic, payload)
        print("Published:", payload)
        time.sleep(5)  # Adjust the interval based on your requirements

    client.disconnect()

if __name__ == "__main__":
    publish_sensor_data()

