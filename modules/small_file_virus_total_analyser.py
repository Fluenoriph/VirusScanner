import os

import requests
from flask.cli import load_dotenv

from modules.base_virus_total_analyser import BaseVirusTotalAnalyser
from modules.url_virus_total_analyser import UrlVirusTotalAnalyser


class SmallFileVirusTotalAnalyser(UrlVirusTotalAnalyser):
    def __init__(self, api_key, endpoint, data):
        super().__init__(api_key, endpoint, data)

    def get_data_id(self):
        with open(self.data, 'rb') as file:
            files = { 'file': (self.data, file) }

            # if 200 or 400 ??
            return requests.post(BaseVirusTotalAnalyser.API_URL + self.endpoint, headers=self.headers, files=files)


load_dotenv()

file_scanner = SmallFileVirusTotalAnalyser(os.getenv('API_KEY'), '/files', '/home/ripher12/certificate_ru.pdf')

result = file_scanner.analyse()
print(f'{result["data"]["attributes"]["stats"]}\n{result["meta"]["file_info"]["sha256"]}\n{result["meta"]["file_info"]["size"]}')

# может быть ошибка 400 или статусы все нули ???