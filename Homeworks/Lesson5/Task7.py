"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

dict_firms = {}
idx = 0
num_profitable = 0
total_profit = 0.0
try:
    with open("Firms.txt", "r", encoding="utf-8") as file_obj:
        for txt_line in file_obj:
            idx += 1
            firm = txt_line.split()
            if len(firm) == 4:
                try:
                    profit = float(firm[2]) - float(firm[3])
                    if profit > 0:
                        num_profitable += 1
                        total_profit += profit
                    dict_firms[firm[0]] = profit
                except ValueError:
                    print("Ошибка данных в строке", idx)
            else:
                print("Неверный формат данных в строке", idx)
except IOError as e:
    print(f'Ошибка работы с файлом: {str(e)}')

if num_profitable > 0:
    dict_avg_profit = {"average_profit": total_profit / num_profitable}
else:
    dict_avg_profit = {}
combined_data = [dict_firms, dict_avg_profit]

try:
    with open("Firms_data.json", "w") as file_obj:
        json.dump(combined_data, file_obj)
except IOError as e:
    print(f'Ошибка работы с файлом: {str(e)}')

print("\n", combined_data)
