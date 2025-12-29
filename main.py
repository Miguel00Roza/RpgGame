import random

class Player:
    """ Player proprerties and actions """
    def __init__(self):
        self.level = 1
        self.name = input("Enter your name:\n")
        self.life = 100
        self.max_life = 100
        self.damage = 25
        self.gold = 0
        self.xp = 0
        self.required_xp = 10
    
    def levelUp(self):
        self.level += 1
        self.max_life += 10
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

    
player = Player()

class Enemy:
    """ Enemy properties and actions """
    def __init__(self, name, player):
        self.name = name
        self.level = random.randint(player.level, player.level + 5) # level do mob vai ser o mesmo level do player ou 5 acima
        self.max_life = 90 + (10 * self.level)
        self.life = self.max_life
        self.damage = 8 + (2 * self.level)
        self.xp = 5 * self.level
        self.gold = 1 * self.level
    

enemy_types = ["Globin", "Skeleton", "Zombie"]
def combat(player_in_combat):
    """ Combat system """
    type_of_enemy = enemy_types[random.randint(0, len(enemy_types) - 1)]
    enemy = Enemy(type_of_enemy, player_in_combat)

    while True:
        print(f"{player_in_combat.name} \nCurrent life: {player_in_combat.life}/{player_in_combat.max_life}\nCurrent level: {player_in_combat.level}\n")
        print(f"{enemy.name} \nEnemy life: {enemy.life}/{enemy.max_life}\nEnemy level: {enemy.level}\n")
        opc = int(input("What do you want to do?\n1-attack\n2-run\n"))
        if opc == 1:
            enemy.life -= player_in_combat.damage
            print(f"You attacked and dealt {player_in_combat.damage} damage!")
        elif opc == 2:
            print("You ran from the combat")
            break
        else:
            print("Do not have these option, try again")
            continue
        
        if enemy.life <= 0:
            print("You win the fight, congratulations!")
            player_in_combat.gain_xp(enemy.xp)
            player_in_combat.gold += enemy.gold
            break
        
        player_in_combat.life -= enemy.damage
        print(f"Enemy attack and dealt {enemy.damage} damage!")

        if player_in_combat.life <= 0:
            print("You died")
            break

combat(player)
            
    

