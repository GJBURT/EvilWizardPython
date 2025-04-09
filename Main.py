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
    def power_shot(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Power Shot on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        
    # Holy Shield method for Paladin class
    # This method is used to deal double damage to the opponent
    def holy_shield(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} blesses his shield with holy energy and throws his Holy Shield at {opponent.name} for {damage} damage! {self.name}'s shield returns to them!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!") 
    
    # Summon Undead method for Necromancer class
    # This method is used to deal double damage to the opponent
    def summon_undead(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} summons an undead minion to attack {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    # Soul Siphon method for Necromancer class
    # This method is used to 10% of Necromancer's max health as damage to the opponent and returns the same amount of health to the Necromancer
    def soul_siphon(self, opponent):
        damage = self.max_health * 10 / 100  # 10% of max health
        if damage > opponent.health: # Ensure we don't deal more damage than the opponent's health
            damage = opponent.health
        opponent.health -= damage # Deal damage to opponent
        
        # Heal the necromancer for the same amount of damage dealt
        # This is the amount of health the necromancer will heal for
        # Ensure the health does not exceed max health
        if self.health < self.max_health:
            heal_amount = min(damage, self.max_health - self.health)
            self.health += damage
            print(f"{self.name} siphons the soul of {opponent.name} for {damage} damage and heals for {heal_amount} health! Current health: {self.health}")
        else:
            print(f"{self.name} is already at full health!")
        print(f"{self.name} siphons the soul of {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25) 
        self.special_ability="Shield Bash"
        self.potion=(self.max_health*0.2)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.special_ability="Fireball"
        self.potion=(self.max_health*0.2)

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
        super().__init__(name, health=120, attack_power=30)
        self.special_ability="Power Shot"
        self.potion=(self.max_health*0.2)

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
        self.special_ability="Holy Shield"
        self.holy_light=(self.max_health*0.25)

# Create Necromancer class
class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25)
        self.special_ability="Summon Undead"
        self.necronic_heal="soul_siphon"

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin") 
    print("5. Necromancer")  # Implement Necromancer class
    print("6. Rogue")  # Implement Rogue class
    print("7. Exit")

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
    elif class_choice == '5': # Implement Necromancer class
        print("Necromancer class is not implemented yet.")
        return Necromancer(name)
    elif class_choice == '6': # Implement Rogue class
        print("Rogue class is not implemented yet.")
        return Rogue(name)
    elif class_choice == '7':
        print("Exiting the game.")
        exit()
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
        print("5. Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.shield_bash(wizard)
            elif isinstance(player, Mage):
                player.fireball(wizard)
            elif isinstance(player, Archer):
                player.power_shot(wizard)
            elif isinstance(player, Paladin):
                player.holy_shield(wizard)
            elif isinstance(player, Necromancer):
                player.soul_siphon(wizard)
            else:
                print("Invalid choice. Try again.")
        elif choice == '3':
            if isinstance(player, Warrior, Archer, Mage):
                player.potion()
            elif isinstance(player, Paladin):
                player.holy_light()
            elif isinstance(player, Necromancer):
                player.soul_siphon(wizard)
            else:
                print("Invalid choice. Try again.")
        elif choice == '4':
            player.display_stats()
        elif choice == '5':
            print("Exiting the game.")
            exit()
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
