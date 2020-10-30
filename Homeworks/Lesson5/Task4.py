"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

eng_ru_dict = {
    "Zero": "Ноль",
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять"
}

translated_list = []
try:
    with open("Eng Nums.txt", "r", encoding="utf-8") as file_obj:
        for txt_line in file_obj:
            trans_line = txt_line.split()
            trans_line[0] = eng_ru_dict[trans_line[0]]
            translated_list.append(" ".join(trans_line))

    print(translated_list)

    with open("Ru Nums.txt", "w", encoding="utf-8") as file_obj:
        for txt_line in translated_list:
            file_obj.write(txt_line + "\n")
except IOError as e:
    print(f'Ошибка работы с файлом: {str(e)}')
