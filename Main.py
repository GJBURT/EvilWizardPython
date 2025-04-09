from characters import Warrior, Mage, Archer, Paladin, Necromancer
from enemies import EvilWizard
from utility import create_character

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
                player.summon_undead(wizard)
            else:
                print("\nInvalid choice. Try again.")
        elif choice == '3':  # Heal
            player.potion()
        elif choice == '4':
            player.display_stats()
        elif choice == '5':
            print("\nExiting the game.")
            exit()
        else:
            print("\nInvalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"\n{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"\nThe wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
