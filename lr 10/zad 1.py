class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand#Бренд транспортного средства
        self.max_speed = max_speed# Максимальная скорость транспортного средства
        self.kind = kind #Тип транспортного средства

    def __str__(self):
        return f"Тип транспорта ({self.kind}) марки {self.brand} может развить скорость {self.max_speed} км/ч"

class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage#Пробег автомобиля
        self._gasoline_residue = gasoline_residue#Остаток бензина в автомобиле

    @property
    def gasoline(self):
        return f"У {self.brand} сталось бензина где-то на {self._gasoline_residue} км"

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int) and value >= 0:
            self._gasoline_residue = value
        else:
            print("Неверное значение количества бензина")

    def __str__(self):
        return f"Автомобиль марки {self.brand} может развить скорость {self.max_speed} км/ч. Пробег: {self.mileage} км"


# Создание объектов типа Car с брендам
audi = Car("Audi", 220, 3500, 40)
tesla = Car("Tesla", 250, 98000, 0)
opel = Car("Opel", 180, 408068, 35)
lexus = Car("Lexus", 240, 615401, 45)

# Вывод информации об автомобилях
print(audi)
print(tesla)
print(opel)
print(lexus)

#Расход бензина автомобилем
audi.gasoline = 40
tesla.gasoline = 30
opel.gasoline = 33
lexus.gasoline = 8

# Вывод информации остатке бензина
print(audi.gasoline)
print(tesla.gasoline)
print(opel.gasoline)
print(lexus.gasoline)