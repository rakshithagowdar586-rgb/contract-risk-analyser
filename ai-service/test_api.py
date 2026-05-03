import requests
import json

BASE_URL = "http://127.0.0.1:5000"


def test_describe():

    url = f"{BASE_URL}/describe"

    payload = {
        "text": "Software contract with unclear IP and liability"
    }

    response = requests.post(url, json=payload)

    print("\nSTATUS CODE:", response.status_code)
    print("RAW RESPONSE:", response.text)

    try:
        print("\nJSON:", json.dumps(response.json(), indent=2))
    except Exception as e:
        print("\nJSON ERROR:", str(e))


if __name__ == "__main__":
    test_describe()