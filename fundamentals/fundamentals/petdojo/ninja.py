import dojopet
import dog
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()



cat = dojopet.Pet("mochi", "BS", "Roll over")

puppy = dog.Dog("Ichigo", "Akita", "Sleep")

pet1 = Ninja("Trong","Doan","Beef","keble",cat)
pet1.feed().walk().bathe()

pet2 = Ninja("Trong","Doan","Beef","keble",puppy)
pet2.feed().walk().bathe()



