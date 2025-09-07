import random
from enemy import Enemy

class BananaMan(Enemy):
    def __init__(self, name):
        self.health = random.randint(50, 150)
        self.attack_power = random.randint(30, 90)
        super().__init__(name)

    def attack(self):
        print("BANANA TIME")
        if random.randint(1,10) == 1:
            print("TAKE THE BANANA")
            return 999999999
        else:
            print("Banana Missed")
            return Enemy.attack(self)
            

    
    