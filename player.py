class Player:
    """ Player proprerties and actions """
    def __init__(self):
        self.level = 1
        self.name = input("Enter your name:\n")
        self.life = 100
        self.max_life = 100
        self.damage = 15
        self.gold = 0
        self.xp = 0
        self.required_xp = 10
        self.basic_heals = 5
        self.full_heals = 3

    def levelUp(self):
        # Adicionei esse increase pra dar uma balanceada, player mid game ja tava com vida pra kct skkdsakdas
        increase = min(self.max_life * 0.3, 30)
        self.level += 1
        self.percent30_life = self.max_life * 0.3
        self.max_life += increase
        self.life += increase
        self.damage += 2
        self.gold += 10
        self.required_xp += 5
    
    def gain_xp(self, enemy_xp):
        self.xp += enemy_xp
        while self.xp >= self.required_xp:
            self.xp -= self.required_xp
            self.levelUp()
            print("Level UP\n")
            print(f"Current level: {self.level}")
    
    def show_player_status(self):
        print(f"------------------- Name: {self.name} --------------------")
        print(f"Level: {self.level}")
        print(f"Damage: {self.damage}")
        print(f"life: {self.life}/{self.max_life}")
        print(f"Gold: {self.gold}")
        print(f"xp: {self.xp}/{self.required_xp}")
        print(f"Basic_heal: {self.basic_heals}")
        print(f"Full_heal: {self.full_heals}")
        print("-"*55)
    
    def basic_heal(self):
        heal = 30
        self.life = min(self.life + heal, self.max_life)
        self.basic_heals -= 1
        print(f"You healed {heal} HP, current basic heals: {self.basic_heals}")
    
    def max_heal(self):
        self.life = self.max_life
        self.full_heals -= 1
        print(f"Your HP has been maximized, current full heals: {self.full_heals}")