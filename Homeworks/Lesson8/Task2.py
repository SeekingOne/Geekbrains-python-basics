"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDiv(Exception):
    def __init__(self, text):
        self.txt = text


def input_divider():
    """
    Ввод делителя с обработкой ошибки нуля
    :return: делитель
    """
    result = float(input("Введите делитель: "))
    if result == 0:
        raise MyZeroDiv("Делитель не может быть нулем!")
    return result


a = float(input("Введите делимое: "))
try:
    b = input_divider()
except MyZeroDiv as err:
    print(err)
    pass
else:
    print(f"Частное: {a / b}")
