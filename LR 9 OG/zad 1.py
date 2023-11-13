class Rectangle:
    def __init__(self, a, b):
        self.a = a  # Присваиваем значение 'a' переменной экземпляра 'a'
        self.b = b  # Присваиваем значение 'b' переменной экземпляра 'b'

    def get_area(self):  # Метод для вычисления площади прямоугольника
        return self.a * self.b  # Возвращаем вычисленную площадь

class Square:
    def __init__(self, a):
        self.a = a  # Присваиваем значение 'a' переменной экземпляра 'a'

    def get_area(self):  # Метод для вычисления площади квадрата
        return self.a ** 2  # Возвращаем вычисленную площадь

class Circle:
    def __init__(self, r):
        self.r = r  # Присваиваем значение 'r' переменной экземпляра 'r'

    def get_area(self):  # Метод для вычисления площади круга
        return 3.14 * self.r ** 2  # Возвращаем вычисленную площадь

# Создаем экземпляры классов
rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 3)
sq1 = Square(2)
cirl = Circle(3)

# Сохраняем экземпляры в списке
figures = [rect1, rect2, sq1, cirl]

# Проходим по каждой фигуре и вычисляем ее площадь
for figure in figures:
    print(figure.get_area())  # Выводим площадь каждой фигуры