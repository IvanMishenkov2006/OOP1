class Oleg:
    def __init__(self, values):#Инициализация класса с параметром values
        self.values = values

    def add(self, other):#Метод сложения
        if isinstance(other, int):#Если other является целым числом
            return Oleg([x + other for x in self.values])#Возвращает новый объект Oleg с измененными значениями
        elif isinstance(other, Oleg) and len(self.values) == len(other.values):#Если other является объектом Oleg и длина значений совпадает
            return Oleg([x + y for x, y in zip(self.values, other.values)])#Возвращает новый объект Oleg с измененными значениями
        else:
            raise ValueError("Сложение не поддерживается для этих типов или векторы имеют разную длину.")

    def mul(self, other):#Метод умножения
        if isinstance(other, int):  # если other является целым числом
            return Oleg([x * other for x in self.values])#Возвращает новый объект Oleg с измененными значениями
        elif isinstance(other, Oleg) and len(self.values) == len(other.values):#Если other является объектом Oleg и длина значений совпадает
            return Oleg([x * y for x, y in zip(self.values, other.values)])#Возвращает новый объект Oleg с измененными значениями
        else:
            raise ValueError("Умножение не поддерживается для этих типов или векторы имеют разную длину.")

    def str(self):#Преобразование в строку
        if len(self.values) == 0:
            return "Пустой вектор"#Возвращает строку "Пустой вектор"
        else:
            return str(self.values)

#Создание экземпляров класса Oleg
O1 = Oleg([1, 2, 3])
O2 = Oleg([4, 5, 6])

# Сложение векторов
result = O1 + O2

# Умножение вектора на число
result = O1 * 2
result2 = O2 * 4
#Вывод результатов
print(result)
print(result2)