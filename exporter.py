import os
import requests
import pprint
import json


token = os.environ.get("NATURE_REMO_TOKEN")

url = "https://api.nature.global/1/devices"
headers = {'Authorization': 'Bearer ' + token}

res = requests.get(url, headers=headers)
data = res.json()

print(json.dumps(data))

for device in data:
    device_name = device['name']
    device_temp = device['newest_events']['te']['val']
    print(device_name, device_temp)


# pprint.pprint(data)
