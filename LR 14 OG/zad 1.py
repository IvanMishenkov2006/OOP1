# Описание родительского класса "Путевки"
class Putevki:
    def __init__(self, kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena):
        self.kod = kod
        self.familia = familia
        self.pansiyonat = pansiyonat
        self.nomer = nomer
        self.vid_jilja = vid_jilja
        self.data_zaezda = data_zaezda
        self.data_vyezda = data_vyezda
        self.kolichestvo_chelovek = kolichestvo_chelovek
        self.cena = cena

# Описание дочерних классов

# Класс "Зарубежные путевки"
class ZarubezhniyePutevki(Putevki):
    def __init__(self, kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena, zagran_pasport, strahovka):
        super().__init__(kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena)
        self.zagran_pasport = zagran_pasport
        self.strahovka = strahovka

# Класс "Санатории"
class Sanatorii(Putevki):
    def __init__(self, kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena, med_polis, diagnoz, napravleniye):
        super().__init__(kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena)
        self.med_polis = med_polis
        self.diagnoz = diagnoz
        self.napravleniye = napravleniye

# Класс "Детские оздоровительные"
class DetskiyeOzdorovitelniye(Putevki):
    def __init__(self, kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena, vozrast_rebenka, svidetelstvo_o_rojdenii, pol):
        super().__init__(kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena)
        self.vozrast_rebenka = vozrast_rebenka
        self.svidetelstvo_o_rojdenii = svidetelstvo_o_rojdenii
        self.pol = pol

# Класс "Спортивные лагеря"
class SportivniyeLagery(Putevki):
    def __init__(self, kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena, vozrast_rebenka, nomer_domika, svidetelstvo_o_rojdenii, pol, predpochitaemiy_vid_sporta):
        super().__init__(kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena)
        self.vozrast_rebenka = vozrast_rebenka
        self.nomer_domika = nomer_domika
        self.svidetelstvo_o_rojdenii = svidetelstvo_o_rojdenii
        self.pol = pol
        self.predpochitaemiy_vid_sporta = predpochitaemiy_vid_sporta

# Класс "Художественные лагеря"
class KhudozhestvenniyeLagery(Putevki):
    def __init__(self, kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena, vozrast_rebenka, nomer_domika, svidetelstvo_o_rojdenii, pol, predpochitaemye_instrumenty_dlya_risovaniya):
        super().__init__(kod, familia, pansiyonat, nomer, vid_jilja, data_zaezda, data_vyezda, kolichestvo_chelovek, cena)
        self.vozrast_rebenka = vozrast_rebenka
        self.nomer_domika = nomer_domika
        self.svidetelstvo_o_rojdenii = svidetelstvo_o_rojdenii
        self.pol = pol
        self.predpochitaemye_instrumenty_dlya_risovaniya = predpochitaemye_instrumenty_dlya_risovaniya

# Создание объектов и вывод информации о них

# Создание объекта класса "Зарубежные путевки"
zarubezhniye_putevki = ZarubezhniyePutevki(
    kod=1,
    familia="Иванов",
    pansiyonat="Отель Riviera",
    nomer=25,
    vid_jilja="Стандартный",
    data_zaezda="2022-08-15",
    data_vyezda="2022-08-30",
    kolichestvo_chelovek=2,
    cena=2500,
    zagran_pasport="AB123456",
    strahovka=True
)

# Создание объекта класса "Санатории"
sanatorii = Sanatorii(
    kod=2,
    familia="Петров",
    pansiyonat="Санаторий Здоровье",
    nomer=12,
    vid_jilja="Люкс",
    data_zaezda="2022-07-10",
    data_vyezda="2022-07-20",
    kolichestvo_chelovek=1,
    cena=3000,
    med_polis="CD789012",
    diagnoz="Гастрит",
    napravleniye="Терапевт"
)

# Создание объекта класса "Детские оздоровительные"
detskiye_ozdorovitelniye = DetskiyeOzdorovitelniye(
    kod=3,
    familia="Сидорова",
    pansiyonat="Детский санаторий Здоровяк",
    nomer=8,
    vid_jilja="Коттедж",
    data_zaezda="2022-06-15",
    data_vyezda="2022-06-25",
    kolichestvo_chelovek=1,
    cena=2000,
    vozrast_rebenka=8,
    svidetelstvo_o_rojdenii="EF345678",
    pol="девочка"
)

# Создание объекта класса "Спортивные лагеря"
sportivniye_lagery = SportivniyeLagery(
    kod=4,
    familia="Козлов",
    pansiyonat="Спортивный лагерь Форсаж",
    nomer=5,
    vid_jilja="Бунгало",
    data_zaezda="2022-07-25",
    data_vyezda="2022-08-10",
    kolichestvo_chelovek=1,
    cena=1800,
    vozrast_rebenka=12,
    nomer_domika=3,
    svidetelstvo_o_rojdenii="GH901234",
    pol="мальчик",
    predpochitaemiy_vid_sporta="Футбол"
)

# Создание объекта класса "Художественные лагеря"
khudozhestvenniye_lagery = KhudozhestvenniyeLagery(
    kod=5,
    familia="Смирнова",
    pansiyonat="Лагерь Художник",
    nomer=7,
    vid_jilja="Палатка",
    data_zaezda="2022-06-20",
    data_vyezda="2022-07-05",
    kolichestvo_chelovek=1,
    cena=1500,
    vozrast_rebenka=10,
    nomer_domika=2,
    svidetelstvo_o_rojdenii="IJ567890",
    pol="девочка",
    predpochitaemye_instrumenty_dlya_risovaniya=["Карандаши", "Акварель"]
)

# Вывод информации о путевках

print("Информация о зарубежных путевках:")
print("Код:", zarubezhniye_putevki.kod)
print("Фамилия клиента:", zarubezhniye_putevki.familia)
print("Название пансионата:", zarubezhniye_putevki.pansiyonat)
print("Номер:", zarubezhniye_putevki.nomer)
print("Вид жилья:", zarubezhniye_putevki.vid_jilja)
print("Дата заезда:", zarubezhniye_putevki.data_zaezda)
print("Дата выезда:", zarubezhniye_putevki.data_vyezda)
print("Количество человек:", zarubezhniye_putevki.kolichestvo_chelovek)
print("Цена:", zarubezhniye_putevki.cena)
print("Загран паспорт:", zarubezhniye_putevki.zagran_pasport)
print("Страховка:", zarubezhniye_putevki.strahovka)

print("\nИнформация о санаториях:")
print("Код:", sanatorii.kod)
print("Фамилия клиента:", sanatorii.familia)
print("Название пансионата:", sanatorii.pansiyonat)
print("Номер:", sanatorii.nomer)
print("Вид жилья:", sanatorii.vid_jilja)
print("Дата заезда:", sanatorii.data_zaezda)
print("Дата выезда:", sanatorii.data_vyezda)
print("Количество человек:", sanatorii.kolichestvo_chelovek)
print("Цена:", sanatorii.cena)
print("Мед. полис:", sanatorii.med_polis)
print("Диагноз:", sanatorii.diagnoz)
print("Направление:", sanatorii.napravleniye)

print("\nИнформация о детских оздоровительных путевках:")
print("Код:", detskiye_ozdorovitelniye.kod)
print("Фамилия клиента:", detskiye_ozdorovitelniye.familia)
print("Название пансионата:", detskiye_ozdorovitelniye.pansiyonat)
print("Номер:", detskiye_ozdorovitelniye.nomer)
print("Вид жилья:", detskiye_ozdorovitelniye.vid_jilja)
print("Дата заезда:", detskiye_ozdorovitelniye.data_zaezda)
print("Дата выезда:", detskiye_ozdorovitelniye.data_vyezda)
print("Количество человек:", detskiye_ozdorovitelniye.kolichestvo_chelovek)
print("Цена:", detskiye_ozdorovitelniye.cena)
print("Возраст ребенка:", detskiye_ozdorovitelniye.vozrast_rebenka)
print("Свидетельство о рождении:", detskiye_ozdorovitelniye.svidetelstvo_o_rojdenii)
print("Пол:", detskiye_ozdorovitelniye.pol)

print("\nИнформация о спортивных лагерях:")
print("Код:", sportivniye_lagery.kod)
print("Фамилия клиента:", sportivniye_lagery.familia)
print("Название пансионата:", sportivniye_lagery.pansiyonat)
print("Номер:", sportivniye_lagery.nomer)
print("Вид жилья:", sportivniye_lagery.vid_jilja)
print("Дата заезда:", sportivniye_lagery.data_zaezda)
print("Дата выезда:", sportivniye_lagery.data_vyezda)
print("Количество человек:", sportivniye_lagery.kolichestvo_chelovek)
print("Цена:", sportivniye_lagery.cena)
print("Возраст ребенка:", sportivniye_lagery.vozrast_rebenka)
print("Номер домика:", sportivniye_lagery.nomer_domika)
print("Свидетельство о рождении:", sportivniye_lagery.svidetelstvo_o_rojdenii)
print("Пол:", sportivniye_lagery.pol)
print("Предпочитаемый вид спорта:", sportivniye_lagery.predpochitaemiy_vid_sporta)

print("\nИнформация о художественных лагерях:")
print("Код:", khudozhestvenniye_lagery.kod)
print("Фамилия клиента:", khudozhestvenniye_lagery.familia)
print("Название пансионата:", khudozhestvenniye_lagery.pansiyonat)
print("Номер:", khudozhestvenniye_lagery.nomer)
print("Вид жилья:", khudozhestvenniye_lagery.vid_jilja)
print("Дата заезда:", khudozhestvenniye_lagery.data_zaezda)
print("Дата выезда:", khudozhestvenniye_lagery.data_vyezda)
print("Количество человек:", khudozhestvenniye_lagery.kolichestvo_chelovek)
print("Цена:", khudozhestvenniye_lagery.cena)
print("Возраст ребенка:", khudozhestvenniye_lagery.vozrast_rebenka)
print("Номер домика:", khudozhestvenniye_lagery.nomer_domika)
print("Свидетельство о рождении:", khudozhestvenniye_lagery.svidetelstvo_o_rojdenii)
print("Пол:", khudozhestvenniye_lagery.pol)
print("Предпочитаемые инструменты для рисования:", khudozhestvenniye_lagery.predpochitaemye_instrumenty_dlya_risovaniya)