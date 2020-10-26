"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""


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


print(list(val for val in custom_range(20, 240) if (val % 20 == 0 or val % 21 == 0)))
