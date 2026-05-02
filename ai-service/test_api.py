import requests

url = "http://127.0.0.1:5000/contract"

payload = {
    "description": "Software contract with unclear IP and liability"
}

response = requests.post(url, json=payload)

print("STATUS CODE:", response.status_code)
print("RAW RESPONSE:", response.text)

try:
    print("JSON:", response.json())
except Exception as e:
    print("Not JSON response:", e)