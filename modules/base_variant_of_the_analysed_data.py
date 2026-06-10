import abc


class BaseVariantOfTheAnalysedData(abc.ABC):
    def __init__(self, data):
        self.data = data

    @abc.abstractmethod
    def