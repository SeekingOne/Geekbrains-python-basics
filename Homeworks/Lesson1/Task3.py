"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
base_num = int(input('Введите целое число от 0 до 9: '))

if base_num >= 0 and base_num <=9:
    second_num = base_num * 10 + base_num
    third_num = base_num * 100 + second_num

    str_expression = f"{base_num} + {second_num} + {third_num} = {base_num + second_num + third_num}"

    print('Результат:\n', str_expression)
else:
    print('Неверное число')
