class Prystiy:
    def uvimknyty(self):
        print("Пристрій увімкнено")

    def vymknyty(self):
        print("Пристрій вимкнено")

class Televizor(Prystiy):
    def pokazaty_kanal(self):
        print("Показує телевізійний канал")

class Noutbuk(Prystiy):
    def zapustyty_programu(self):
        print("Запускає програму на ноутбуці")

tv = Televizor()
tv.uvimknyty()
tv.pokazaty_kanal()
tv.vymknyty()

print("---")

pc = Noutbuk()
pc.uvimknyty()
pc.zapustyty_programu()
pc.vymknyty()
