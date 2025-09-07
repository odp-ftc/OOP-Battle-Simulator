from enemy import Enemy

class Baby_Elf(Enemy):
    #new ability
    def cry():
        print("WAAAAAAAAAAAAH")
    
    def take_damage(self,damage):
        print("YOU KILLED A CHILD :D")
        return super().take_damage(damage)
