"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, colour, name, is_police):
        self.name = name
        self.colour = colour
        self.is_police = bool(is_police)
        self.speed = 0.0
        self.direction = "прямо"

    def accelerate_to(self, speed):
        """
        "Разгоняет" автомобиль до требуемой скорости

        :param speed: скорость
        :return: -
        """
        self.speed = speed

    def stop(self):
        """
        "Останавливает" автомобиль

        :return: -
        """
        self.speed = 0.0

    def turn(self, direction):
        """
        "Поворачивает" автомобиль в указанном направлении

        :param direction: направление
        :return: -
        """
        self.direction = str(direction)

    def show_speed(self):
        """
        Отображает текущую скорость автомобиля

        :return: -
        """
        if self.is_police:
            car_type_str = "Полицейский автомобиль"
        else:
            car_type_str = "Гражданский автомобиль"

        print(f"{car_type_str} марки {self.name} движется со скоростью: {self.speed}")


# TownCar, SportCar, WorkCar, PoliceCar.

class TownCar(Car):
    def __init__(self, colour):
        super().__init__(colour, "Mercedes Smart", False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение!")


class SportCar(Car):
    def __init__(self, colour):
        super().__init__(colour, "Subaru WRX STI", False)

    def show_speed(self):
        super().show_speed()
        if self.speed < 120:
            print("На такой машине нельзя тошнить! :)")


class WorkCar(Car):
    def __init__(self):
        self.load = 0.0
        super().__init__("оранжевый", "БелАЗ", False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение!")

    def loading(self, tons):
        self.load = tons


class PoliceCar(Car):
    def __init__(self):
        super().__init__("белый", "Ford", True)


t_car = TownCar("мокрый асфальт")
s_car = SportCar("синий")
w_car = WorkCar()
p_car_1 = PoliceCar()
p_car_2 = PoliceCar()

t_car.accelerate_to(55)
s_car.accelerate_to(100)

w_car.accelerate_to(45)
w_car.loading(15)

p_car_1.accelerate_to(90)
p_car_1.turn("направо")

p_car_2.accelerate_to(80)
p_car_2.turn("на восток")

t_car.show_speed()
t_car.turn("налево")
print(f"Городское авто цвета {t_car.colour} движется {t_car.direction} со скоростью {t_car.speed}")
t_car.accelerate_to(70)
t_car.show_speed()
print("\n")

s_car.show_speed()
print("\n")

print(f"Грузовик марки {w_car.name} цвета {w_car.colour} с загрузкой {w_car.load} тонн \
движется {w_car.direction} со скоростью {w_car.speed}")
print("\n")

p_car_1.show_speed()
print(f"Направление: {p_car_1.direction}")
p_car_2.show_speed()
print(f"Направление: {p_car_2.direction}")
