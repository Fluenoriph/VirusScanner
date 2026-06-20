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
from pathlib import Path
import typer
from rich import print

from modules.data_validator.file_validator import FileValidator
from modules.data_validator.target_web_data_validator import TargetWebDataValidator
from modules.data_validator.rgx_patterns import IP_ADDRESS

#from dotenv import load_dotenv
from modules.report_generator.base_report_generator import BaseReportGenerator
from modules.virus_analyser.big_file_analyser import BigFileAnalyser
from modules.virus_analyser.direct_endpoint_analyser import DirectEndpointAnalyser
from modules.virus_analyser.small_file_analyser import SmallFileAnalyser
from modules.virus_analyser.url_analyser import UrlAnalyser


class VirusScannerCLI:
    APP = typer.Typer()
    APP_DIRECTORY = typer.get_app_dir('virus-scanner') # name ????

    def __init__(self):
        VirusScannerCLI.APP()

    @staticmethod
    @APP.command()
    def analyse_the_data(virus_total_api_key: str, data_to_analyse: str,
                         target: Annotated[Literal['ip', 'domain', 'url', 'file'], typer.Argument()]):  # testing !!!
                         #variant: Annotated[Literal['object', 'log', 'directory'], typer.Argument()]
                         #output: Annotated[str, typer.Argument()] = APP_DIRECTORY,
                         #report: Annotated[str, typer.Argument()] = BaseReportGenerator.REPORT_FILE_TYPE[0]):

        #input_data = 'virus_total_api_key', 'data_to_analyse', 'output', 'report', 'target', 'verbose'

        #big /home/fluenoriph/Downloads/Backup_PDF_Protocols.Scan.Files_2.0.exe
        #small /home/fluenoriph/music_test/media/ripher12/samsung_ssd/ELECTRONICA/[ASHADOW941CD] Moving Shadow 04.1 mixed By Timecode [2004]/11. The Ark.flac

        web_data_analyser = {
            'ip': DirectEndpointAnalyser(virus_total_api_key, data_to_analyse, 'ip'),
            'domain': DirectEndpointAnalyser(virus_total_api_key, data_to_analyse, 'domain'),
            'url': UrlAnalyser(virus_total_api_key, data_to_analyse)
        }

        file_analyser = {
            'small': SmallFileAnalyser(virus_total_api_key, data_to_analyse),
            'big': BigFileAnalyser(virus_total_api_key, data_to_analyse)
        }

        # если в ответе одни нули, то повтор.

        print("[green]Scanner started ![/green]")

        if target != 'file':
            analyser_engine = web_data_analyser[target]

            if analyser_engine.analyse():
                print("[green] APP OK !!! [/green]")
            else:
                print("[red] APP FAILED !!! [/red]")

            print(analyser_engine.result_data)
        else:
            file_size = os.path.getsize(data_to_analyse)  # checking the exist file !!!
            print(file_size)
            print(data_to_analyse)

            if file_size < 33554432:
                analyser_engine = file_analyser['small']

                if analyser_engine.analyse():
                    print("[green] APP OK !!! [/green]")
                else:
                    print("[red] APP FAILED !!! [/red]")

                print(analyser_engine.result_data)
            else:   # and < 209715200 (200 mb)
                analyser_engine = file_analyser['big']

                if analyser_engine.analyse():
                    print("[green] APP OK !!! [/green]")
                else:
                    print("[red] APP FAILED !!! [/red]")

                print(analyser_engine.result_data)


VirusScannerCLI()
