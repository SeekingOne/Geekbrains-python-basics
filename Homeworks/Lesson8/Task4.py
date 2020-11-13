"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""

equipment_keys = {
    1: "Принтеры",
    2: "Сканеры",
    3: "Ксероксы"
}


class Location:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self._equipment = {
            "Принтеры": {},
            "Сканеры": {},
            "Ксероксы": {}
        }

    def accept(self, item):
        """
        Принятие оборудования на баланс подразделения

        :param item: Объект оргтехники
        :return: -
        """
        item_type, ser_num, machine = item.get_key_data()
        self._equipment[item_type][ser_num] = machine

    def remove(self, equip_type, ser_num):
        """
        Снятие оборудования с баланса подразделения

        :param equip_type: тип оборудования
        :param ser_num: серийный номер
        :return: снятый объект
        """
        key = equipment_keys[equip_type]
        return self._equipment[key].pop(ser_num)

    def print_content(self):
        """
        Распечатка всей техники на балансе подразделения

        :return: -
        """
        print(f"{self.name} по адресу {self.location}")
        print("---------------------------------------")
        for key in self._equipment.keys():
            print(f"{key}: {len(self._equipment[key])} штук")
            for _, item in self._equipment[key].items():
                print(item)
        print("")

    def print_equip_type(self, equip_type):
        """
        Распечатка одного типа оборудования на балансе

        :param equip_type:
        :return:
        """
        key = equipment_keys[equip_type]
        print(f"В наличии - {key}: {len(self._equipment[key])} штук")
        for _, item in self._equipment[key].items():
            print(item)
        print("")


class OfficeEquipment:

    def __init__(self, year, brand, serial_num, item_type):
        self._manufactured = year
        self._brand = brand
        self._serial_num = serial_num
        self._type = item_type

    def __str__(self):
        """
        возвращает объект в строковом виде для печати

        :return: строка
        """
        return f"{self._brand}, серийный номер {self._serial_num}, произведен в {self._manufactured} году."

    def get_key_data(self):
        """
        Возвращает список из объекта и его ключевых данных: типа и серийного номера

        :return: список
        """
        return [self._type, self._serial_num, self]


class Printer(OfficeEquipment):
    def __init__(self, year, brand, serial_num):
        super().__init__(year, brand, serial_num, "Принтеры")


class Scanner(OfficeEquipment):
    def __init__(self, year, brand, serial_num):
        super().__init__(year, brand, serial_num, "Сканеры")


class Copier(OfficeEquipment):
    def __init__(self, year, brand, serial_num):
        super().__init__(year, brand, serial_num, "Ксероксы")


def accept_to_wh(warehouse: Location, equipment):
    for item in equipment:
        warehouse.accept(item)


def int_safeinput(prompt):
    """
    Запрос пользователю на ввод целого числа с обработкой ошибки ввода

    :param prompt: Сообщение пользователю
    :return: введенное число или 0
    """
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input!")
        return 0
