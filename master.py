import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient

# MQTT settings
broker_address = "your_broker_address"
broker_port = 1883
topic = "sensor_data"

# Database setting-------

# MQTT settings
broker_address = "your_broker_address"
broker_port = 1883
topic = "sensor_data"

# MongoDB settings
mongo_host = "localhost"  # Replace with your MongoDB host
mongo_port = 27017  # Replace with your MongoDB port
mongo_db_name = "sensor_data_db"
mongo_collection_name = "sensor_data_collection"

# Connect to MongoDB
client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db_name]
collection = db[mongo_collection_name]

# Callback function to handle incoming sensor data




# Replace with your database configuration
# For example, if you're using MongoDB:
# from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017/')
# db = client['your_database_name']
# collection = db['sensor_data_collection']

# Callback function to handle incoming sensor data
def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode())
    # Store data in database
    # collection.insert_one(payload)
    print("Received:", payload)

def run_server():
    client = mqtt.Client()
    client.connect(broker_address, broker_port)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()

if __name__ == "__main__":
    run_server()
