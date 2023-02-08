# Main Menu
#from PIL import Image, ImageFont, ImageDraw
from info import print_logo
import os

menu = {'11': 'информация о системе', \
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


def stop_menu():
    print('😎 До скорой встречи!')
    return False


def print_menu():
    title = ' МЕНЮ '
    max_str = int((max((len(v)) for v in menu.values()) + 4 - len(title)) / 2)
    print('=' * max_str, title, '=' * max_str)
    for key, val in menu.items():
        print(f'{key}. {val}')
    print('-' * (max_str * 2 + len(title) + 2))
    return

def start_menu(ask=True):
    print_menu()
    while ask:
        item = input('... Ваш выбор: ')
        if item in menu.keys():
            if item == "00":
                ask = func_list(item)
            elif item == "11":
                func_list(item)
            elif item == "35":
                func_list(item)
            else:
                print('Ok')
        else:
            print(' 🚫 Ошибка выбора пункта меню!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
