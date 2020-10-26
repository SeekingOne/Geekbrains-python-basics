"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def calc_payout(p_hours, p_hourly_salary, p_bonus):
    """
    Расчет ЗП сотрудника

    :param p_hours: Выработка в часах
    :param p_hourly_salary: Ставка в час
    :param p_bonus: Премия
    :return: ЗП
    """
    try:
        return int(p_hours) * float(p_hourly_salary) + float(p_bonus)
    except ValueError:
        print("Неверные данные для расчета!")
        return 0.0


try:
    script_name, hours, salary, bonus = argv
    print("Зарплата сотрудника: ", calc_payout(hours, salary, bonus))
except ValueError:
    print("Неверные параметры скрипта!")
