"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать
функцию input().
"""

test_list = []
idx = 0

print("Введите элементы списка. Введите 'Exit' для завершения ввода.")
while True:
    element = input(f"Элемент №{idx}: ")
    if element == "Exit":
        idx -= 1
        break
    else:
        test_list.append(element)
        idx += 1

print ("Исходный список:\n", test_list)

iterator = 1

while iterator <= idx:
    prev_element = test_list[iterator - 1]
    cur_element = test_list[iterator]
    test_list[iterator - 1] = cur_element
    test_list[iterator] = prev_element
    iterator += 2

print ("Обработанный список:\n", test_list)

