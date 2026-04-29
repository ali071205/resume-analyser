"""Test newer Gemini models."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from google import genai

client = genai.Client(api_key="AIzaSyB3GVXDf14Tz-NLcwiDPfi4Kj-MXalONKE")

models_to_try = [
    "models/gemini-2.5-flash-lite",
    "models/gemini-2.5-flash",
    "models/gemini-2.5-pro",
    "models/gemini-3-flash-preview",
    "models/gemini-3-pro-preview",
]

for model_name in models_to_try:
    try:
        response = client.models.generate_content(
            model=model_name,
            contents="Say hello in one word",
        )
        print(f"OK {model_name}: WORKS! Response: {response.text.strip()}")
    except Exception as e:
        err = str(e)
        if 'quota' in err.lower() or '429' in err:
            print(f"FAIL {model_name}: QUOTA EXCEEDED")
        elif '404' in err:
            print(f"FAIL {model_name}: NOT FOUND")
        else:
            print(f"FAIL {model_name}: {err[:200]}")
