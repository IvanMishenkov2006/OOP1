# Определение класса "Трапеция"
class Trapezoid:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def calculate_perimeter(self):  # Метод для вычисления периметра трапеции
        return self.side1 + self.side2 + self.side3 + self.side4


# Определение класса "Ромб"
class Rhombus:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):  # Метод для вычисления периметра ромба
        return 4 * self.side

# Определение класса "Прямоугольник"
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):  # Метод для вычисления периметра прямоугольника
        return 2 * (self.width + self.height)

# Основная функция
def main():
    # Создание экземпляров объектов различных фигур
    trapezoid = Trapezoid(3, 6, 5, 5)
    rhombus = Rhombus(6)
    rectangle = Rectangle(3, 6)

    shapes = [trapezoid, rhombus, rectangle]  # Список фигур

    for shape in shapes:  # Итерация по списку фигур
        print(f"Периметр фигуры: {shape.calculate_perimeter()}")  # Вывод периметра каждой фигуры

if __name__ == "__main__":
    main()