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
        
def backstab(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} vanishes in a puff of smoke reappearing behind {opponent.name} and uses Backstab for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")
        
def power_shot(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} uses Power Shot on {opponent.name} for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")
        
def holy_shield(player, opponent):
    damage = player.attack_power * 0.2
    opponent.health -= damage
    print(f"\n{player.name} blesses their Holy Shield and throws it at {opponent.name} for {damage} damage! The Holy Shield returns to {player.name}!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")