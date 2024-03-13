from math import pi, sqrt


# Для добавления новой фигуры необходимо создать класс, описывающий эту фигуру


class Figures:
    pass


class Circle(Figures):
    type = 'Круг'
    variables = ['R']

    def __init__(self, args):
        try:
            self.R, *_ = [abs(int(a)) for a in args]  # если приходит отрицательное число, делаем его положительным
        except ValueError:
            print('Неправильный ввод, требуется ввести одно целое число')
            exit()

    def calculate(self):
        return pi * self.R ** 2


class Triangle(Figures):
    type = 'Треугльник'
    variables = ['a', 'b', 'c']

    def __init__(self, args):
        try:
            self.a, self.b, self.c = [abs(int(a)) for a in args]
        except ValueError:
            print('Неправильный ввод, требуется ввести три целых числа через пробел')
            exit()

    def calculate(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def check_right_angled(self):
        max_var = max(self.a, self.b, self.c)
        other = list([var for var in [self.a, self.b, self.c] if var != max_var])
        if len(other) != 2:
            return 'Треугольник не прямоугольный'
        if max_var ** 2 == other[0] ** 2 + other[1] ** 2:
            return 'Треугольник прямоугольный'
        return 'Треугольник не прямоугольный'
