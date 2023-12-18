import tkinter as tk

#Функция для вычисления простых процентов
def calculate_simple_interest(principal, interest_rate, time_period):
    simple_interest = (principal * interest_rate * time_period) / 100
    return principal + simple_interest, simple_interest

#Функция для вычисления сложных процентов
def calculate_compound_interest(principal, interest_rate, time_period):
    amount = principal * (1 + interest_rate / 100) ** time_period
    compound_interest = amount - principal
    return amount, compound_interest

#Функция, которая вызывается при нажатии кнопки "Рассчитать"
def calculate():
    #Получаем значения из полей ввода
    principal_amount = float(principal_entry.get())
    time_period = float(time_entry.get())
    interest_rate = float(rate_entry.get())

    #Определяем выбранный тип процентов
    if interest_type.get() == "Простые проценты":
        amount, interest = calculate_simple_interest(principal_amount, interest_rate, time_period)
    else:
        amount, interest = calculate_compound_interest(principal_amount, interest_rate, time_period)

    #Обновляем текст метки с результатом
    result_label.config(text=f"Доход: {interest:.2f}\nСумма в конце срока вклада: {amount:.2f}")

#Инициализация графического интерфейса
root = tk.Tk()
root.title("Вычисление дохода по вкладу")

#Метка и поле ввода для суммы
principal_label = tk.Label(root, text="Сумма:")
principal_label.pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

#Метка и поле ввода для срока в месяцах
time_label = tk.Label(root, text="Срок (месяц):")
time_label.pack()
time_entry = tk.Entry(root)
time_entry.pack()

#Метка и поле ввода для процентной ставки
rate_label = tk.Label(root, text="Процентная ставка (годовая):")
rate_label.pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

#Выбор типа процентов
interest_type = tk.StringVar()
simple_interest_radiobutton = tk.Radiobutton(root, text="Простые проценты", variable=interest_type, value="Простые проценты")
simple_interest_radiobutton.pack()
compound_interest_radiobutton = tk.Radiobutton(root, text="Сложные проценты", variable=interest_type, value="Сложные проценты")
compound_interest_radiobutton.pack()

#Кнопка "Рассчитать"
calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.pack()

#Метка для вывода результатов
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()