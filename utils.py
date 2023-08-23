from data_base import check_data
import math


def page_print(database: list[dict], contact_in_one_page: int, all_page: int, page: int) -> None:
    """
    Function for beautiful page display
    :param database: Contact list
    :param contact_in_one_page: Number of contacts on one page
    :param all_page: Total pages
    :param page: page number
    """
    phone_directory: list[dict] = check_data()  # для отображения порядкового номера контакта в файле
    start: int = contact_in_one_page * (page - 1)
    end: int = start + contact_in_one_page
    print(f'Страница {page} из {all_page}')
    print('=' * 25)
    for contact in database[start:end]:
        print(f'Контакт номер - {phone_directory.index(contact) + 1}')
        for key, value in contact.items():
            if not value:
                value = 'Данные отсутсвуют'
            print(f"{key}: {value} ")
        print('-' * 25)
    print('=' * 25)


def all_pages(database: list[dict], contact_in_one_page: int) -> int:
    """
    Function for counting all pages
    :param database: Contact list
    :param contact_in_one_page: Number of contacts on one pageint
    :return: Total pages
    """
    all_page: int = math.ceil(len(database) / contact_in_one_page) if math.ceil(
        len(database) / contact_in_one_page) != 0 else 1
    return all_page
