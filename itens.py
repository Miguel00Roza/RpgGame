class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def use(self, player):
        pass

class BasicHealPotion(Item):
    def __init__(self):
        super().__init__(
            name="Basic Heal Potion",
            description="A magic potion that restore 30% HP, 30 HP limit",
            price=30
        )
    def use(self, player):
        if player.life == player.max_life:
            print("Your HP is already full")
            return 0
        heal = int(min(player.max_life * 0.3, 30))
        # Coloco o int pois quando eu multiplico por 0.3 o numero vira float
        player.life = min(player.life + heal, player.max_life)
        print(f"You healed {heal} HP")
        return heal

class FullHealPotion(Item):
    def __init__(self):
        super().__init__(
            name="Full Heal Potion",
            description="Similar to the basic healing potion, but denser and with more \"Magic Secrets\", heals 100% of HP",
            price=120
        )
    def use(self, player):
        if player.life == player.max_life:
            print("Your HP is already full")
            return 0
        heal = player.max_life
        player.life = heal
        print("Your HP has been maximized")
        return heal

