import requests
import json

# Replace the placeholder values with your own information
teams_webhook_url = "https://outlook.office.com/webhook/..."
channel_id = "19:...@thread.tacv2"
message = "Hello from Python!"

# Construct the HTTP request payload
payload = {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "summary": "Message from Python",
    "themeColor": "0076D7",
    "title": "Message from Python",
    "text": message,
    "potentialAction": [{
        "@type": "OpenUri",
        "name": "View Details",
        "targets": [{ "os": "default", "uri": teams_webhook_url }]
    }]
}

# Set the HTTP headers
headers = { "Content-Type": "application/json" }

# Send the HTTP request
response = requests.post(teams_webhook_url, headers=headers, data=json.dumps(payload))

# Check the HTTP response status code
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message: {response.text}")
