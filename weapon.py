import random
from ability import Ability


class Weapon(Ability):
    def attack(self):
        lo = self.max_damage // 2
        return random.randint(lo, self.max_damage)
