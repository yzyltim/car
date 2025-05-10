class Sim:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def play(self, other):
        self.happiness += 10
        other.happiness += 10
        print(f"{self.name} и {other.name} Грають. Щастя: {self.happiness}, {other.happiness}")

    def argue(self, other):
        self.happiness -= 10
        other.happiness -= 10
        print(f"{self.name} и {other.name} ругаються. Щастя: {self.happiness}, {other.happiness}")

    def eat(self):
        self.hunger -= 10
        print(f"{self.name} поїв. Голод: {self.hunger}")

anna = Sim("Вікторія")
boris = Sim("Борис")

anna.play(boris)
anna.eat()
boris.argue(anna)
boris.eat()
