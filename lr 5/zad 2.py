import math
class Vector:
    def __init__(self, x, y):    # Конструктор класса, принимающий две координаты вектора (x и y)
        self.x = x
        self.y = y
    def calculate_magnitude(self):    # Метод для вычисления модуля вектора
         return math.sqrt(self.x**2 + self.y**2)
    def multiply_by_constant(self, k):
        return Vector(k*self.x, k*self.y)# Метод для умножения вектора на константу
v = Vector(3, 4)# Содание объекта класса Vector с координатами (3, 4)
magnitude = v.calculate_magnitude()# Вызов метода calculate_magnitude() для объекта v и вывод результата
print(f'|вектор| = {magnitude} (f’|вектор|=sqrt({v.x}^2 + {v.y}^2)')
k = 2# Вызов метода multiply_by_constant() для объекта v с константой k=2 и вывод результата
result_vector = v.multiply_by_constant(k)
print(f'{k}*|вектор| = ({result_vector.x}, {result_vector.y}) (f’{k}*|вектор| = ({k}*{v.x}, {k}*{v.y})')