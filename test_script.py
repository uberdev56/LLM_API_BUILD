import requests
from dotenv import load_dotenv
import os

load_dotenv()

base_url = "http://localhost:8000/generate"

# get prompt from the user
prompt = input("Enter prompt: ").strip()
if not prompt:
    raise SystemExit("No prompt provided. Exiting.")

headers = {"x-api-key": os.getenv("API_KEY"), "Content-Type": "application/json"}

try:
    response = requests.post(base_url, headers=headers, params={"prompt": prompt}, timeout=30)
    response.raise_for_status()
    try:
        print(response.json())
    except ValueError:
        # fallback if response is not JSON
        print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")