import os
from dotenv import load_dotenv
import requests
import json

# Load .env (local) if present
load_dotenv()

endpoint = "https://api.betfair.com/exchange/betting/rest/v1.0/"

# Read credentials from environment (loaded from .env during development)
application_key = os.getenv("BETFAIR_APP_KEY", "")
authentication_token = os.getenv("BETFAIR_AUTH_TOKEN", "")

if not application_key or not authentication_token:
	raise RuntimeError("BETFAIR_APP_KEY and BETFAIR_AUTH_TOKEN must be set in the environment or .env file")

# Headers for Betfair API
headers = {
	"X-Application": application_key,
	"X-Authentication": authentication_token,
	"Content-Type": "application/json",
}

# Request body as a Python dict (requests will serialize when using json=...)
json_req = {"filter": {}}

url = endpoint + "listEventTypes/"

response = requests.post(url, json=json_req, headers=headers)

# Parse JSON response if possible
try:
	data = response.json()
except ValueError:
	data = {"text": response.text}

print(json.dumps(data, indent=3))