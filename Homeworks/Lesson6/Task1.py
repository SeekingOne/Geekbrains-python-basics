"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    __colour_timings = [
        ("Красный", 7),
        ("Зеленый", 14),
        ("Желтый", 2)
    ]
    __current_colour = 0

    def __set_next_colour(self):
        self.__current_colour = (self.__current_colour + 1) % 3

    def running(self):
        start_time = time.time()
        print(self.__colour_timings[self.__current_colour][0])
        while True:
            if time.time() - start_time >= self.__colour_timings[self.__current_colour][1]:
                self.__set_next_colour()
                start_time = time.time()
                print(self.__colour_timings[self.__current_colour][0])


tl = TrafficLight()

tl.running()
