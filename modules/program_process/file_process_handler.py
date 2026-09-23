from modules.program_process.base_program_process_handler import BaseProgramProcessHandler
from modules.virus_analyser.file_analyser_selector import FileAnalyserSelector


class FileProcessHandler(BaseProgramProcessHandler):
    def __init__(self, api_key):
        super().__init__(api_key)

    def process_the_object(self, data):
        file_size_selector = FileAnalyserSelector()

        if file_size_selector.select(data):
            analyser = file_size_selector.result
            analyser.api_key = self.api_key

            result_payload = self.process_the_analysis(analyser)

            if result_payload is not False:
                print(result_payload)
                # generate report !
            else:
                print('Error connection to Virus Total')
                return

        else:
            print(f"Error -- {file_size_selector.result}")  # BAD ARGUMENT !
            # write to program log !!
            return
