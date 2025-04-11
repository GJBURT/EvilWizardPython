import random

class EvilWizard:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 15
        self.skip_turn = False  # New attribute to track if the wizard should skip their turn

    def regenerate(self):
        self.health += 5
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        if self.skip_turn:
            print(f"\n{self.name} is stunned and misses their turn!")
            self.skip_turn = False  # Reset the skip_turn flag
            return
        if hasattr(opponent, 'rage') and opponent.rage:
            damage = self.attack_power // 2  # Half damage if the warrior is enraged
            opponent.is_enraged = False  # Reset rage status after the attack
        elif hasattr(opponent, 'mana_shield') and opponent.mana_shield:
            damage = self.attack_power * 0.75  # 25% damage reduction if the mage has a mana shield
        elif hasattr(opponent, 'bone_armor') and opponent.bone_armor:
            damage = self.attack_power * 0.75 
        else:
            damage = self.attack_power

        opponent.health -= damage
        print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")