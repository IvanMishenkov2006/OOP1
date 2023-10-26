# Ввод двух множеств чисел
set1 = set(map(int, input("Введите элементы 1 множества через пробел: ").split()))
set2 = set(map(int, input("Введите элементы 2 множества через пробел: ").split()))
# Найти все различные числа в обоих множествах
distinct_numbers = set1.union(set2)
# Найти числа,которые входят в первое и второе множества и отсортировать их по возрастанию
common_numbers=sorted(set1.intersection(set2))
# Вывести результаты
print("Все различные числа в обоих множествах:", distinct_numbers)
print("Числа, которые входят в первое и второе множества(в порядке возрастания):", common_numbers)