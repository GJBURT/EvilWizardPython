class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"\n{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Special Ability: {self.special_ability}")

    def potion(self):
        if self.health < self.max_health:
            heal_amount = min(self.max_health - self.health, self.potion_amount)
            self.health += heal_amount
            print(f"\n{self.name} uses a potion and heals for {heal_amount} health! Current health: {self.health}")
        else:
            print(f"\n{self.name} is already at full health!")

# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.special_ability = "Shield Bash"
        self.potion_amount = self.max_health * 0.2

# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.special_ability = "Fireball"
        self.potion_amount = self.max_health * 0.2

# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.special_ability = "Power Shot"
        self.potion_amount = self.max_health * 0.2

# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
        self.special_ability = "Holy Shield"
        self.holy_light_amount = self.max_health * 0.25

# Necromancer class
class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25)
        self.special_ability = "Summon Undead"
        self.necronic_heal = "soul_siphon"