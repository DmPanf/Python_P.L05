"""
    написать тесты для каждой ""чистой"" функции
    попробовать написать тесты для ""грязных"" функций, например копирования файла/папки, ...
"""

from os_info import os_info
from personal_bank import bank_balance, average_check


def test_os_info():
    assert os_info() == "linux" or os_info() == "linux2"


def test_bank_balance():
    assert bank_balance(0) == '💰 Остаток на счету: 0'
    assert bank_balance(125) == '💰 Остаток на счету: 125'


def test_average_check():
    assert average_check({}) == 'Еще не было покупок!', 'Нет истории еще'
    assert average_check({'tools': 50.0, 'tv': 30.0}) == '🛒Средний чек = 40.0'
    assert average_check({'books': 150.0}) == '🛒Средний чек = 150.0'

