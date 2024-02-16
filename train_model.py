from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from joblib import dump
import numpy as np

# MongoDB settings
mongo_host = "localhost"  # Replace with your MongoDB host
mongo_port = 27017  # Replace with your MongoDB port
mongo_db_name = "sensor_data_db"
mongo_collection_name = "sensor_data_collection"

# Connect to MongoDB
client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db_name]
collection = db[mongo_collection_name]

# Retrieve data from the database
cursor = collection.find()
data = []
for document in cursor:
    data.append(document)

# Preprocess the data (convert to numpy arrays)
X = np.array([[d['temperature'], d['humidity']] for d in data])
y = np.array([d['target_variable'] for d in data])  # Replace 'target_variable' with your target variable name

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train the machine learning model (example: linear regression)
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model's performance
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Save the trained model
dump(model, 'trained_model.joblib')

