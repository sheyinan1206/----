import requests
import json

method = "POST"

url = "http://localhost:90/api/login"

data = {"username": "qianwei", "password": "123456"}

# payload = json.dumps({
#   "username": "qianwei",
#   "password": "123456"
# })
# headers = {
#   'Content-Type': 'application/json'
# }

response = requests.request(method, url, json=data)

print(response.text)