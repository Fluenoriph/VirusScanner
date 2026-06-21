import re
from modules.app_data import AppData
from modules.data_validator.base_validator import BaseValidator


class TargetWebDataValidator(BaseValidator):
    def __init__(self, target_type):
        self.rgx_pattern = AppData.RGX_PATTERN[target_type]

    def validate(self, data):
        #match = re.search(self.rgx_pattern, data)
        if re.search(self.rgx_pattern, data):
            return True
        else:
            return False
