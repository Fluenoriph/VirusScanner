# 'web_data_validator.py' - проверка валидности веб-данных (domain, url, ip address).

import re
from modules.app_data import RGX_PATTERN
from modules.target_data_validator.base_validator import BaseValidator


class WebDataValidator(BaseValidator):
    def __init__(self, target_flag):
        self.rgx_pattern = RGX_PATTERN[target_flag]

    def validate(self, data):
        if re.search(self.rgx_pattern, data):
            return True
        else:
            return False
