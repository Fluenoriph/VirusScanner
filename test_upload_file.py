import os
import requests
from flask.cli import load_dotenv

url = "https://www.virustotal.com/api/v3/files/upload_url"


#file = input("Enter your file size (< 32 mb: 1) or (32 mb to 200 mb: 2) > ")

load_dotenv()

key = os.getenv("API_KEY")
headers = { "x-apikey": key }

response = requests.get(url, headers=headers)

print(response.json()) # data upload url

