"""Test newer Gemini models."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from google import genai

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

client = genai.Client(api_key=api_key)

models_to_try = [
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b",
    "gemini-1.5-pro",
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
