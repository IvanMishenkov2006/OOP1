class MilitaryPersonnel:
    def __init__(self, last_name, company, rank, birth_date, enlistment_date, unit):
        # Инициализация атрибутов класса MilitaryPersonnel
        self.last_name = last_name
        self.company = company
        self.rank = rank
        self.birth_date = birth_date
        self.enlistment_date = enlistment_date
        self.unit = unit

    def __str__(self):
        # Переопределение метода __str__ для класса MilitaryPersonnel
        return f"Фамилия: {self.last_name}\n" \
               f"Рота: {self.company}\n" \
               f"Звание: {self.rank}\n" \
               f"Дата рождения: {self.birth_date}\n" \
               f"Дата поступления на службу: {self.enlistment_date}\n" \
               f"Часть: {self.unit}"

class MilitaryCommand:
    def __init__(self, district, position, years_of_service, allowance_amount):
        # Инициализация атрибутов класса MilitaryCommand
        self.district = district
        self.position = position
        self.years_of_service = years_of_service
        self.allowance_amount = allowance_amount

    def __str__(self):
        # Переопределение метода __str__ для класса MilitaryCommand
        return f"Название округа: {self.district}\n" \
               f"Должность: {self.position}\n" \
               f"Выслуга лет: {self.years_of_service}\n" \
               f"Сумма надбавки: {self.allowance_amount}"

class ContractMilitaryService(MilitaryPersonnel):
    def __init__(self, last_name, company, rank, birth_date, enlistment_date, unit, contract_period, contract_date, protocol_number, salary_amount):
        # Инициализация атрибутов класса ContractMilitaryService
        super().__init__(last_name, company, rank, birth_date, enlistment_date, unit)
        self.contract_period = contract_period
        self.contract_date = contract_date
        self.protocol_number = protocol_number
        self.salary_amount = salary_amount

    def __str__(self):
        # Переопределение метода __str__ для класса ContractMilitaryService
        return super().__str__() + "\n" \
               f"Период договора: {self.contract_period}\n" \
               f"Дата договора: {self.contract_date}\n" \
               f"Номер протокола: {self.protocol_number}\n" \
               f"Сумма зарплаты: {self.salary_amount}"
class AwardedPersonnel(MilitaryPersonnel):
    def __init__(self, last_name, company, rank, birthday_date, enlistment_date, unit, award_name, award_amount, allowance_amount):
        # Вызов конструктора родительского класса MilitaryPersonnel с помощью super()
        super().__init__(last_name, company, rank, birthday_date, enlistment_date, unit)
        # Инициализация атрибутов, специфичных для класса AwardedPersonnel
        self.award_name = award_name
        self.award_amount = award_amount
        self.allowance_amount = allowance_amount
    def __str__(self):
        # Вызов метода __str__() родительского класса MilitaryPersonnel с помощью super()
        return super().__str__() + "\n" \
            f"Название награды: {self.award_name}\n" \
            f"Премия: {self.award_amount}\n" \
            f"Сумма надбавки: {self.allowance_amount}"
#Создание экземпляра класса MilitaryPersonnel с помощью конструктора класса
person = MilitaryPersonnel("Иванов", "1-я рота", "лейтенант", "01.01.1990", "01.01.2010", "Часть 1")
#Создание экземпляра класса MilitaryCommand с помощью конструктора класса
company = MilitaryCommand("Московский", "главнокомандующий", 15, 10000)
#Создание экземпляра класса ContractMilitaryService с помощью конструктора класса
contract_person = ContractMilitaryService("Петров", "2-я рота", "капитан", "01.01.1985", "01.01.2005", "Часть 2", "5 лет", "01.01.2025", "12345", 50000)
#Создание экземпляра класса AwardedPersonnel с помощью конструктора класса
award_person = AwardedPersonnel("Сидоров", "3-я рота", "майор", "01.01.1980", "01.01.2000", "Часть 3", "Заслуженный боец", "100000", "20000")
#Вывод экземпляров класса
print(person)
print("======================")
print(company)
print("======================")
print(contract_person)
print("======================")
print(award_person)