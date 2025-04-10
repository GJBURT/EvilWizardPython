from abilities import shield_bash, fireball, summon_undead, backstab, power_shot, holy_shield

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
    
    def shield_bash(self, opponent):
        shield_bash(self, opponent)

# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.special_ability = "Fireball"
        self.potion_amount = self.max_health * 0.2
        
    def fireball(self, opponent):
        fireball(self, opponent)

# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.special_ability = "Power Shot"
        self.potion_amount = self.max_health * 0.2
        
    def power_shot(self, opponent):
        power_shot(self, opponent)

# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
        self.special_ability = "Holy Shield"
        self.holy_light_amount = self.max_health * 0.25
        
    def holy_shield(self, opponent):
        holy_shield(self, opponent)
        

# Necromancer class
class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25)
        self.special_ability = "Summon Undead"
        self.necronic_heal = "soul_siphon"
        
    def summon_undead(self, opponent):
        summon_undead(self, opponent)
        
    def soul_siphon(self):
        heal_amount = min(self.max_health - self.health, self.necronic_heal)
        self.health += heal_amount
        print(f"\n{self.name} uses Soul Siphon and heals for {heal_amount} health! Current health: {self.health}")

# Rogue class
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=115, attack_power=28)
        self.special_ability = "Backstab"
        self.potion_amount = self.max_health * 0.2
    
    def backstab(self, opponent):
        backstab(self, opponent)