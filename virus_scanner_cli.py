"""
Application name: Virus Scanner
Version: 1.0
Date:  2026 г.
Author: Ivan Bogdanov
Contacts: fluenoriph@gmail.com, fluenoriph@yandex.ru
"""

import os
import sys
from typing import Annotated, Literal
import typer
from rich import print

from modules.data_validator.file_validator import FileValidator
from modules.data_validator.target_web_data_validator import TargetWebDataValidator
from modules.data_validator.rgx_patterns import IP_ADDRESS

#from dotenv import load_dotenv
from modules.report_generator.base_report_generator import BaseReportGenerator
from modules.virus_analyser.direct_endpoint_analyser import DirectEndpointAnalyser


class VirusScannerCLI:
    APP = typer.Typer()
    APP_DIRECTORY = typer.get_app_dir('virus-scanner') # name ????

    def __init__(self):
        VirusScannerCLI.APP()

    @staticmethod
    @APP.command()
    def analyse_the_data(virus_total_api_key: str, data_to_analyse: str,
                         target: Annotated[Literal['ip', 'domain', 'url', 'file'], typer.Argument()],  # testing !!!
                         variant: Annotated[Literal['object', 'log', 'directory'], typer.Argument()]):
                         #output: Annotated[str, typer.Argument()] = APP_DIRECTORY,
                         #report: Annotated[str, typer.Argument()] = BaseReportGenerator.REPORT_FILE_TYPE[0]):

        input_data = 'virus_total_api_key', 'data_to_analyse', 'output', 'report', 'target', 'verbose'

        print("[green]Scanner started ![/green]")

        if target == VirusScannerCLI.TARGET_DATA[1] and variant == VirusScannerCLI.DATA_VARIANT[0]:
# validate out path
# .........
            # validate target data
            validator = TargetWebDataValidator(IP_ADDRESS)
            valid_data = validator.validate(data_to_analyse)  # return 1 or 0

            if valid_data:
                # analyse

                analyser = DirectEndpointAnalyser(virus_total_api_key, '/ip_addresses/',
                                              valid_data, VirusScannerCLI.TARGET_DATA[0].upper())
                if analyser.analyse():
                    print(f'YES OK !!!!!!!\n{analyser.result_data}')
                else:
                    print(f'ERROR !!!!!!!\n{analyser.result_data}')

            else:
                print("[red]Invalid data![/red]")


VirusScannerCLI()


validators = (TargetWebDataValidator(IP_ADDRESS), TargetWebDataValidator('DOMAIN'),
              TargetWebDataValidator('URL'), FileValidator())

analysers =





