import abc


class BaseValidator(abc.ABC):
    @abc.abstractmethod
    def validate(self, data):
        pass