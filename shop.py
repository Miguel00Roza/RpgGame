# Import de itens de cura
from itens import BasicHealPotion, FullHealPotion
# Favor conforme mais itens serem adicionados separar em categoria
# EX: Import armaduras
# from itens imort ArmaduraFodona
# Não sei se vai pesar importar tudo separado mas azar

class Shop:
    def __init__(self):
        self.itens = [
            BasicHealPotion,
            FullHealPotion
        ]

    def buy(self, player_buying):
        while True:
            print("0-Exit")
            for i, item in enumerate(self.itens):
                temp_item = item()
                print(f"{i + 1}-{temp_item.name}({temp_item.price} golds)")
            choice = int(input("What do you want to buy?"))
            if choice == 0:
                print("bye bye")
                return 0
            else:
                if choice > len(self.itens):
                    print("We dont have this")
                else:
                    item_Buying_class = self.itens[choice - 1] # -1 because i show the index whit plus one on the For Loop
                    item_buying = item_Buying_class()
                    if player_buying.gold < item_buying.price:
                        print("you don't have gold enough")
                    else:
                        player_buying.gold -= item_buying.price
                        
                        player_buying.add_item(item_buying)
                        print(f"You buyed a {item_buying.name}")
        