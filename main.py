# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_menu():
    menu = { \
        '11': 'информация о системе', \
        '21': 'создать папку', \
        '22': 'удалить (файл/папку)', \
        '23': 'копировать (файл/папку)', \
        '24': 'просмотр содержимого директории', \
        '25': 'посмотреть только папки', \
        '26': 'посмотреть только файлы', \
        '27': 'смена рабочей директории', \
        '31': 'играть в викторину', \
        '32': 'мой банковский счет', \
        '33': 'информация по ip-адресу', \
        '34': 'справка Markdown (смс на Telegram)', \
        '35': 'создатель программы (Info)', \
        '00': 'выход.' \
        }

    title = ' МЕНЮ '
    max_str = int((max((len(v)) for v in menu.values()) + 4 - len(title)) / 2)
    print('=' * max_str, title, '=' * max_str)
    for key, val in menu.items():
        print(f'{key}. {val}')
    print('-' * (max_str * 2 + len(title) + 2))
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
