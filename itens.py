# Classe Item global
class Item:
    consumable = True

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def use(self, player):
        pass

# Itens de cura
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

# Classe global para equipamentos
class Equipaments(Item):
    consumable = False
    
    def __init__(self, name, description, price, hp_bonus=0, damage_bonus=0):
        super().__init__(name, description, price)
        self.hp_bonus = hp_bonus
        self.damage_bonus = damage_bonus

    def equip(self, player):        
        player.max_life += self.hp_bonus
        player.life += self.hp_bonus
        player.damage += self.damage_bonus
        player.equipament = self


        
    def unequip(self, player):
        player.max_life -= self.hp_bonus
        player.damage -= self.damage_bonus

        # Adiciona o item ao inventario de volta
        player.add_item(self)

        player.equipament = None
    
    def use(self, player):
        # Se esse item estiver equipado ele apenas desequipa
        if player.equipament is self:
            self.unequip(player)
            print(f"You unequipped {self.name}")
            return
        
        # Se já tiver algum item equipado, desequipa
        if player.equipament is not None:
            player.equipament.unequip(player)
        
        self.equip(player)
        print(f"You equipped {self.name}")
        

            
# Equipamentos

class Scarf(Equipaments):
    def __init__(self):
        super().__init__(
            name="Scarf", 
            description="A simple scarf, but wearing it makes you feel more alive", 
            price=60, 
            hp_bonus=30
        )

class Crown(Equipaments):
    def __init__(self):
        super().__init__(
            name="Crown",
            description="The crown of an ancient war king, It has some gems in it that may be worth some money",
            price=120,
            hp_bonus=20,
            damage_bonus=5
        )
    
class Cape(Equipaments):
    def __init__(self):
        super().__init__(
            name="Cape",
            description="A nice cape, typical of a hero",
            price=90,
            hp_bonus=10,
            damage_bonus=15
        )