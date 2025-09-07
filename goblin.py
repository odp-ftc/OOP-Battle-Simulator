from enemy import Enemy

class Goblin(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        print(self.attack_power)
        self.color = color