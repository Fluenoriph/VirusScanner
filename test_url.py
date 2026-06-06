import os
import requests


API_URL = "https://www.virustotal.com/api/v3/"


KEY = input("Enter your VirusTotal API Key: ")

data = {"url": "https://love.intim25.vip"}
headers = { "x-apikey": KEY }

response_url_id = requests.post(f'{API_URL+'urls'}', headers=headers, data=data)

URL_ANALYSIS_ID = response_url_id.json()["data"]["id"]

result_url = API_URL + 'analyses/' + URL_ANALYSIS_ID

result_response = requests.get(result_url, headers=headers)

print(result_response.text)