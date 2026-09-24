import re


TARGET_FLAG = 'i', 'dm', 'u', 'f'

TARGET_NAME = {
    TARGET_FLAG[0]: 'ip',
    TARGET_FLAG[1]: 'domain',
    TARGET_FLAG[2]: 'url',
    TARGET_FLAG[3]: 'file'
}
# object, log, directory
VARIANT_FLAG = 'o', 'l', 'dr'

ANALYSIS_STATUS = ('malicious', 'suspicious', 'undetected', 'harmless', 'timeout', 'confirmed-timeout',
                   'failure', 'type-unsupported')

DIRECT_ENDPOINT_STATS_KEY = 'last_analysis_stats'
URL_AND_FILE_STATS_KEY = 'stats'

STATS_KEY = {
    TARGET_FLAG[0]: DIRECT_ENDPOINT_STATS_KEY,
    TARGET_FLAG[1]: DIRECT_ENDPOINT_STATS_KEY,
    TARGET_FLAG[2]: URL_AND_FILE_STATS_KEY,
    TARGET_FLAG[3]: URL_AND_FILE_STATS_KEY
}

ENDPOINT = {
    TARGET_FLAG[0]: '/ip_addresses/',
    TARGET_FLAG[1]: '/domains/',
    TARGET_FLAG[2]: '/urls',
    TARGET_FLAG[3]: ('/files', '/files/upload_url')
}

RGX_PATTERN = {
    TARGET_FLAG[0]: re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'),
    TARGET_FLAG[1]: re.compile(r'^[a-zA-Z0-9][-a-zA-Z0-9\\.]*$'),
    TARGET_FLAG[2]: re.compile(r'https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
}

REPORT_FILE_TYPE = 'html', 'csv', 'json'
