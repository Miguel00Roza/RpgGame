from player import Player
from shop import Shop
from combat import combat

player = Player()
shop = Shop()

player.gold = 9999999

while True:
    if player.life <= 0:
        break

    do = int(input("You can\n1-Fight\n2-PlayerStatus\n3-Use item\n4-Shop\n0-Exit\nWhat do you want?\n"))
    if do == 0:
        print("Bye bye")
        break
    elif do == 1:
        combat(player)
    elif do == 2:
        player.show_player_status()
    elif do == 3:
        player.use_item()
    elif do == 4:
        shop.buy(player)
    else:
        print("Try a true option")
            
    

