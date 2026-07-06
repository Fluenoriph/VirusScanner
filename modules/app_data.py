import re


TARGET = 'ip', 'domain', 'url', 'file'
VARIANT = 'object', 'log', 'directory'

DIRECT_ENDPOINT_STATS_KEY = 'last_analysis_stats'
URL_AND_FILE_STATS_KEY = 'stats'

STATS_KEY = {
    TARGET[0]: DIRECT_ENDPOINT_STATS_KEY,
    TARGET[1]: DIRECT_ENDPOINT_STATS_KEY,
    TARGET[2]: URL_AND_FILE_STATS_KEY,
    TARGET[3]: URL_AND_FILE_STATS_KEY
}

ENDPOINT = {
    TARGET[0]: '/ip_addresses/',
    TARGET[1]: '/domains/',
    TARGET[2]: '/urls',
    TARGET[3]: ('/files', '/files/upload_url')
}

RGX_PATTERN = {
    TARGET[0]: re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"),
    TARGET[1]: re.compile(r"^[a-zA-Z0-9][-a-zA-Z0-9\\.]*$"),
    TARGET[2]: re.compile(r"^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\."
                          r"[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$")
}
