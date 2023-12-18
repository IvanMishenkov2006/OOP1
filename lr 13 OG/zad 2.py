import tkinter as tk
import random

# Функция для генерации массива случайных чисел
def generate_array():
    size = int(entry.get())
    array = [random.randint(1, 100) for _ in range(size)]

    # Выводим сгенерированный массив на экран
    lbl_output['text'] = 'Элементы массива:\n' + ', '.join(map(str, array))

# Функция для поиска минимального элемента в массиве
def find_min():
    array = [int(num) for num in lbl_output['text'].split('\n')[1].split(', ')]
    min_num = min(array)
    lbl_min['text'] = f'Минимальный элемент: {min_num}'

# Функция для поиска максимального элемента в массиве
def find_max():
    array = [int(num) for num in lbl_output['text'].split('\n')[1].split(', ')]
    max_num = max(array)
    lbl_max['text'] = f'Максимальный элемент: {max_num}'

# Функция для вычисления суммы элементов массива
def calculate_sum():
    array = [int(num) for num in lbl_output['text'].split('\n')[1].split(', ')]
    array_sum = sum(array)
    lbl_sum['text'] = f'Сумма элементов: {array_sum}'

# Создаем графический интерфейс
root = tk.Tk()

label = tk.Label(root, text='Введите размер массива:')
label.pack()

entry = tk.Entry(root)
entry.pack()

btn_generate = tk.Button(root, text='Сгенерировать массив', command=generate_array)
btn_generate.pack()

lbl_output = tk.Label(root, text='Элементы массива:')
lbl_output.pack()

btn_min = tk.Button(root, text='Найти минимальный элемент', command=find_min)
btn_min.pack()

lbl_min = tk.Label(root, text='Минимальный элемент:')
lbl_min.pack()

btn_max = tk.Button(root, text='Найти максимальный элемент', command=find_max)
btn_max.pack()

lbl_max = tk.Label(root, text='Максимальный элемент:')
lbl_max.pack()

btn_sum = tk.Button(root, text='Рассчитать сумму элементов', command=calculate_sum)
btn_sum.pack()

lbl_sum = tk.Label(root, text='Сумма элементов:')
lbl_sum.pack()

root.mainloop()