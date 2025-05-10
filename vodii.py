class Osoba:
    def __init__(self, imya, vik):
        self.imya = imya
        self.vik = vik

    def pokazaty_info(self):
        print(f"Ім'я: {self.imya}, Вік: {self.vik}")

class Vodiy(Osoba):
    def __init__(self, imya, vik, prava):
        super().__init__(imya, vik)
        self.prava = prava

    def pokazaty_info(self):
        super().pokazaty_info()
        print(f"Номер посвідчення: {self.prava}")

v = Vodiy("Олег", 35, "AB123456")
v.pokazaty_info()
