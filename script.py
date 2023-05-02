from pathlib import Path

from pravo_api import PravoApi

data_folder = Path("./worker_test_folder").absolute()

api = PravoApi(
    FEDERAL_GOVERNMENT_BODY="Правительство",
    DATA_FOLDER=data_folder,
    FROM_DATE="20.12.2013",
    TO_DATE="01.01.2014",
    log_file="my.log",
    SAVE_FORMAT="txt",  # или html
    parse_appointments=True,
    parse_only=False,
)

api.get(output_filename="results.json")
