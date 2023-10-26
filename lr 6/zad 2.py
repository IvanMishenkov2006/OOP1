class Abiturient:
    #Класс для представления абитуриента.
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def print_info(self):
#Метод для вывода информации об абитуриенте.
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age}\n'
              f'Школа: {self.school}\n')

if __name__ == '__main__':
#Создание объектов класса Abiturient
    abiturient1 = Abiturient("Мишенков Иван", 16, "Школа №1")
    abiturient2 = Abiturient("Тополь Алексей", 17, "Школа №3")
#Вывод информации о каждом абитуриенте
    abiturient1.print_info()
    abiturient2.print_info()