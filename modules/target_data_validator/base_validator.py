# 'base_validator.py' - базовый класс валидаторов данных для анализа.

from abc import ABC, abstractmethod


class BaseValidator(ABC):
    @abstractmethod
    def validate(self, data):
        pass
