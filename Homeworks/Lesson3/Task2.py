"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def print_user(**kwargs):
    data_string = ""
    for property, value in kwargs.items():
        data_string += f"{property}: {value}; "
    print(data_string)

print_user(name = "Вася", surname = "Петров", birth_year = 2000, \
           home_town = "Урюпинск", email = "vasya@mail.ru", phone = "+7 777 8889900")