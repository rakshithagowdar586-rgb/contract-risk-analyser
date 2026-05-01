import requests

url = "http://127.0.0.1:5000/describe"

data = {
    "text": "This contract has unlimited liability and no termination clause."
}

response = requests.post(url, json=data)

print(response.json())