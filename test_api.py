import requests

url = "http://127.0.0.1:5000/describe"

payload = {
    "text": "This is a software development contract for 6 months between two companies."
}

response = requests.post(url, json=payload)

print(response.json())