import dojopet

class Dog(dojopet.Pet):
    def __init__(self, name, type, trick):
        super().__init__(name, type, trick)

    def noise(self):
        print("woof woof")
        return self
