import random


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        if (random.randint(0, 1) == 0):
            print(f"{self.name} defeats {opponent.name}!")
        else:
            print(f"{opponent.name} defeats {self.name}")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 250)

    hero1.fight(hero2)
