class Worker:
    def __init__(self, full_name, position, start_year, salary):
        self._full_name = full_name
        self._position = position
        self._start_year = start_year
        self._salary = salary
    def full_name(self):
        return self._full_name
    def position(self):
        return self._position
    @property
    def start_year(self):
        return self._start_year
    @property
    def salary(self):
        return self._salary
worker1 = Worker("Данишевский Даниил Павлович ", "Уборщик", 2018, 5)
print(worker1.full_name()) # Выводит значение полного имени
print(worker1.position()) # Выводит значение должности
print(worker1.start_year) # Выводит значение года поступления на работу (2018)
print(worker1.salary) # Выводит значение зарплаты (5)