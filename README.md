# Virus Scanner CLI

## Утилита командной оболочки для анализа файлов, IP адресов, доменных имен и URL адресов на вредоносную активность.
## Функционирование программы осуществляется посредством интеграции с Virus Total API v3.
### Параметры: `[ key target variant data report output ]`
- key: API ключ Virus Total
<br><br>
- target: флаг анализируемого объекта (`"i" - ip адрес, "dn" - доменное имя, "u" - url адрес, "f" - файл`)
<br><br>
- variant: флаг варианта данных (`"o" - единичный объект, "l" - лог файл (.txt или .log), "d" - директория, папка`)
<br><br>
- data: анализируемые данные. Пример: `192.168.10.123; example.com; https://example.ru; C:\Folder\Subfolder\ | file.exe | log_file.txt | log_file.log` (если путь с пробелами, то берите в кавычки)
<br><br>
- report: тип файла отчета. Допустимые значения: `csv, json, html`
<br><br>
- output: директория для файлов отчетов. Необязательный параметр, по умолчанию `./reports/`
## v. 1.0 Beta
#### В лог файле анализируемые данные размещаются на каждой строке. Например:
`192.168.20.101`
<br>
`192.168.20.102`
<br>
`192.168.20.103`
<br>
`192.168.20.104`
#### Допустимо передавать в аргумент директорию с несколькими лог файлами.
#### Для анализа файлов допустимы только полные пути, также и в файле лога. В директории соответственно сами файлы. Допустимый размер файла до 200 Мб.
#### Отчеты создаются по каждому объекту отдельно. Имя отчета составляется из имени объекта, даты и времени создания.
#### Основные действия утилиты и ошибки логируются в файл `./program_log.log`
#### Проверяются только HTTP статусы 200, 409 и 401.
## Запуск из виртуального окружения
1. В Windows запустите PowerShell, в Linux запустите терминал.
<br><br>
2. Клонируйте репозиторий:
```
git clone https://github.com/Fluenoriph/VirusScanner.git
```
3. Перейдите в директорию программы:
- OS Windows
```
cd .\VirusScanner
```
- OS Linux
```
cd ./VirusScanner
```
4. Создайте виртуальное окружение:
- OS Windows
```
python -m venv venv
```
- OS Linux
```
python3 -m venv venv
```
5. Активируйте окружение:
- OS Windows
```
.\venv\Scripts\activate
```
- OS Linux
```
source venv/bin/activate
```
    После активации в командной строке появится префикс (venv) — это значит, что всё, что вы запускаете и устанавливаете, относится к окружению.
    Деактивировать можно командой: 'deactivate'
6. Установите пакеты:
```
pip install -r requirements.txt
```
7. Запустите утилиту:
```
python virus_scanner_cli.py YOUR_API_KEY i o 192.168.10.123 html
```
## Запуск в контейнере Docker
```
cd ./VirusScanner
docker build -t virus-scanner .
mkdir -p work
```
- Анализ единичного объекта
```
docker run --rm --user "$(id -u):$(id -g)" -e TZ="$(timedatectl show -p Timezone --value)" -v "$(pwd)/work:/work" virus-scanner YOUR_API_KEY i o 192.168.10.123 html
```
- Анализ лог файла
```
docker run --rm --user "$(id -u):$(id -g)" -e TZ="$(timedatectl show -p Timezone --value)" -v "$(pwd)/work:/work" -v "/folder/subfolder:/data:ro" virus-scanner YOUR_API_KEY i l /data/log_file.log csv
```
- Анализ папки с файлами или логами
```
docker run --rm --user "$(id -u):$(id -g)" -e TZ="$(timedatectl show -p Timezone --value)" -v "$(pwd)/work:/work" -v "/home/me/samples:/home/me/samples:ro" virus-scanner YOUR_API_KEY f d /home/me/samples html
```
- Свой путь отчетов
```
mkdir -p /home/me/new_reports_folder
docker run --rm --user "$(id -u):$(id -g)" -e TZ="$(timedatectl show -p Timezone --value)" -v "$(pwd)/work:/work" -v "/home/me/new_reports_folder:/reports" virus-scanner YOUR_API_KEY u o https://example.com json /reports
```