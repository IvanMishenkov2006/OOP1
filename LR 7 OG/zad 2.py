class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def c(self):
        return self.a ** 3 + 2/5 * self.b

obj = A(2, 6)
print(obj.c)  # Выводит значение выражения: