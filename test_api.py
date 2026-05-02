import requests

url = "http://127.0.0.1:5000/recommend"

payload = {
    "text": "This contract has unclear payment terms and no termination clause."
}

response = requests.post(url, json=payload)

print(response.json())