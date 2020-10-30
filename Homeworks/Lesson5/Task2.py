"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

try:
    file_obj = open("PyTest.txt", "a")

    print("Введите текст построчно. Для завершения ввода нажмите Enter в пустой строке.")

    while True:
        txt_line = input()
        if txt_line == "":
            break
        file_obj.write(txt_line + "\n")

    file_obj.close()
except IOError as e:
    print(f'Ошибка работы с файлом: {str(e)}')

# Нужно закрыть и переоткрыть файл, чтобы вновь добавленные строки стали доступны для чтения
try:
    file_obj = open("PyTest.txt", "r")
    complete_text = file_obj.readlines()
    file_obj.close()
except IOError as e:
    print(f'Ошибка работы с файлом: {str(e)}')
    complete_text = []

print("\nЧисло строк в файле:", len(complete_text))

for idx, txt_line in enumerate(complete_text):
    word_count = 0
    word_separators = (" ", ",", ".", "!", "?", "\n")
    separator_found = True
    if len(txt_line) > 0:
        for letter in txt_line:
            if letter in word_separators:
                separator_found = True
            else:
                if separator_found:
                    separator_found = False
                    word_count += 1
    print(f"строка {idx + 1}: {word_count} слов(а)")
