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