numbers = []

while True:
    num = int(input('новое число: '))
    numbers.append(num)
    print('текущий список чисел:', numbers)
    for i in numbers:
        print(i ** 2, i ** 3, i ** 4)
    print()