import os
import requests
import pprint
import json
from dotenv import load_dotenv
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client.registry import Collector


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

class NatureRemoCollector(Collector):
    def collect(self):
        temperature = GaugeMetricFamily(
                'nature_remo_temperature_celsius',
                'Room temperature reported by Nature Remo Device',
                labels=['device']
        )
    
        for device in data:
            device_name = device['name']
            device_temp = device['newest_events']['te']['val']
            temperature.add_metric([device_name], device_temp)
        
        yield temperature

REGISTRY.register(NatureRemoCollector())

if __name__ == '__main__':
    start_http_server(8000)
    import time
    while True:
        time.sleep(1)
