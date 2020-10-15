"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
base_num = int(input('Введите целое число: '))

recurring_num = base_num
max_digit = base_num % 10

current_digit: int = 0

while (recurring_num // 10) > 0:
    recurring_num = recurring_num // 10
    current_digit = recurring_num % 10
    if current_digit > max_digit:
        max_digit = current_digit

print("Наибольшая цифра во введенном числе:", max_digit)