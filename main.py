import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# --- ENV VARS ---
load_dotenv()

app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")
SHEETY_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")


URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/90eb9c28deebc309920c1b415fe8e67b/workoutTracker/sheet1"

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
    "Content-Type": "application/json"
}

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

# Get exercise data from Nutritionix

query = input("Tell me what exercise you did: ")

payload = {
    "query": query,
    "gender": "female",
    "weight_kg": 68,
    "height_cm": 165,
    "age": 27
}

response = requests.post(URL, headers=headers, json=payload)
exercises = response.json().get("exercises", [])

# Log each exercise into Sheety
for ex in exercises:
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    sheet_input = {
        "sheet1": {
            "date": date_str,
            "time": time_str,
            "exercise": ex["name"].title(),
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"],
        }
    }

    sheety_response = requests.post(sheety_url, headers=sheety_headers, json=sheet_input)

    if sheety_response.status_code == 200 or sheety_response.status_code == 201:
    # if sheety_response.status_code in (200, 201):
        print(f"✅ Logged: {ex['name'].title()} ({ex['duration_min']} mins, {ex['nf_calories']} cal)")
    else:
        print("❌ Error logging to Sheety:", sheety_response.text)


















# payload = {
#     "query": "did 45 minutes of power yoga",
#     "gender": "female",
#     "weight_kg": 65,
#     "height_cm": 165,
#     "age": 36,
# }

# response = requests.post(URL, headers=headers, json=payload)

# if response.status_code == 200:
#     data = response.json()
#     print("✅ Success! Parsed exercises:")
#     for ex in data.get("exercises", []):
#         print(f"- {ex.get('name')}: {ex.get('duration_min')} mins, {ex.get('nf_calories')} cal")
# else:
#     print("❌ Error:", response.status_code, response.text)
