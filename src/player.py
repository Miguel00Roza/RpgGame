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
        self.inventory = {}
        self.equipament = None

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
        print(f"inventory: {self.show_inventory()}")
        print(f"Equipament: {self.equipament}")
        print("-"*55)
    
    def add_item(self, item):
        if item.name in self.inventory:
            self.inventory[item.name]["quantity"] += 1
        else:
            self.inventory[item.name] = {
                'item': item,
                'quantity': 1
            }

    def show_inventory(self):
        if not self.inventory:
            print("You have nothing...")
            return 0
        items_inventory = []
        for i, item in enumerate(self.inventory):
                print(f"{i + 1}-{item}")
                quantity = self.inventory[item]["quantity"]
                items_inventory.append(f"{item}({quantity})")
        return items_inventory
    
    def use_item(self):
        while True:
            print("Select item to use or press 0 to exit")
            response = self.show_inventory()
            if response == 0:
                return 0
            
            choice = int(input("chose what item do you want use:\n"))
            if choice == 0:
                print("bye bye")
                return 0
            else:
                if choice > len(response):
                    print("You don't have this")
                else:
                    choice = response[choice - 1]
                    data = self.inventory[choice]
                    item_chosen = data["item"]

                    item_chosen.use(self)
                    # Verifica se é um item empilhavel ( equipamentos não são)
                    if item_chosen.consumable:
                        data["quantity"] -= 1
                        if data["quantity"] == 0:
                            del self.inventory[choice]