import os
import requests
from flask.cli import load_dotenv
from modules.base_virus_total_analyser import BaseVirusTotalAnalyser


class DirectEndpointVirusTotalAnalyser(BaseVirusTotalAnalyser):
    def __init__(self, api_key, endpoint, data):
        super().__init__(api_key, endpoint, data)

    def analyse(self):
        response = requests.get(BaseVirusTotalAnalyser.API_URL + self.endpoint + self.data, headers=self.headers)

        if response.status_code == 200:  # separated method
            return response.json()
        else:
            return None # Message ? exit ?


load_dotenv()

ip_analys = DirectEndpointVirusTotalAnalyser(os.getenv('API_KEY'), '/ip_addresses/', '8.8.8.8')

result_ip = ip_analys.analyse()

print(f'IP result\n{result_ip["data"]["id"]}\n{result_ip["data"]["attributes"]["last_analysis_stats"]}')
print('\n')

domain_analys = DirectEndpointVirusTotalAnalyser(os.getenv('API_KEY'), '/domains/', 'metanit.com')
result_domain = ip_analys.analyse()

print(f'Domain result\n{result_domain["data"]["id"]}\n{result_domain["data"]["attributes"]["last_analysis_stats"]}')