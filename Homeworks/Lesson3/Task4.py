"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def num_safeinput(prompt, type=float):
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

def custom_pow(x, y):
    """
    Возведение в степень с оператором **

    :param x: основание степени
    :param y: показатель степени
    :return: x в степени y
    """
    try:
        return x ** y
    except TypeError:
        print("Invalid arguments!")
        return 0.0

def custom_pow_2(x, y):
    """
    Возведение в степень с помощью цикла

    :param x: основание степени (float)
    :param y: показатель степени (int)
    :return: x в степени y
    """
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print("Неверные аргументы!")
        return 0.0

    negative_power = False
    if y < 0:
        power = y * -1
        negative_power = True
    else:
        power = y

    idx = 1
    result = 1

    while idx <= power:
        result *= x
        idx += 1
    if negative_power:
        result = 1 / result

    return result

val_1 = num_safeinput("Введите действительное положительное число: ")
if val_1 < 0:
    val_1 *= -1
    print(f"Неверный знак! Ввод исправлен на: {val_1}")
elif val_1 == 0:
    val_1 = 1
    print(f"Неверное число! Ввод исправлен на: {val_1}")

val_2 = num_safeinput("Введите целый отрицательный показатель степени: ", int)
if val_2 > 0:
    val_2 *= -1
    print(f"Неверный знак! Ввод исправлен на: {val_2}")
elif val_2 == 0:
    val_2 = -1
    print(f"Неверное число! Ввод исправлен на: {val_2}")

print("Степень с оператором **:\n", custom_pow(val_1, val_2))
print("Степень с циклом:\n",custom_pow_2(val_1, val_2))
