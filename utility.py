from characters import Warrior, Mage, Archer, Paladin, Necromancer, Rogue

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    print("5. Necromancer")
    print("6. Rogue")  
    print("7. Exit")

    class_choice = input("Enter the number of your class choice: ")

    if class_choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("\nInvalid choice. Defaulting to Warrior.")
        class_choice = '1'

    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    elif class_choice == '5':
        return Necromancer(name)
    elif class_choice == '6':
        return Rogue(name)
    elif class_choice == '7':
        print("Exiting the game.")
        exit()