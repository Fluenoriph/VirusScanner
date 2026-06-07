import os

import requests
import dotenv
from flask.cli import load_dotenv

from modules.base_virus_total_analyser import BaseVirusTotalAnalyser


class DirectEndpointVirusTotalAnalyser(BaseVirusTotalAnalyser):
    def __init__(self, api_key):
        super().__init__(api_key)

    def analyze(self, endpoint, data):
        response = requests.get(BaseVirusTotalAnalyser.API_URL + endpoint + data, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None # Message ? exit ?


load_dotenv()

program = DirectEndpointVirusTotalAnalyser(os.getenv('API_KEY'))


result_ip = program.analyze('/ip_addresses/', '8.8.8.8')

print(f'IP result\n{result_ip["data"]["id"]}\n{result_ip["data"]["attributes"]["last_analysis_stats"]}')
print('\n')

result_domain = program.analyze('/domains/', 'metanit.com')

print(f'Domain result\n{result_domain["data"]["id"]}\n{result_domain["data"]["attributes"]["last_analysis_stats"]}')