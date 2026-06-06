# Файл 'virus_total_checker.py': класс для проверки всех найденных ip адресов и хэшей файлов на ресурсе VirusTotal.
# * Возможно в дальнейшем можно разделить на два класса или более, по своим конкретным обязанностям. Может из абстрактного класса.

import requests
from modules.real_time import CurrentTime


class VirusTotalChecker:
    API_URL = 'https://www.virustotal.com/api/v3/'

    IP_ANALYS_ENDPOINT = 'ip_addresses/'
    FILE_DIGEST_ANALYS_ENDPOINT = 'files/'
    ANALYSIS_STATUS = ("malicious", "suspicious", "undetected", "harmless")
    ANALYSIS_OBJECT = ('IP address', 'File digest')

    def __init__(self, api_key, data_to_check, program_logger):
        self.headers = { 'x-apikey': api_key }
        self.data_to_check = data_to_check
        self._checks_result = []

        program_logger.info('Started scanning on VirusTotal')

        try:
            [self.checks_result.append(
                VirusTotalChecker.convert_response(self.get_response(VirusTotalChecker.IP_ANALYS_ENDPOINT, log_data[0]),
                                                   self.get_response(VirusTotalChecker.FILE_DIGEST_ANALYS_ENDPOINT, log_data[1]),
                                                   log_data)) for log_data in self.data_to_check]

            program_logger.info('Scanning is successful')

        except requests.exceptions.ConnectionError:
            program_logger.error('Network connection critical error')
            exit(0)

    @property
    def checks_result(self):
        return self._checks_result

    # Метод для формирования результата проверки с отдельно взятыми параметрами ответа от VirusTotal.

    @staticmethod
    def convert_response(ip_analys_response, hash_analys_response, log_data):
        result = {}

        status_type = lambda analysis_object, analysis_status: f"{analysis_object} status {analysis_status} count"
        status_count = lambda analysis_type, analysis_status: analysis_type["data"]["attributes"]["last_analysis_stats"][analysis_status]

        result["VirusTotal analysis time"] = f'>> {CurrentTime.get_time()} <<'
        result["Client action time"] = log_data[2].strip('[]')
        result["Client IP address"] = log_data[0]

        for status in VirusTotalChecker.ANALYSIS_STATUS:
            result[status_type(VirusTotalChecker.ANALYSIS_OBJECT[0], status)] = status_count(ip_analys_response, status)

        result["Client uploaded file digest"] = log_data[1]

        if hash_analys_response is not None:
            for status in VirusTotalChecker.ANALYSIS_STATUS:
                result[status_type(VirusTotalChecker.ANALYSIS_OBJECT[1], status)] = status_count(hash_analys_response, status)
        else:
            result[f"{VirusTotalChecker.ANALYSIS_OBJECT[1]} status"] = 'Not exist in VirusTotal base'

        return result




    def get_response(self, endpoint_type, log_data_type):
        response = requests.get(f'{VirusTotalChecker.API_URL}{endpoint_type}{log_data_type}', headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None
