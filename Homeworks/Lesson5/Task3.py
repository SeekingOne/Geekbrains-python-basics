"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

try:
    file_obj = open("Staff.txt", "r", encoding="utf-8")

    staff_list = file_obj.readlines()
    file_obj.close()
except IOError as e:
    print(f'Ошибка работы с файлом: {str(e)}')
    staff_list = []

num_employees = len(staff_list)

undervalued_staff = []
total_salary = 0
for idx, txt_line in enumerate(staff_list):
    employee = txt_line.split()
    if len(employee) > 1:
        try:
            salary = float(employee[1])
            total_salary += salary
            if salary < 20000:
                undervalued_staff.append(employee)
        except ValueError:
            print(f"Некорректные данные в строке {idx + 1}!")
            salary = 0
            num_employees -= 1
    else:
        print(f"Некорректные данные в строке {idx + 1}!")
        num_employees -= 1

print("\nЧисло сотрудников:", num_employees)
print("Средний оклад:", total_salary / num_employees)
print("\nСотрудники с окладом менее 20 тыс. руб.:")

for employee in undervalued_staff:
    print(f"{employee[0]}, оклад: {employee[1]}")
