import json
import os


def create_database() -> None:
    """
    Function for creating a data file
    """
    with os.scandir('.') as entries:
        for entry in entries:
            if entry.name == 'phone_directory.json':
                return
    file = open('phone_directory.json', 'w')
    file.close()


def check_data() -> list:
    """
    Function for checking the presence of a data file
    :return: contact list
    """
    with open('phone_directory.json', 'r', encoding='utf-8') as data:
        try:
            database: list[dict] = json.load(data)
        except json.decoder.JSONDecodeError:
            return []
        return database


def write_json(database: list[dict]) -> None:
    """
    Function for recording data
    :param database: contact list
    """
    with open('phone_directory.json', 'w', encoding='utf-8') as data:
        json.dump(database, data, indent=2, ensure_ascii=False)
