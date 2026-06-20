


class AppData:
    TARGET = 'ip', 'domain', 'url', 'file'
    VARIANT = 'object', 'log', 'directory'

    DIRECT_ENDPOINT_STATS_KEY = 'last_analysis_stats'
    URL_AND_FILE_STATS_KEY = 'stats'

    PROCESS_HANDLER = {
        'ip': 'ip',
        'domain': 'domain',
        'url': 'url',
    }

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
        TARGET[3]: { 'small': '/files', 'big': '/files/upload_url' }
    }
