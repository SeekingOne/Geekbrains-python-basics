"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length = 0.0
    _width = 0.0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_demand(self, m2_pavement_mass, thickness):
        return self._length * self._width * m2_pavement_mass * thickness


moskva_petushki = Road(100000, 50)

print(moskva_petushki.calc_asphalt_demand(100,5))
