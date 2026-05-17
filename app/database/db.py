import os
from langchain_community.utilities import SQLDatabase


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "chinook.db")


def get_database():
    return SQLDatabase.from_uri(
        f"sqlite:///{DB_PATH}",
        sample_rows_in_table_info=3,
    )
