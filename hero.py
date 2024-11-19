from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_damage_blocked = 0
        for armor in self.armors:
            total_damage_blocked += armor.block()
        return total_damage_blocked

    def take_damage(self, damage):
        damage_taken = 0
        damage_blocked = self.defend()
        if (damage_blocked >= damage):
            print("Tis but a scratch")
        else:
            damage_taken = damage - damage_blocked
            self.current_health = self.current_health - damage_taken

    def is_alive(self):
        if (self.current_health <= 0):
            return False
        else:
            return True

    def fight(self, opponent):
        if (len(self.abilities) == 0 or len(opponent.abilities) == 0):
            print("Draw")
        else:
            fight_is_active = True
            while (fight_is_active):
                opponent.take_damage(self.attack())
                if (opponent.is_alive() == False):
                    print(f"{self.name} won!")
                    fight_is_active = False
                    return
                self.take_damage(opponent.attack())
                if (self.is_alive() == False):
                    print(f"{opponent.name} won!")
                    fight_is_active = False
                    return


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
