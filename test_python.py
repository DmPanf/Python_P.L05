"""
    В модуле написать тесты для встроенных функций filter, map, sorted,
    а также для функций из библиотеки math:
    pi, sqrt, pow, hypot.
    Чем больше тестов на каждую функцию - тем лучше
"""

import math


def test_filter():
    assert list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])) == [2, 4, 6]
    assert list(filter(lambda x: x.startswith('a'), ['apple', 'banana', 'avocado'])) == ['apple', 'avocado']


def test_map():
    assert list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])) == [1, 4, 9, 16, 25]
    assert list(map(lambda x: x.upper(), ['apple', 'banana', 'avocado'])) == ['APPLE', 'BANANA', 'AVOCADO']


def test_sorted():
    assert sorted([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]
    assert sorted(['apple', 'banana', 'avocado'], key=lambda x: len(x)) == ['apple', 'banana', 'avocado']


def test_pi():
    assert math.isclose(math.pi, 3.141592653589793, rel_tol=1e-9)


def test_sqrt():
    assert math.isclose(math.sqrt(2), 1.4142135623730951, rel_tol=1e-9)


def test_pow():
    assert math.isclose(math.pow(2, 3), 8, rel_tol=1e-9)


def test_hypot():
    assert math.isclose(math.hypot(3, 4), 5, rel_tol=1e-9)
