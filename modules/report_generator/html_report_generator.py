from modules.report_generator.base_report_generator import BaseReportGenerator
from modules.app_data import ANALYSIS_STATUS
from modules.app_data import REPORT_FILE_TYPE


class HtmlReportGenerator(BaseReportGenerator):
    def __init__(self, result_data, report_path, target_flag):
        super().__init__(result_data, report_path, target_flag)

    def generate(self):
        total_count = 0
        for status in ANALYSIS_STATUS:
            if status in self.result_data:
                total_count += self.result_data[status]

        rows = "\n".join(f"<tr><td>{key}</td><td>{value}</td></tr>"
                         for key, value in self.result_data.items())

        html_content = f"""<!DOCTYPE html>
        <html lang="ru">
        <head>
        <meta charset="UTF-8">
        <title>Отчёт анализа объекта: {self.target_object}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; max-width: 500px; background: #fff; }}
            th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
            th {{ background-color: #333; color: #fff; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            .malicious {{ color: #c0392b; font-weight: bold; }}
            .harmless {{ color: #27ae60; font-weight: bold; }}
        </style>
        </head>
        <body>
            <h1>Отчёт анализа: {self.target_object}</h1>
            <p>Дата анализа: {self.result_data['analysis time']}</p>
            <table>
                <tr><th>Параметр</th><th>Значение</th></tr>
                {rows}
            </table>
            <p><strong>Всего проверок:</strong> {total_count}</p>
        </body>
        </html>"""

        with open (self.create_report_file(REPORT_FILE_TYPE[0]), 'w', encoding='utf-8') as file:
            file.write(html_content)
