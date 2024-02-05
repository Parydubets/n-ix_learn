import sys
from abc import ABC, abstractmethod
from math import sqrt

class Figure(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def calc_area(self):
        return self.a * self.b


class Square(Figure):
    def __init__(self, a):
        self.a = int(a)

    def calc_area(self):
        return self.a ** 2

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def calc_area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))



if sys.argv[1] == 'triangle':
    print("The ares is ", Triangle(sys.argv[2], sys.argv[3], sys.argv[4]).calc_area())
elif sys.argv[1] == 'rectangle':
    print("The ares is ", Rectangle(sys.argv[2], sys.argv[3]).calc_area())
elif sys.argv[1] == 'square':
    print("The ares is ", Square(sys.argv[2]).calc_area())
else:
    print("Wrong figure")