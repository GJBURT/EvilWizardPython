from characters import Warrior, Mage, Archer, Paladin, Necromancer, Rogue
from enemies import EvilWizard
from utility import create_character
import random

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        # Dynamically update menu options based on the player's class
        special_ability = player.special_ability if hasattr(player, 'special_ability') else "Special Ability"
        unique_ability = player.unique_ability if hasattr(player, 'unique_ability') else "Unique Ability"
        
        print("\n--- Your Turn ---")
        print("1. Attack")
        print(f"2. {special_ability}")
        print(f"3. {unique_ability}")
        print("4. Heal")
        print("5. View Stats")
        print("6. Exit")

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
                player.divine_strike(wizard)
            elif isinstance(player, Necromancer):
                player.summon_undead(wizard)
            elif isinstance(player, Rogue):
                player.backstab(wizard)
            else:
                print("\nInvalid choice. Try again.")
        # This will have Choice 3 for the Second Special Ability for each class, their unique ability
        elif choice == '3':  # Unique Ability
            if isinstance(player, Warrior):
                player.rage()
            elif isinstance(player, Mage):
                player.mana_shield()
            elif isinstance(player, Archer):
                player.rapid_fire(wizard)
            elif isinstance(player, Paladin):
                player.holy_shield()
            elif isinstance(player, Necromancer):
                player.soul_siphon(wizard)
            elif isinstance(player, Rogue):
                player.shadow_dance()  # Call the Rogue's shadow_dance method
            else:
                print("\nInvalid choice. Try again.")
        elif choice == '4':  # Heal
            if isinstance(player, (Warrior, Mage, Archer, Rogue)):
                player.potion()
            elif isinstance(player, Paladin):
                player.holy_light()
            elif isinstance(player, Necromancer):
                player.soul_siphon(wizard)
        elif choice == '5':
            player.display_stats()
        elif choice == '6':
            print("\nExiting the game.")
            exit()
        else:
            print("\nInvalid choice. Try again.")

        # Wizard's turn
        if wizard.health > 0:
            wizard.regenerate()
            if wizard.skip_turn:
                print(f"\n{wizard.name} is stunned and misses their turn!")
                wizard.skip_turn = False  # Reset the skip_turn flag
            else:
                if isinstance(player, Rogue) and isinstance(player.dodge_chance, float) and player.dodge_chance > 0: # Rogue's Shadow Dance ability
                    import random
                    if random.random() < player.dodge_chance:
                        print(f"\n{player.name} dodges the attack using Shadow Dance!")
                    else:
                        wizard.attack(player)
                else:
                    if isinstance(player, (Paladin, Necromancer)) and player.is_protected: # Paladin's Holy Shield or Necromancer's Bone Armor
                        damage = int(wizard.attack_power * 0.75)  # Reduce damage by 25%
                        player.health -= damage
                        print(f"\n{wizard.name} attacks {player.name} for {damage} damage!")
                    else:
                        # Normal attack if not protected
                        wizard.attack(player)
                
            # Reset the enraged state after warrior takes damage
            if isinstance(player, Warrior) and player.is_enraged:
                player.is_enraged = False
                print(f"\n{player.name} is no longer enraged.")
        if player.health <= 0:
            print(f"\n{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"\n {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
