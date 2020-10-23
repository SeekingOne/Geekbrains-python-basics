"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def num_safeinput(prompt, type = float):
    """
    Запрос пользователю на ввод числа с обработкой ошибки ввода

    :param prompt: Сообщение пользователю
    :param type: числовой тип для введенного значения (int или float, по умолчанию float)
    :return: введенное число или 0
    """
    if type not in (int, float):
        print("Incorrect data type!")
        return 0.0

    try:
        return type(input(prompt))
    except ValueError:
        print("Invalid input!")
        return type(0)

def divide(a, b):
    """
    Деление двух чисел с обработкой ошибки деления на 0.

    :param a: делимое
    :param b: делитель
    :return: частное
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero!!!")
        return 0.0

val_a = num_safeinput("Input 1st value: ")
val_b = num_safeinput("input 2nd value: ")

print(divide(val_a, val_b))