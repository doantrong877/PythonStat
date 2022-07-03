class Pet:
    def __init__(self, name, type, trick):
        self.name = name
        self.type = type
        self.trick = trick
        self.health = 0
        self.energy = 0

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("meow")
        return self
        
