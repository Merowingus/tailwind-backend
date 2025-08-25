import requests
import json

# The URL of your local Flask API endpoint
url = 'http://127.0.0.1:5000/api/v1/events'

# The JSON data payload to send
payload = {
    "driverId": "test_driver_001",
    "eventType": "match_detected",
    "metadata": {
        "jobId": "job_001",
        "pickup_location": "A",
        "dropoff_location": "B"
    }
}

# The headers to specify the content type is JSON
headers = {
    "Content-Type": "application/json"
}

print("Attempting to send POST request...")
try:
    # Send the POST request
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Print the response details
    print(f"Request sent. Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")

except requests.exceptions.ConnectionError as e:
    print(f"Error: Could not connect to the server. Is your Flask app running? {e}")

except json.JSONDecodeError:
    print("Error: The response body is not valid JSON.")
    print(f"Raw Response Body: {response.text}")