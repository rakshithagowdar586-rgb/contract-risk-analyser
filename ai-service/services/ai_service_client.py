import requests

class AiServiceClient:

    def analyze_contract(self, text):
        try:
            url = "http://127.0.0.1:5000/describe"

            response = requests.post(url, json={
                "text": text
            })

            return response.json()

        except Exception as e:
            print("AI ERROR:", e)
            return None