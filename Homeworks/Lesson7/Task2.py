"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothing(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_needed(self):
        pass


class Suit(Clothing):

    def __init__(self, name, height):
        super().__init__(name)
        self.H = height

    @property
    def fabric_needed(self):
        return self.H * 2 + 0.3


class Coat(Clothing):

    def __init__(self, name, size):
        super().__init__(name)
        self.V = size

    @property
    def fabric_needed(self):
        return self.V / 6.5 + 0.5


if __name__ == "__main__":
    my_suit = Suit("офисный костюм", 1.7)
    my_coat = Coat("осеннее пальто", 50)

    print(f"Расход ткани на {my_suit.name} составляет {my_suit.fabric_needed} м.")
    print(f"Расход ткани на {my_coat.name} составляет {my_coat.fabric_needed} м.")
    print(f"Общий расход ткани: {my_coat.fabric_needed + my_suit.fabric_needed} м.")
