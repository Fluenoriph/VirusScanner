# 'file_validator.py' - проверка валидности файла.

import os
from modules.target_data_validator.base_validator import BaseValidator


class FileValidator(BaseValidator):
    def validate(self, data):
        if os.path.exists(data) and os.path.isfile(data):
            return True
        else:
            return False
