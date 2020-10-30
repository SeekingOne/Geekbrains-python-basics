"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

nums = input("Введите числа через пробел: ")
try:
    with open("Nums.txt", "w") as file_obj:
        file_obj.write(nums)

    with open("Nums.txt", "r") as file_obj:
        nums_list = file_obj.read().split()
except IOError as e:
    print(f'Ошибка работы с файлом: {str(e)}')
    nums_list = []

sum_total = 0
for num_str in nums_list:
    try:
        sum_total += float(num_str)
    except ValueError:
        pass

print("Сумма: ", sum_total)
