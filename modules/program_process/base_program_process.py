import abc
import os


class BaseProgramProcess(abc.ABC):
    # logger ???

    def __init__(self, input_data):
        self.api_key = input_data[0]
        #self.report_format = input_data[3]
        #self._result_data = []

        #if not os.path.exists(input_data[2]):
            #os.makedirs(input_data[2])  # raise ??
            #self.output_path = input_data[2]

    #@property
    #def result_data(self):
        #return self._result_data
