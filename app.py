from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

# Your MongoDB Atlas connection string.
# It's a best practice to use an environment variable for this in production.
# For now, you can paste the full string here.
MONGO_URI = "mongodb+srv://worker81:test12345678@tailwind-backend-db.mzqwvbv.mongodb.net/?retryWrites=true&w=majority&appName=tailwind-backend-db"

# Initialize the Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.tailwind  # "tailwind" is the name of your database
events_collection = db.events  # "events" is the name of your collection

@app.route('/')
def hello_world():
    return 'Welcome to Tailwind Backend 2!'

@app.route('/api/v1/events', methods=['POST'])
def receive_event():
    data = request.json
    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    try:
        # Insert the received event data into the 'events' collection
        # MongoDB will automatically add a unique "_id" to each document
        events_collection.insert_one(data)

        print(f"Received and saved event from driver {data.get('driverId')}")

        return jsonify({
            "status": "success",
            "message": "Event received and stored successfully"
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)