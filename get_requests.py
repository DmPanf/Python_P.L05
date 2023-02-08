# Включает две функции - информация по ip адресу и отправка фото-справки в Телеграм

import json
from requests import get

def get_ip():
    print('\nЗапрос по IP-адресу отправлен!\nОжидайте ...')
    url = 'https://api.ipify.org'
    ip = get(url).content.decode('utf8')
    ip_url = 'https://geolocation-db.com/jsonp/' + ip

    response = get(ip_url)
    res = response.content.decode()
    res = res.split("(")[1].strip(")")  # очистка лишних знаков
    res = json.loads(res)  # data -> dict
    for key, val in res.items():
        print('{:<12}: {:}'.format(key, val))
    return
