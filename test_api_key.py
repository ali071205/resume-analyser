import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

print(f"Testing Key: {api_key}")

# 1. First, let's list available models to see what this key can actually access
print("\n--- Listing Available Models ---")
list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
try:
    list_response = requests.get(list_url)
    if list_response.status_code == 200:
        models = list_response.json().get('models', [])
        print(f"Found {len(models)} models.")
        for m in models:
            print(f" - {m['name']}")
    else:
        print(f"Failed to list models: {list_response.status_code}")
        print(list_response.text)
except Exception as e:
    print(f"Error listing models: {e}")

# 2. Now try a simple generation with a model that is likely to exist
print("\n--- Testing Generation ---")
# Try gemini-1.5-flash in v1 instead of v1beta
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
payload = {
    "contents": [{"parts": [{"text": "Hello"}]}]
}

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ SUCCESS! API key is working with v1/gemini-1.5-flash")
    else:
        print(f"❌ FAILED v1! Code: {response.status_code}")
        print("Details:", response.text)
except Exception as e:
    print(f"❌ Error during request: {e}")
