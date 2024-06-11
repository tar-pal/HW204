from add_numbers import adding
import pytest

def test_adding():
    # Перевірка додавання додатних чисел
    assert adding(3, 5) == 8

    # Перевірка додавання від'ємних чисел
    assert adding(-2, -3) == -5

    # Перевірка додавання додатнього та від'ємного чисел
    assert adding(5, -3) == 2

    # Перевірка додавання нуля
    assert adding(0, 7) == 7

    # Перевірка додавання до нуля
    assert adding(10, 0) == 10



if __name__ == "__main__":
    test_adding()
#     print("Всі тести пройдено успішно!")