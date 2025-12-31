import random

class Enemy:
    """ Enemy properties and actions """
    def __init__(self, name, player):
        self.name = name
        self.level = random.randint(player.level , player.level + 3) # level do mob vai ser o mesmo level do player ou 3 acima
        self.max_life = 90 + (10 * self.level)
        self.life = self.max_life
        self.damage = 8 + (2 * self.level)
        self.xp = 5 * self.level
        self.gold = 1 * self.level