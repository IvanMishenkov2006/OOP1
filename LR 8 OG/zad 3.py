class Quadrilateral:
    def __init__(self, width, height=None):
        if height is None:
            height = width
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == self.height:
            return f"Куб размером {self.width}х{self.height}"
        else:
            return f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        return self.width == self.height
quad1 = Quadrilateral(3)
print(quad1)  # Вывод: Куб размером 3х3
print(bool(quad1))  # Вывод: True

quad2 = Quadrilateral(3, 4)
print(quad2)#Вывод:Прямоугольник размером 3х4
print(bool(quad2))#Вывод:False