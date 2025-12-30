from player import Player
from shop import Shop
from combat import combat

player = Player()
shop = Shop()

player.gold = 9999999

while True:
    if player.life <= 0:
        break

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
            
    

