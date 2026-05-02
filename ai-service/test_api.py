import requests

url = "http://127.0.0.1:5000/recommend"

payload = {
    "text": """
This agreement is between Company A and Company B for software development.
Duration is 6 months. Payment is milestone-based. 
Company A will deliver code, Company B will review and approve.

There is no clarity on intellectual property ownership or liability.
Termination clause is not defined clearly.
"""
}

response = requests.post(url, json=payload)

print(response.json())