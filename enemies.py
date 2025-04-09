class EvilWizard:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 15

    def regenerate(self):
        self.health += 5
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"\n{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")