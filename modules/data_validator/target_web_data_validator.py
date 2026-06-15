import re
from modules.data_validator.base_validator import BaseValidator


class TargetWebDataValidator(BaseValidator):
    def __init__(self, rgx_pattern):
        self.rgx_pattern = rgx_pattern

    def validate(self, data):
        #match = re.search(self.rgx_pattern, data)
        if re.search(self.rgx_pattern, data):
            return True
        else:
            return False
