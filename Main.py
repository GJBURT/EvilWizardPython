# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Special Ability: {self.special_ability}")
    
    # Healing method potion  
    def potion(self):
        if self.health < self.max_health:
            heal_amount = min(self.max_health - self.health, self.potion)
            self.health += heal_amount
            print(f"{self.name} uses a potion and heals for {heal_amount} health! Current health: {self.health}")
        else:
            print(f"{self.name} is already at full health!")
    
    # Healing method for Paladin class
    def holy_light(self):
        if self.health < self.max_health:
            heal_amount = min(self.max_health - self.health, self.holy_light)
            self.health += heal_amount
            print(f"{self.name} casts Holy Light causing a bright brilliant light to wash over {self.name} and heals for {heal_amount} health! Current health: {self.health}")
        else:
            print(f"{self.name} is already at full health!")        
    
    # Shield Bash method for Warrior class
    # This method is used to deal double damage to the opponent
    def shield_bash(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Shield Bash on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    # Fireball method for Mage class
    # This method is used to deal double damage to the opponent
    def fireball(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Fireball on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    # Rapid Fire method for Archer class
    # This method is used to deal double damage to the opponent
    def rapid_fire(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Rapid Fire on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        
    # 
    

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, special_ability="Shield Bash", potion=(self.health*0.2))

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, special_ability="Fireball", potion=(self.health*0.2))

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30, special_ability="Rapid Fire", potion=(self.health*0.2))

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20, special_ability="Holy Shield", holy_light=(self.health*0.25))


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)  # Implement Archer class
    elif class_choice == '4':
        return Paladin(name)  # Implement Paladin class
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            pass  # Implement special abilities
        elif choice == '3':
            pass  # Implement heal method
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
