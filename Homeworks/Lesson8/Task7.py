"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real_a: float, real_b: float):
        self.__real_a = real_a
        self.__real_b = real_b

    def __str__(self):
        """
        Комплексное число в строковой форме

        :return: строковая форма числа
        """
        if self.__real_b >= 0:
            imaginary = f" + {self.__real_b}i"
        else:
            imaginary = f" - {abs(self.__real_b)}i"
        return str(self.__real_a) + imaginary

    @property
    def real(self):
        return self.__real_a

    @property
    def other_real(self):
        return self.__real_b

    def __add__(self, other):
        """
        Сложение комплексного числа с комплексным или натуральным

        :param other: Complex или float
        :return: сумма (Complex)
        """
        if not isinstance(other, Complex):
            try:
                other_a = float(other)
            except ValueError:
                raise ValueError("Неверный операнд!")
            return Complex(self.__real_a + other_a, self.__real_b)
        else:
            return Complex(self.__real_a + other.real, self.__real_b + other.other_real)

    def __sub__(self, other):
        """
        Вычитание из комплексного числа другого комплексного или натурального

        :param other: Complex или float
        :return: разность (Complex)
        """
        if not isinstance(other, Complex):
            try:
                other_a = float(other)
            except ValueError:
                raise ValueError("Неверный операнд!")
            return Complex(self.__real_a - other_a, self.__real_b)
        else:
            return Complex(self.__real_a - other.real, self.__real_b - other.other_real)

    def __mul__(self, other):
        """
        Умножение комплексного числа на другое комплексное или натуральное
        :param other: Complex или float
        :return: произведение (Complex)
        """
        if not isinstance(other, Complex):
            try:
                other_a = float(other)
            except ValueError:
                raise ValueError("Неверный операнд!")
            second = Complex(other_a, 0)
        else:
            second = other

        return Complex((self.__real_a * second.real - self.__real_b * second.other_real),
                       (self.__real_b * second.real + self.__real_a * second.other_real))


if __name__ == "__main__":
    a = Complex(2, 3)
    b = Complex(-4.3, 2)
    c = Complex(6, -4)
    complex_sum = a + b
    complex_diff = a - c
    complex_prod = a * c

    print(a, b, c, sep='\n')
    print(f'({a}) + ({b}) = {complex_sum}')
    print(f'({a}) - ({c}) = {complex_diff}')
    print(f'({a}) * ({c}) = {complex_prod}')
