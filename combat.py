from enemies import Enemy
import random

# Por enquanto só tem esses 3 inimigos, a unica diferença entre eles é o nome
enemy_types = ["Globin", "Skeleton", "Zombie"]

def combat(player_in_combat):
    """ Combat system """
    type_of_enemy = enemy_types[random.randint(0, len(enemy_types) - 1)]
    enemy = Enemy(type_of_enemy, player_in_combat)

    while True:
        print(f"{player_in_combat.name} \nCurrent life: {player_in_combat.life}/{player_in_combat.max_life}\nCurrent level: {player_in_combat.level}\n")
        print(f"{enemy.name} \nEnemy life: {enemy.life}/{enemy.max_life}\nEnemy level: {enemy.level}\n")
        opc = int(input("What do you want to do?\n1-attack\n2-run\n3-inventory\n"))
        if opc == 1:
            enemy.life -= player_in_combat.damage
            print(f"You attacked and dealt {player_in_combat.damage} damage!\n")
        elif opc == 2:
            print("You ran from the combat")
            break
        elif opc == 3:
            player_in_combat.use_item()
        else:
            print("Do not have these option, try again\n")
            continue
        
        if enemy.life <= 0:
            print("You win the fight, congratulations!\n")
            player_in_combat.gain_xp(enemy.xp)
            player_in_combat.gold += enemy.gold
            break
        
        player_in_combat.life -= enemy.damage
        print(f"Enemy attack and dealt {enemy.damage} damage!\n")

        if player_in_combat.life <= 0:
            print("You died")
            print("Game over, finish status:")
            player_in_combat.show_player_status()
            break
