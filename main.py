import random

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
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Damage: {self.damage}")
        print(f"life: {self.life}/{self.max_life}")
        print(f"Gold: {self.gold}")
        print(f"xp: {self.xp}/{self.required_xp}")
        print(f"Basic_heal: {self.basic_heals}")
        print(f"Full_heal: {self.full_heals}")
    
    def basic_heal(self):
        heal = 30
        self.life = min(self.life + heal, self.max_life)
        self.basic_heals -= 1
        print(f"You healed {heal} HP, current basic heals: {self.basic_heals}")
    
    def max_heal(self):
        self.life = self.max_life
        self.full_heals -= 1
        print(f"Your HP has been maximized, current full heals: {self.full_heals}")

    
player = Player()

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

class Shop:
    def __init__(self):
        self.basic_heal_price = 20
        self.full_heal_price = 120

    def buy(self, player_buying):
        while True:
            print(f"What do you need?\n1-basic heal:{self.basic_heal_price} golds\n2-full heal:{self.full_heal_price} golds\n3-Exit")
            opc = int(input())
            if opc == 1:
                if player_buying.gold >= self.basic_heal_price:
                    print("You buy 1 basic heal")
                    player_buying.gold -= self.basic_heal_price
                    player_buying.basic_heals += 1
                else:
                    print("You dont have gold enough to this")
            elif opc == 2:
                if player_buying.gold >= self.full_heal_price:
                    print("You buy 1 full heal")
                    player_buying.gold -= self.full_heal_price
                    player_buying.full_heals += 1
                else:
                    print("You dont have gold enough to this")
            elif opc == 3:
                print("Exiting from shop")
                break
            else:
                print("We dont have this")
shop = Shop()

enemy_types = ["Globin", "Skeleton", "Zombie"]
def combat(player_in_combat):
    """ Combat system """
    type_of_enemy = enemy_types[random.randint(0, len(enemy_types) - 1)]
    enemy = Enemy(type_of_enemy, player_in_combat)

    while True:
        print(f"{player_in_combat.name} \nCurrent life: {player_in_combat.life}/{player_in_combat.max_life}\nCurrent level: {player_in_combat.level}\n")
        print(f"{enemy.name} \nEnemy life: {enemy.life}/{enemy.max_life}\nEnemy level: {enemy.level}\n")
        opc = int(input("What do you want to do?\n1-attack\n2-run\n3-heal\n"))
        if opc == 1:
            enemy.life -= player_in_combat.damage
            print(f"You attacked and dealt {player_in_combat.damage} damage!")
        elif opc == 2:
            print("You ran from the combat")
            break
        elif opc == 3:
            if player_in_combat.basic_heals > 0:
                player_in_combat.basic_heal()
            else:
                print("You dont't have any basic heals left")
                continue
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

while True:
    do = int(input("You can\n1-Fight\n2-PlayerStatus\n3-Full heal\n4-Basic heal\n5-Shop\n0-Exit\nWhat do you want?\n"))
    if do == 0:
        print("Bye bye")
        break
    elif do == 1:
        combat(player)
    elif do == 2:
        player.show_player_status()
    elif do == 3:
        if player.full_heals > 0:
            player.max_heal()
        else:
            print("You don't have any full heal left")
    elif do == 4:
        if player.basic_heals > 0:
            player.basic_heal()
        else:
            print("You don't have any basic heal left")
    elif do == 5:
        shop.buy(player)
    else:
        print("Try a true option")
            
    

