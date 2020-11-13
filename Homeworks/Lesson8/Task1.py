"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    date_separator = "-"

    def __init__(self, date: str):
        self.date_str = date

    @classmethod
    def split_date(cls, date_str):
        """
        Разбивает дату на части

        :param date_str: дата
        :return: части в виде списка
        """
        return [int(val) for val in date_str.split(cls.date_separator)]

    @staticmethod
    def validate_date(date_list):
        """
        Проверяет корректность частей даты

        :param date_list: список частей
        :return: -
        """
        day, month, year = date_list
        if day < 1 or day > 31:
            print("Некорректный день")
        elif month < 1 or month > 12:
            print("Некорректный месяц")
        elif year < 1900 or year > 2020:
            print("Некорректный год")
        else:
            print("Дата корректна")


cur_date = Date("13-11-2020")

print(Date.split_date("12-11-2020"))
print(cur_date.split_date("13-11-2020"))
Date.validate_date(cur_date.split_date("13-11-2021"))
