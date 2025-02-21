import json
import requests

OPENRED_BASEURL = "https://openred.ibercivis.es/api"
ENDPOINT_DEVICEMODELS = f"{OPENRED_BASEURL}/device-models/"
ENDPOINT_MEASUREMENTS = f"{OPENRED_BASEURL}/measurements/"
headers  = {
    "accept": "application/json",
    "X-CSRFTOKEN": "aU8tvFz8z9iZafc3iPjEawa1CNjpnz2iKqRypLGl8N1eeCyh13h7YBkD2zZRH6zz"
}
data     = {
    "id": 0,
    "device": 1,
    "user": 1,
    "latitude": 39.92,
    "longitude": -1.03,
    "altitude": 0,
    "values": {
      "radiation": 0.05446434020996094,
      "DoseRate": 0.05446434020996094,
      "CPS": 2.859375,
      "DoseErrorRate": 24.9,
      "CPSErrorRate": 7.3,
      "DeviceSN": "RC-102-00704",
      "Temperature": 25.72,
      "ChargeLevel": 98.81,
      "Temperature1": 26.5,
      "Humidity": 37.9,
      "Pressure": 997.1,
      "VBAT": 4.226
    },
    "dateTime": "2025-02-21T13:06:40.406Z", 
}

# DEVICE MODELS
response = requests.get(ENDPOINT_DEVICEMODELS, headers=headers)
print(response)
print(json.dumps(response.json(), indent=2))

# MEASUREMENTS
response = requests.post(ENDPOINT_MEASUREMENTS, headers=headers, json=data)
print(response)
print(json.dumps(response.json(), indent=2))


