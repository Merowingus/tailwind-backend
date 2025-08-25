from flask import Flask, request, jsonify

app = Flask(__name__)

# This is a simple GET endpoint to confirm the server is running.
@app.route('/')
def hello_world():
    return 'Welcome to Tailwind Backend1!'

# This is the new POST endpoint for your API.
@app.route('/api/v1/events', methods=['POST'])
def receive_event():
    # 1. Get the JSON data from the incoming request.
    data = request.json

    # 2. Check if data was actually sent.
    if not data:
        # Return an error message if the JSON is missing.
        return jsonify({"error": "Missing JSON data"}), 400

    # 3. Process the data (for now, we'll just print it).
    # In the next step, you will save this data to a database.
    try:
        driver_id = data.get('driverId')
        event_type = data.get('eventType')
        metadata = data.get('metadata')

        print(f"Received event from driver {driver_id}: {event_type}")
        print(f"Metadata: {metadata}")

        # 4. Return a success response.
        return jsonify({
            "status": "success",
            "message": "Event received successfully",
            "data": data
        }), 200
        
    except Exception as e:
        # Handle any errors during processing.
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Make sure to run the app in debug mode during development.
    app.run(debug=True)