"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count
from itertools import cycle


def int_safeinput(prompt):
    """
    Запрос пользователю на ввод целого числа с обработкой ошибки ввода

    :param prompt: Сообщение пользователю
    :return: введенное число или 0
    """
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input!")
        return 0


def num_gen(start_val: int):
    """
    Функция, использующая итератор count() для генерации целых чисел 
    от указанного стартового значения до 15

    :param start_val: начало последовательности
    :return: последовательность
    """
    if start_val >= 15:
        return start_val
    for val in count(start_val):
        yield val
        if val == 15:
            break


def list_gen(base_list: list):
    """
    Функция, использующая итератор cycle() для повторения списка 3 раза

    :param base_list: базовый список
    :return: троекратно повторенная последовательность элементов полученного списка
    """
    counter = 0
    list_len = len(base_list)
    for val in cycle(base_list):
        yield val
        counter += 1
        if counter // list_len == 3:
            break


init_val = int_safeinput("Введите начало последовательности: ")
print(list(num_gen(init_val)))

start_list = input("Введите элементы списка через пробел: ").split()
print(list(list_gen(start_list)))
