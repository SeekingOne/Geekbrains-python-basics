"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
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

def sort_desc(*args):
    """
    Пузырьковая сортировка списка аргументов (по убыванию)

    :param args: произвольный список аргументов
    :return: отсортированный список
    """
    sorted_list = list(args)
    change_made = True
    num_items = len(sorted_list)
    while change_made:
        idx = 1
        change_made = False
        while idx < num_items:
            if sorted_list[idx - 1] < sorted_list[idx]:
                sorted_list[idx - 1], sorted_list[idx] = sorted_list[idx], sorted_list[idx - 1]
                change_made = True
            idx += 1

    return sorted_list

def my_func(a, b, c):
    """
    Функция суммирует два наибольших аргумента из трех полученных

    :param a: числовой аргумент
    :param b: числовой аргумент
    :param с: числовой аргумент
    :return: сумма
    """
    sorted_args = sort_desc(a, b, c)
    return f"{sorted_args[0]} + {sorted_args[1]} = {sorted_args[0] + sorted_args[1]}"

val_1 = num_safeinput("Enter value 1: ")
val_2 = num_safeinput("Enter value 2: ")
val_3 = num_safeinput("Enter value 3: ")

print(my_func(val_1, val_2, val_3))
