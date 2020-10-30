"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

try:
    file_obj = open("PyTest.txt", "w")

    print("Введите текст построчно. Для завершения ввода нажмите Enter в пустой строке.")

    while True:
        txt_line = input()
        if txt_line == "":
            break
        file_obj.write(txt_line + "\n")

    file_obj.close()
except IOError as e:
    print(f'Ошибка работы с файлом: {str(e)}')
