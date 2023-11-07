class Oleg:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if isinstance(other, int):
            return Oleg([x + other for x in self.values])
        elif isinstance(other, Oleg) and len(self.values) == len(other.values):
            return Oleg([x + y for x, y in zip(self.values, other.values)])
        else:
            raise ValueError("Сложение не поддерживается для этих типов или векторы имеют разную длину.")

    def __mul__(self, other):
        if isinstance(other, int):
            return Oleg([x * other for x in self.values])
        elif isinstance(other, Oleg) and len(self.values) == len(other.values):
            return Oleg([x * y for x, y in zip(self.values, other.values)])
        else:
            raise ValueError("Умножение не поддерживается для этих типов или векторы имеют разную длину.")

    def __str__(self):
        if len(self.values) == 0:
            return "Пустой вектор"
        else:
            return str(self.values)
O1 = Oleg([1, 2, 3])
O2 = Oleg([4, 5, 6])
# Сложение векторов
result = O1 + O2
print(result)
# Умножение вектора на число
result = O1 * 2
print(result)
result2=O2 * 4
print(result2)