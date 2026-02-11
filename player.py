
class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def attack(self):
        print(f'{self.name} attack!')