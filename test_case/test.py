import requests
import json

url = "http://kdtx-test.itheima.net/api/login"

payload = json.dumps({
  "username": "admin",
  "password": "HM_2023_test",
  "code": "2",
  "uuid": "f71fdc8e4e2241e9a2fae912a9961a64"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
assert response.status_code == 100
assert "token" in response.text