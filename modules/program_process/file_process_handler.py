from modules.data_validator.file_validator import FileValidator
from modules.program_process.base_program_process_handler import BaseProgramProcessHandler
from modules.virus_analyser.file_analyser_selector import FileAnalyserSelector


class FileProcessHandler(BaseProgramProcessHandler):
    def __init__(self, api_key, target_flag, output_path, report_file_type):
        super().__init__(api_key, target_flag, output_path, report_file_type)

    def process_the_object(self, data):
        validator = FileValidator()

        if validator.validate(data):
            file_size_selector = FileAnalyserSelector()

            if file_size_selector.select(data):
                file_analyser = file_size_selector.analyser
                file_analyser.api_key = self.api_key

                result_payload = self.process_the_analysis(file_analyser)

                if result_payload is not False:
                    print(result_payload)

                    self.process_the_report(result_payload)
                else:
                    print('Error connection to Virus Total')
                    return

            else:
                print('File too large !')  # BAD ARGUMENT SIZE !
                # write to program log !!
                return
        else:
            print('File not found ! Bad argument !')
            return
