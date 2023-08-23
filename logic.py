from data_base import check_data, write_json
from utils import page_print, all_pages

contact_in_one_page: int = 3


def start_menu(command: int) -> None:
    """
    This function is designed to implement the functionality of the program
    :param command: int
    """
    if command == 1:
        show_contact()
    elif command == 2:
        add_new_contact()
    elif command == 3:
        change_contact()
    elif command == 4:
        search()
    else:
        print('Введена некорректная команда, повторите попытку')


def show_contact() -> None:
    """
    Contact display function
    """
    database: list[dict] = check_data()
    if not database:
        print('У вас нет контактов')
        return
    all_page: int = all_pages(database, contact_in_one_page)
    page: int = 1
    page_print(database, contact_in_one_page, all_page, page)
    while True:
        command: int = int(input('Выберете команду из доступных (1-4)\n'
                                 '1.Следующая страница\n'
                                 '2.Предыдущая страница\n'
                                 '3.Ввести номер страницы\n'
                                 '4.Выход в меню\n'))
        if command == 1:
            if page == all_page:
                page = 1
            else:
                page += 1
            page_print(database, contact_in_one_page, all_page, page)
        elif command == 2:
            if page == 1 or all_page == 1:
                page = all_page
            else:
                page -= 1
            page_print(database, contact_in_one_page, all_page, page)
        elif command == 3:
            page = int(input(f'Введите номер старницы (1 - {all_page}): '))
            if page <= 0 or page > all_page:
                print('Такой страницы не сущетсвует')
            else:
                page_print(database, contact_in_one_page, all_page, page)
        elif command == 4:
            return
        else:
            print('Введена некорректная команда, повторите попытку')


def add_new_contact(index: int | None = None) -> None:
    """
    The function of adding new contacts
    :param index: index of the item in the list
    """
    surname: str = input('Введите фамилию: ')
    name: str = input('Введите имя: ')
    middle_name: str = input('Введите отчество: ')
    company_name: str = input('Введите название компании: ')
    work_phone_number: str = input('Введите рабочий телефон: ')
    personal_phone_number: str = input('Введите личный телефон (сотовый): ')
    database: list[dict] = check_data()
    if index is None:
        new_contact: dict[str, str] = {
            'surname': surname,
            'name': name,
            'middle_name': middle_name,
            'company_name': company_name,
            'work_phone_number': work_phone_number,
            'personal_phone_number': personal_phone_number
        }
        database.append(new_contact)
    else:
        replaced_contact: dict[str, str] = {
            'surname': surname if surname else database[index]['surname'],
            'name': name if name else database[index]['name'],
            'middle_name': middle_name if middle_name else database[index]['middle_name'],
            'company_name': company_name if company_name else database[index]['company_name'],
            'work_phone_number': work_phone_number if work_phone_number else database[index]['work_phone_number'],
            'personal_phone_number': personal_phone_number if personal_phone_number else database[index][
                'personal_phone_number']
        }
        database.pop(index)
        database.insert(index, replaced_contact)
    write_json(database)
    print('Контакт успешно добавлен' if index is None else 'Контакт успешно изменен')


def change_contact() -> None:
    """
    Function for deleting and changing entries in the directory
    """
    database: list[dict] = check_data()
    if not database:
        print('У вас нет контактов')
        return
    command: int = int(input('Выберете команду из доступных (1-2)\n'
                             '1.Изменить данные о контакте\n'
                             '2.Удалить контакт\n'))
    number: int = int(input('Введите порядковый номер контакта: '))
    if number not in range(1, len(database) + 1):
        print('Введен некорректный номер')
        return
    if command == 1:
        print('Введите только те значения, которые хотите изменить!')
        add_new_contact(number - 1)
    elif command == 2:
        database.pop(number - 1)
        write_json(database)
        print('Контакт удален')
    else:
        print('Введена некорректная команда, повторите попытку')


def search() -> None:
    """
    The function of searching for contacts according to the specified criteria
    """
    database: list[dict] = check_data()
    if not database:
        print('У вас нет контактов')
        return
    surname: str = input('Введите фамилию или оставьте пустую строку: ')
    name: str = input('Введите имя или оставьте пустую строку: ')
    middle_name: str = input('Введите отчество или оставьте пустую строку: ')
    company_name: str = input('Введите название компании или оставьте пустую строку: ')
    work_phone_number: str = input('Введите рабочий телефон или оставьте пустую строку: ')
    personal_phone_number: str = input('Введите личный телефон (сотовый) или оставьте пустую строку: ')

    result: list[dict] = []
    data_search: dict[str, str] = {}

    if surname:
        data_search['surname'] = surname
    if name:
        data_search['name'] = name
    if middle_name:
        data_search['middle_name'] = middle_name
    if company_name:
        data_search['company_name'] = company_name
    if work_phone_number:
        data_search['work_phone_number'] = work_phone_number
    if personal_phone_number:
        data_search['personal_phone_number'] = personal_phone_number

    for contact in database:
        coincidence: int = 0  # совпадения
        for key in data_search:
            if contact[key] == data_search[key]:
                coincidence += 1
        if coincidence == len(data_search):
            result.append(contact)
    if len(result) == 0:
        print('Контакты не найдены')
        return
    print(f'Найденно контактов: {len(result)}')
    all_page: int = all_pages(result, contact_in_one_page)
    for i in range(1, all_page + 1):
        page_print(result, contact_in_one_page, all_page, i)
