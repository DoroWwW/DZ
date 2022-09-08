"""
Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух окружностей, вычитание
 радиусов произвести по модулю. Если вычитаются две окружности с одинаковым значением радиуса, то результатом 
 вычитания будет точка класса Point.
"""


import math


class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)