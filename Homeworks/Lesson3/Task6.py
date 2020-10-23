"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(string):
    """
    Делает первый символ строки string заглавным

    :param string: строка
    :return: строка, начинающася с заглавной буквы
    """
    return str(string).title()


def x_map(x_func, x_obj):
    """
    Генератор, применяет полученную функцию к каждому елементу итерируемого объекта

    :param x_func: функция
    :param x_obj: итерируемый объект
    :return: модифицированные элементы
    """
    result = []
    for val in x_obj:
        yield x_func(val)


words_list = list(x_map(int_func, input("Вводите слова через пробел: ").split()))

print(" ".join(words_list))
