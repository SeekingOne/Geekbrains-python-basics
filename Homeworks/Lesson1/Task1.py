"""
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""
oper_add = "сложение"
oper_mult = "умножение"
invite = "Укажите операцию ('" + oper_add + "' или '" + oper_mult + "'):"

selected_oper = input(invite + '\n>>>: ')
arg1 = input('Введите первое число: ')
arg2 = input('Введите второе число: ')

if selected_oper == oper_add:
    result = int(arg1) + int(arg2)
elif selected_oper == oper_mult:
    result = int(arg1) * int(arg2)
else:
    result = "операция указана неверно"

print('Результат:', result)


