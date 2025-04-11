import random

class EvilWizard:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 15

    def regenerate(self):
        self.health += 5
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}")

    # Need to update to account for Rage ability where warrior takes half damage, Mana Shield has a 25% shield, Bone Armor has a 25% shield, and Shadow Dance has a chance to dodge
    def attack(self, opponent):
        if hasattr(opponent, 'rage') and opponent.rage:
            damage = self.attack_power // 2  # Half damage if the warrior is enraged
            opponent.is_enraged = False  # Reset rage status after the attack
        elif hasattr(opponent, 'mana_shield') and opponent.mana_shield:
            damage = self.attack_power * 0.75  # 25% damage reduction if the mage has a mana shield
        elif hasattr(opponent, 'bone_armor') and opponent.bone_armor:
            damage = self.attack_power * 0.75
        elif hasattr(opponent, 'shadow_dance') and opponent.shadow_dance:
            dodge_chance = opponent.shadow_dance
            if random.random() < dodge_chance:
                print(f"{opponent.name} dodges the attack!")
                return  # No damage if dodged   
        else:
            damage = self.attack_power

        opponent.health -= damage
        print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")