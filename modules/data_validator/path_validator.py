import os
from modules.data_validator.base_validator import BaseValidator


class PathValidator(BaseValidator):
    def validate(self, data):
        if os.path.exists(os.path.normcase(data)):
            return True
        else:
            return False
