import os
import sys
import requests
from flask.cli import load_dotenv

from modules.base_virus_total_analyser import BaseVirusTotalAnalyser


class BigFileVirusTotalAnalyser(BaseVirusTotalAnalyser):
    def __init__(self, api_key, endpoint, data):
        super().__init__(api_key, endpoint, data)

    def analyse(self):
        response_upload_url = requests.get(BaseVirusTotalAnalyser.API_URL + self.endpoint, headers=self.headers)

        # if 200 or 400
        with open(self.data, 'rb') as file:
            files = { 'file': (self.data, file) }
            response_url = requests.post(response_upload_url.json()["data"], headers=self.headers, files=files)

        if response_url.status_code == 409:
            print('Link exists !!')  # error this !!!
            sys.exit()
            # {'error': {'code': 'AlreadySubmittedError', 'message': 'Already being submitted for scanning'}} 409 !!!!!
            # resource(link) exists !!

        # if 200, 400


        result = requests.get(response_url.json()["data"]["links"]["self"], headers=self.headers)
        # if 200, 400
        if result.status_code == 409:
            print(result.json())
            sys.exit()
        return result.json()


load_dotenv()
file = BigFileVirusTotalAnalyser(os.getenv('API_KEY'), '/files/upload_url',
                                 '/home/ripher12/Загрузки/code_1.109.0-1770171879_amd64.deb')

result_file = file.analyse()
print(f'{result_file["data"]["attributes"]["stats"]}\n{result_file["meta"]["file_info"]["md5"]}\n{result_file["meta"]["file_info"]["size"]}')

