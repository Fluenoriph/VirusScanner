import re
from modules.app_data import RGX_PATTERN
from modules.data_validator.base_validator import BaseValidator


class TargetWebDataValidator(BaseValidator):
    def __init__(self, target_flag):
        self.rgx_pattern = RGX_PATTERN[target_flag]

    def validate(self, data):
        if re.search(self.rgx_pattern, data):
            return True
        else:
            return False
