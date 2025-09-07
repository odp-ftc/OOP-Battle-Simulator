import random


class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 267
        self.attack_power = random.randint(10, 41)
        self.defense = random.randint(15, 20)
        self.banana = random.randint(1,5) < 1 #Hero hits goblin with infinity banana, leading to their DOOOM
    

    def strike(self):
        if self.banana:
            return 9999999999
        else:
            return random.randint(5, self.attack_power)
    
    def receive_damage(self, damage):
        if self.health >= 0:
            self.health -= damage//self.defense
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    def is_alive(self):
        return self.health > 0
