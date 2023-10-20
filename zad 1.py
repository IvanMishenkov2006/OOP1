class C:
    def __init__(self, a, b=5):# Определение метода инициализации с двумя параметрами-a и b (b имеет значение по умолчанию равное 5)
        self.a = a# Установка переменной экземпляра a значением параметра a
        self.b = b# Установка переменной экземпляра b значением параметра b
    def c(self):# Определение метода с именем c
        return self.a + self.b # Возврат суммы переменных экземпляра a и b
    def d(self):# Определение метода с именем d
        return self.a - self.b# Возврат разности переменных экземпляра a и b
a1 = C(5)# Создание объекта a1 класса C с аргументом 5 для параметра a
print(f'{a1.a}+{a1.b}', a1.c())# Печать форматированной строки, отображающей значения a1.a и a1.b, вместе с результатом метода c()
a2 = C(4, 6)# Создание объекта a2 класса C с аргументами 4 и 6 для параметров a и b соответственно
print(f'{a2.a}-{a2.b}', a2.d())# Печать форматированной строки, отображающей значения a2.a и a2.b, вместе с результатом метода d()