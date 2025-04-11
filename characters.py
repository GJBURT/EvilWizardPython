from abilities import shield_bash, fireball, summon_undead, backstab, power_shot, holy_shield, holy_light, soul_siphon, shadow_dance, mana_shield, bone_armor, rage, rapid_fire, divine_strike

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    # Standard Normal Attack
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"\n{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    # Displaying Character Stats
    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Special Ability: {self.special_ability}")

    # Healing with a Potion
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
        
    def rage(self):
        rage(self)

# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.special_ability = "Fireball"
        self.unique_ability = "Mana Shield"
        self.potion_amount = self.max_health * 0.2
        
    def fireball(self, opponent):
        fireball(self, opponent)
    
    def mana_shield(self):
        mana_shield(self)

# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.special_ability = "Power Shot"
        self.unique_ability = "Rapid Fire"
        self.potion_amount = self.max_health * 0.2
        
    def power_shot(self, opponent):
        power_shot(self, opponent)
        
    def rapid_fire(self, opponent):
        rapid_fire(self, opponent)

# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
        self.special_ability = "Divine Strike"
        self.unique_ability = "Holy Shield"
        self.holy_light_amount = self.max_health * 0.25
        self.is_protected = False  # New attribute to track if the paladin is protected
        
    def holy_shield(self):
        holy_shield(self)

    def holy_light(self):
        holy_light(self)
    
    def divine_strike(self, opponent):
        divine_strike(self, opponent)
        

# Necromancer class
class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25)
        self.special_ability = "Summon Undead"
        self.necronic_heal = "soul_siphon"
        self.unique_abilitiy = "bone_armor"
        self.is_protected = False  # New attribute to track if the paladin is protected
        
    def summon_undead(self, opponent):
        summon_undead(self, opponent)

    def soul_siphon(self, opponent):
        soul_siphon(self, opponent)
        
    def bone_armor(self, opponent):
        bone_armor(self, opponent)
        
# Rogue class
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=115, attack_power=28)
        self.special_ability = "Backstab"
        self.unique_ability = "Shadow Dance"
        self.potion_amount = self.max_health * 0.2
    
    def backstab(self, opponent):
        backstab(self, opponent)
        
    def shadow_dance(self, opponent):
        shadow_dance(self, opponent)