"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def custom_range(rng_start: int, rng_end: int, rng_step: int = 1):
    """
    Генератор диапазона целых чисел.

    :param rng_start: начало диапазона
    :param rng_end: конец диапазона
    :param rng_step: шаг
    :return: диапазон
    """
    idx = rng_start
    while idx < rng_end:
        yield idx
        idx += rng_step


def custom_reduce(reducer_func, list_obj: list):
    """
    Редуктор, сводящий список к одному значению с помощью полученной функции двух аргументов.

    :param reducer_func: функция
    :param list_obj: исходный список
    :return: значение
    """
    list_len = len(list_obj)
    if list_len == 0:
        return 0
    elif list_len == 1:
        return list_obj[0]

    result = reducer_func(list_obj[0], list_obj[1])
    idx = 2
    while idx < list_len:
        result = reducer_func(result, list_obj[idx])
        idx += 1
    return result


even_list = [val for val in custom_range(100, 1001) if not val & 1]
print("Четные числа в диапазоне 100-1000:\n", even_list)

print("Результат с самопальной функцией reduce:\n", custom_reduce(lambda x, y: x * y, even_list))
print("Результат с функцией reduce из functools:\n", reduce(lambda x, y: x * y, even_list))
