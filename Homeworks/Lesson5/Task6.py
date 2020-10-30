"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def get_number(src_str: str):
    """
    Извлекает число из строки вида: 100(л)

    :param src_str: строка, содержащая число
    :return: извлеченное число
    """
    try:
        # return int(src_str[0:src_str.find("(")])
        return int(src_str.split("(")[0])
    except ValueError:
        return 0


dict_subjects = {}
idx = 0
try:
    with open("Curriculum.txt", "r", encoding="utf-8") as file_obj:
        for txt_line in file_obj:
            idx += 1
            subject = txt_line.split()
            if len(subject) == 4:
                sum_hours = get_number(subject[1]) + \
                            get_number(subject[2]) + \
                            get_number(subject[3])
                dict_subjects[subject[0][0:subject[0].find(":")]] = sum_hours
            else:
                print("Неверный формат данных в строке", idx)
except IOError as e:
    print(f'Ошибка работы с файлом: {str(e)}')

print("\n", dict_subjects)
