import os
import requests


token = os.environ.get("NATURE_REMO_TOKEN")

url = "https://api.nature.global/1/devices"
headers = {'Authorization': 'Bearer ' + token}

res = requests.get(url, headers=headers)
data = res.json()

print(data)

