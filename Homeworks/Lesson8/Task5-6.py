"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
import Homeworks.Lesson8.Task4 as t


def select_office():
    """
    Запрос к пользователю на выбор офиса

    :return: индекс офиса (1 илил 2)
    """
    all_ok = False
    office_idx = 0
    while not all_ok:
        office_idx = t.int_safeinput("Выберите офис (1 - RnD, 2 - бухгалтерия): ")
        if office_idx not in [1, 2]:
            print("Ошибка! Повторите ввод")
        else:
            all_ok = True
    return office_idx


warehouse = t.Location("Склад", "Ленина 10 к1")
offices = {
    1: t.Location("RnD", "Ленина 10 к2"),
    2: t.Location("Бухгалтерия", "Ленина 10 к3")
}

equipment_classes = {
    1: t.Printer,
    2: t.Scanner,
    3: t.Copier
}

while True:
    print(
        "Выберите действие:\n1 - принять оргтехнику на склад\n2 - передать оргтехнику в офис\n\
3 - просмотр техники на складе\n4 - просмотр техники в офисах\n0 - выход")
    choice = t.int_safeinput("")

    if choice == 0:
        break

    if choice == 1:
        item_type = t.int_safeinput("Укажите тип техники (1 - принтеры, 2 - сканеры, 3 - ксероксы): ")
        brand = input("Укажите марку: ")
        qty = t.int_safeinput("Укажите размер партии: ")
        year = t.int_safeinput("Укажите год выпуска: ")

        nums = []
        while True:
            nums = input("Введите серийные номера через пробел: ").split()
            if len(nums) == qty:
                break
            else:
                print("Ошибка при вводе серийных номеров. Повторите ввод.")
        idx = 0
        while idx < qty:
            warehouse.accept(equipment_classes[item_type](year, brand, nums[idx]))
            idx += 1
        print("Техника успешно принята на склад!\n")

    if choice == 2:
        office = select_office()
        item_type = t.int_safeinput("Укажите тип техники (1 - принтеры, 2 - сканеры, 3 - ксероксы): ")
        warehouse.print_equip_type(item_type)
        ser_num = input("Введите серийный номер: ")
        item = warehouse.remove(item_type, ser_num)
        offices[office].accept(item)
        print("Перевод техники произведен!\n")

    if choice == 3:
        warehouse.print_content()

    if choice == 4:
        offices[select_office()].print_content()
