# Включает две функции - информация по ip адресу и отправка фото-справки в Телеграм
import json
import os
import gdown
import requests


def get_ip():
    print('\nЗапрос по IP-адресу отправлен!\nОжидайте ...')
    url = 'https://api.ipify.org'
    ip = requests.get(url).content.decode('utf8')
    ip_url = 'https://geolocation-db.com/jsonp/' + ip

    response = requests.get(ip_url)
    res = response.content.decode()
    res = res.split("(")[1].strip(")")  # очистка лишних знаков
    res = json.loads(res)  # data -> dict
    for key, val in res.items():
        print('{:<12}: {:}'.format(key, val))
    return


# Функция отправки фото из Google Colab в Telegram
def send_jpg(img, chat_id, token):
    url = 'https://api.telegram.org/bot'
    files = {'photo': open(img, 'rb')}
    resp = requests.post(f'{url}{token}/sendPhoto?chat_id={chat_id}', files=files)
    if resp.status_code == 400:
        print('\nДля первого раза надо инициировать Бота и повторить:')
        print('🌐 https://t.me/z4_mini_dl_na_bot <- нажать [ЗАПУСТИТЬ] или [START]')
        print('💡 узнать свой ID очень просто -> https://t.me/getmyid_bot')
    return resp


def send_photo():
    # Функция поиска шпаргалки на Markdown и отправки через send_photo(img, chat_id)
    markdown_file = 'markdown.jpg'
    jpg_link = 'https://raw.githubusercontent.com/dnp34/AI_CNN/main/Data/markdown.jpg'

    if not os.path.exists(markdown_file):
        gdown.download(jpg_link, None, quiet=True)

    j_file = 'env.json'
    if os.path.exists(j_file):
        with open(j_file) as f:  # загрузка файла
            data = json.load(f)
        token, chat_id = data.values()
        tgm_id = input('\nВведите свой Telegram ID: ')
        if len(tgm_id) < 2:
            tgm_id = chat_id
        print('\nНачалась отправка справки по Markdown ...')
        send_jpg(markdown_file, tgm_id, token)
    else:
        print('\nОтсутствует файл env.json с BOT_TOKEN!')
    return
