import abc
from modules.program_process.base_program_process import BaseProgramProcess


class ObjectVariantProgramProcess(BaseProgramProcess, abc.ABC):
    def __init__(self, input_data):
        super().__init__(input_data)
        validator = ObjectVariantProgramProcess.validator()
        self.target_data = validator.validate(input_data[1])

        if self.target_data:
            self.result_data = self.analyser().analyse(self.target_data)

            if self.result_data[0]:
                print(f'YES OK !!!!!!\n{self.result_data[1]}')
            else:
                print(f'RESULT ERROR !!!!!!\n{self.result_data[1]}')

        else:
            print("Input data is invalid")
            #exit return code

    @staticmethod
    @abc.abstractmethod
    def validator():
        pass

    @abc.abstractmethod
    def analyser(self):
        pass