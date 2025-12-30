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
            description="Restore 30%% of max HP, limit 30HP",
            price=30
        )
    def use(self, player):
        heal = int(min(player.max_life * 0.3, 30))
        # Coloco o int pois quando eu multiplico por 0.3 o numero vira float
        player.life = min(player.life + heal, player.max_life)
        print(f"You healed {heal} HP")

class FullHealPotion(Item):
    def __init__(self):
        super().__init__(
            name="Full Heal Potion",
            description="Restore 100%% of your HP",
            price=120
        )
    def use(self, player):
        player.life = player.max_life
        print("Your HP has been maximized")
