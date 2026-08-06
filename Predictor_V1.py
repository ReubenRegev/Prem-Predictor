import os
from dotenv import load_dotenv

load_dotenv()  

api_key = os.getenv("FOOTBALL_DATA_KEY")
print(api_key)  

import requests

headers = {
    "X-Auth-Token": api_key
}

url = "https://api.football-data.org/v4/competitions/PL/matches?season=2024"

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)

data = response.json()
print("Top-level keys:", data.keys())
print("Number of matches:", len(data["matches"]))
print("First match:\n", data["matches"][0])
import json

with open("data/pl_2024_25_raw.json", "w") as f:
    json.dump(data, f)