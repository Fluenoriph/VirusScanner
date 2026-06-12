import os
from modules.data_validator.base_validator import BaseValidator
from modules.data_validator.path_validator import PathValidator


class InlineFileValidator(BaseValidator):
    path_validator = PathValidator()

    def validate(self, data):
        if os.path.isfile(data) and InlineFileValidator.path_validator.validate(data):
            return data
        else:
            return False
