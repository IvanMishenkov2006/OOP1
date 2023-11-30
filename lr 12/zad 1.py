# Определение класса Bank
class Bank:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

# Определение класса Filial (филиал)
class Filial:
    def __init__(self, name, total_deposits):
        self.name = name
        self.total_deposits = total_deposits

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_total_deposits(self):
        return self.total_deposits

    def set_total_deposits(self, new_total_deposits):
        self.total_deposits = new_total_deposits

# Определение класса Deposit (вклад)
class Deposit:
    def __init__(self, client_name, deposit_amount):
        self.client_name = client_name
        self.deposit_amount = deposit_amount

    def get_client_name(self):
        return self.client_name

    def set_client_name(self, new_client_name):
        self.client_name = new_client_name

    def get_deposit_amount(self):
        return self.deposit_amount

    def set_deposit_amount(self, new_deposit_amount):
        self.deposit_amount = new_deposit_amount

    def calculate_deposit(self, months):
        try:
            if months < 0:
                raise ValueError("Количество месяцев не может быть отрицательным")
            else:
                return self.deposit_amount * months
        except ValueError as e:
            print("Ошибка:", str(e))

# Определение класса LongTermDeposit (долгосрочный вклад), унаследованного от Deposit
class LongTermDeposit(Deposit):
    def calculate_deposit(self, months):
        try:
            if months < 0:
                raise ValueError("Количество месяцев не может быть отрицательным")
            else:
                return self.deposit_amount * months * 1.1
        except ValueError as e:
            print("Ошибка:", str(e))

# Определение класса DemandDeposit (вклад до востребования), унаследованного от Deposit
class DemandDeposit(Deposit):
    def calculate_deposit(self, months):
        try:
            if months < 0:
                raise ValueError("Количество месяцев не может быть отрицательным")
            else:
                return self.deposit_amount * months * 1.05
        except ValueError as e:
            print("Ошибка:", str(e))

# Создание экземпляров объектов
bank = Bank("БелАгроПромБанк")
filial = Filial("Филиал 1", 9999999)
deposit = Deposit("Тополь Алексей Витальевич", 50000)
long_term_deposit = LongTermDeposit("Берёза Елизавета Сергеевна", 100000)
demand_deposit = DemandDeposit("Ель Александр Иванович", 200000)

# Вывод информации об объектах
print("Название банка:", bank.get_name())
print("Общая сумма вкладов в филиале:", filial.get_total_deposits())
print("Сумма вклада Тополя Алексея Витальевича:", deposit.get_deposit_amount())
print("Сумма вклада Тополя Алексея Витальевича через 10 месяцев:", deposit.calculate_deposit(10))
print("Сумма долгосрочного вклада Берёзы Елизаветы Сергеевны через 10 месяцев:", long_term_deposit.calculate_deposit(10))
print("Сумма вклада до востребования Ель Александра Ивановича через -1 день:", demand_deposit.calculate_deposit(-1))
