"""
Application name: Virus Scanner
Version: 1.0
Date:  2026 г.
Author: Ivan Bogdanov
Contacts: fluenoriph@gmail.com, fluenoriph@yandex.ru
"""

import os
import sys
from typing import Annotated
import typer
from modules.text_constants import REPORT_FILE_TYPE


class VirusScannerCLI:
    APP = typer.Typer()
    APP_DIRECTORY = typer.get_app_dir('virus-scanner') # name ????
    TARGET_DATA = 'ip', 'domain', 'url', 'file'
    DATA_VARIANT = 'object', 'log', 'directory'

    def __init__(self):
        VirusScannerCLI.APP()

    @staticmethod
    @APP.command()
    def analyse_the_data(virus_total_api_key: str, data_to_analyse: str,
                         target: Annotated[TARGET_DATA, typer.Argument()],  # testing !!!
                         variant: Annotated[DATA_VARIANT, typer.Argument()],
                         output_path: Annotated[str, typer.Argument()] = APP_DIRECTORY,
                         report_format: Annotated[str, typer.Argument()] = REPORT_FILE_TYPE[0]):

        # typer echo Start

            # process

        # echo Scanning done / bad - exit









