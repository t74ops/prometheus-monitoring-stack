import os
import requests
import pprint
import json
from dotenv import load_dotenv
from prometheus_client import start_http_server


load_dotenv()
token = os.environ.get("NATURE_REMO_TOKEN")

url = "https://api.nature.global/1/devices"
headers = {'Authorization': 'Bearer ' + token}

res = requests.get(url, headers=headers)
data = res.json()

for device in data:
    device_name = device['name']
    device_temp = device['newest_events']['te']['val']
    print(device_name, device_temp)


if __name__ == '__main__':
    start_http_server(8000)
    import time
    while True:
        time.sleep(1)
