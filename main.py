from logic import start_menu
from data_base import create_database

while True:
    create_database()
    command: int = int(input('Выберете команду из доступных (1-5):\n'
                             '1.Вывести список контактов\n'
                             '2.Добавление новой записи в справочник\n'
                             '3.Редактирование записей в справочнике\n'
                             '4.Поиск записей\n'
                             '5.Выход\n'))
    if command == 5:
        break
    start_menu(command)
