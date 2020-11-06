"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print("Запуск отрисовки...")

class Pen(Stationery):
    def __init__(self):
        super().__init__("Ручка")
    def draw(self):
        super().draw()
        print(f"{self.name} проводит тонкую чернильную линию")

class Penсil(Stationery):
    def __init__(self):
        super().__init__("Карандаш")
    def draw(self):
        super().draw()
        print(f"{self.name} проводит тонкую графитовую линию")

class Marker(Stationery):
    def __init__(self):
        super().__init__("Маркер")
    def draw(self):
        super().draw()
        print(f"{self.name} проводит жирную линию")

my_pen = Pen()
my_pencil = Penсil()
my_marker = Marker()

my_pen.draw()
my_pencil.draw()
my_marker.draw()