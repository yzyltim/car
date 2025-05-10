class Tvaryna:
    def __init__(self, imya):
        self.imya = imya

    def zvuk(self):
        print("Тварина видає звук")

class Sobaka(Tvaryna):
    def __init__(self, imya):
        super().__init__(imya)

    def zvuk(self):
        print(f"{self.imya} каже: Гав-гав!")

class Kit(Tvaryna):
    def __init__(self, imya):
        super().__init__(imya)

    def zvuk(self):
        print(f"{self.imya} каже: Мяу!")

s = Sobaka("Барсик")
k = Kit("Мурка")

s.zvuk()
k.zvuk()
