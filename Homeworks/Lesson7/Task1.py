"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    values = []

    def __init__(self, values: list):
        self.values = values

    def __str__(self):
        """
        Возвращает матрицу в строковой форме для печати

        :return: матрица в виде строки
        """
        result = ""
        for line in self.values:
            for item in line:
                result += (str(item) + " ")
            result += "\n"
        return result

    def __add__(self, other):
        """
        Возвращает сумму двух матриц.
        Размерность матрицы-результата совпадает с размерностью аргумента слева.

        :param other: объект типа Matrix
        :return: объект-сумма
        """
        if not isinstance(other, Matrix):
            raise TypeError('Неверный тип оператора!')
        y_other = len(other.values)
        idx_y = 0
        sum_matrix = []
        for line in self.values:
            idx_x = 0
            sum_line = []
            if idx_y < y_other:
                x_other = len(other.values[idx_y])
            else:
                x_other = 0
            for item in line:
                if idx_x < x_other and idx_y < y_other:
                    sum_line.append(item + other.values[idx_y][idx_x])
                else:
                    sum_line.append(item)
                idx_x += 1
            sum_matrix.append(sum_line)
            idx_y += 1
        return Matrix(sum_matrix)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[10, 20, 30, 40], [50, 60, 70, 80]])

print(m1)
print(m2)
print(m1 + m2)
