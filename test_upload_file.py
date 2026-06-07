import requests


url = "https://www.virustotal.com/api/v3/files/upload_url"

KEY = input("Enter your VirusTotal API Key: ")
file = input("Enter your file size (< 32 mb: 1) or (32 mb to 200 mb: 2) > ")



headers = { "x-apikey": KEY }

response = requests.get(url, headers=headers)

print(response.text) # data upload url

