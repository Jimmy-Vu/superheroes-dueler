class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    def bark(self):
        print("Woof!")

    def sit(self):
        print(f"{self.name} sits")

    def rollover(self):
        print(f"{self.name} rolls over")
