import requests
import json
endpoint1= 'https://openred.ibercivis.es/api/measurements/'
datos= {
  "device": 1,
  "user": 1,
  "latitude": 39.92,
  "longitude": -1.03,
  "altitude": 0,
  "values": {"radiation":50},
  "dateTime": "2025-02-21T13:06:40.406Z",
  "accuracy": 0,
  "unit": "string",
  "notes": "string",
  "weather": {}
}
headers={"accept: application/json","Content-Type: application/json","X-CSRFTOKEN: wIfvK8q7caSt7vkPb2kSwbQfIm4jhYfCjUnugxDOt6DmcnnXqchoEAobLUDCj8oT"}
response= requests.post(endpoint1, data=datos, headers=headers)
print(response.json())

