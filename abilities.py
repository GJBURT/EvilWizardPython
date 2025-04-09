def shield_bash(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} uses Shield Bash on {opponent.name} for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")

def fireball(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} uses Fireball on {opponent.name} for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")

def summon_undead(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} summons an undead minion to attack {opponent.name} for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")