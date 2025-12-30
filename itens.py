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
            description="Restore 30%% of max HP, limit 30HP"
        )
    def use(self, player):
        heal = min(player.max_life * 0.3, 30)
        player.life = min(player.life + heal, player.max_life)
        print(f"You healed {heal} HP")
