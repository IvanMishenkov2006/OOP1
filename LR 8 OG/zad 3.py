class Quadrilateral:
    def __init__(self, width, height=None):#Инициализария объека класса Quadrilateral,принимаем ширину и высоту
        if height is None:#Если высота не указана, то это куб, высота = ширине
            height = width
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == self.height:#Если ширина равна высоте,тогда это куб
            return f"Куб размером {self.width}х{self.height}"
        else:#В ином случае это прямоугольник
            return f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):#Метод для проверки истинности объекта
        return self.width == self.height#Вернуть True, если ширина = высоте

quad1 = Quadrilateral(3)#Создаем куб
print(quad1)#Куб размером 3х3
print(bool(quad1))#Вывод True

quad2 = Quadrilateral(3, 4)#Создаем прямоугольник
print(quad2)#Прямоугольник размером 3х4
print(bool(quad2))#Вывод False