class Flower:
    def __init__(self, name, freshness, stem_length):
        self.name = name
        self.freshness = freshness
        self.stem_length = stem_length
    def __repr__(self):
        return f"Flower('{self.name}', {self.freshness}, {self.stem_length})"
# Создание объектов-цветов
flower1 = Flower("Роза", 8, 1)
flower2 = Flower("Тюльпан", 7, 17)
flower3 = Flower("Адуванчик", 4, 12)
flower4 = Flower("Пионы", 6, 6)
# Помещение цветов в список
flowers = [flower1, flower2, flower3, flower4]
# Сортировка цветов по уровню свежести
sorted_flowers = sorted(flowers, key=lambda flower: flower.freshness, reverse=True)
print("Отсортированные цветы по уровню свежести:")
for flower in sorted_flowers:
    print(flower)
# Найти цветы в заданном диапазоне длин стеблей
min_stem_length = 10
max_stem_length = 15
filtered_flowers = [flower for flower in flowers if min_stem_length <= flower.stem_length <= max_stem_length]
print("\nЦветы в заданном диапазоне длин стеблей:")
for flower in filtered_flowers:
    print(flower)