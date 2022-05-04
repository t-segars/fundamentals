from pet import Pet


class Ninja:


    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Spot", "dog", "sit")

    def walk(self):
        print(f"{self.first_name} takes their pet for a walk")
        self.pet.play()

    def feed(self):
        print(f"{self.first_name} feeds pet {self.pet.type} some {self.pet_food}")
        self.pet.eat()

    def bathe(self):
        print(f"{self.first_name} gives their pet {self.pet.type} a bathe")
        self.pet.noise()

Nicole = Ninja("Nicole", "Prentice", "Buck", "house made chow", Pet("Buck", "Boxer", "speak"))
Nicole.pet = Pet("Buck", "Boxer", "speak")
print("----------------")
Nicole.walk()
print("----------------")
Nicole.feed()
print("----------------")
Nicole.bathe()
print("----------------")

Tim =  Ninja("Tim", "Segars", 'Anabelle', "kibble", Pet("Belle", "Tibetan Terrier", "speak"))
Tim.pet = Pet("Anabelle", "Tibetan Terrier", "speak")
print("----------------")
Tim.walk()
print("----------------")
Tim.feed()
print("----------------")
Tim.bathe()
print("----------------")