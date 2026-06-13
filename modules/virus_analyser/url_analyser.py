import os

import requests
from flask.cli import load_dotenv

from modules.virus_analyser.base_analyser import BaseAnalyser


class UrlAnalyser(BaseAnalyser):
    def __init__(self, api_key, endpoint, data):
        super().__init__(api_key, endpoint, data)

    def analyse(self):
        response_id = self.get_data_id()

        if response_id.status_code == 200:
            response_result = requests.get(BaseAnalyser.API_URL + '/analyses/' +
                                           response_id.json()["data"]["id"], headers=self.headers)

            # if 400
            return response_result.json()
        else:
            return None # Message ? exit ? #

    def get_data_id(self):
        return requests.post(BaseAnalyser.API_URL + self.endpoint, headers=self.headers,
                             data={ 'url': self.data })


load_dotenv()
url_scanner = UrlAnalyser(os.getenv('API_KEY'), '/urls', 'https://cyberyozh.com')

result = url_scanner.analyse()

out = { "Analysis time": 2026 }
out.update({ "URL": result["meta"]["url_info"]["url"] })
out.update(result["data"]["attributes"]["stats"])

print(out)

#print(f'URL result: {result["data"]["attributes"]["stats"]}\n{result["meta"]["url_info"]["url"]}')