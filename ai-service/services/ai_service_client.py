import requests

class AiServiceClient:

    def analyze_contract(self, text):
        try:
            url = "http://127.0.0.1:5000/describe"

            print("SENDING REQUEST TO AI SERVER...")

            response = requests.post(url, json={"text": text})

            print("STATUS:", response.status_code)
            print("RAW:", response.text)

            data = response.json()

            return data

        except Exception as e:
            print("CLIENT ERROR:", e)
            return None