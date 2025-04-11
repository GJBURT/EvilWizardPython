# Warrior abilities
# Warrior Rage increases the warrior's attack power for a short duration and stacks with each use
def rage(player):
    player.attack_power *= 1.5  # Increase attack power by 50%
    print(f"\n{player.name} uses Rage, increasing attack power to {player.attack_power:.2f}!")

# Warrior Shield Bash
def shield_bash(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} uses Shield Bash on {opponent.name} for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")

# Mage abilities
# Mage Mana Shield grants the mage a shield that absorbs damage
def mana_shield(player):
    shield_amount = player.max_health * 0.25  # 25% of max health
    player.health += shield_amount
    print(f"\n{player.name} casts Mana Shield, gaining {shield_amount} protection! Current health: {player.health}")
    if player.health > player.max_health:
        player.health = player.max_health  # Ensure health does not exceed max health

# Mage Fireball
def fireball(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} uses Fireball on {opponent.name} for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")

# Necromancer abilities
# Necromancer Bone Armor granting the necromancer a shield that absorbs damage
def bone_armor(player):
    shield_amount = player.max_health * 0.25  # 25% of max health
    player.health += shield_amount
    print(f"\n{player.name} summons Bone Armor, gaining {shield_amount} protection! Current health: {player.health}")
    if player.health > player.max_health:
        player.health = player.max_health  # Ensure health does not exceed max health

# Necromancer Summon Undead
def summon_undead(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} summons an undead minion to attack {opponent.name} for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")

# Necromancer Soul Siphon
def soul_siphon(self, target):
        """Drain health from the target and heal the Necromancer."""
        drained_health = self.max_health * 0.1  # 10% of Necromancer's max health
        target.health -= drained_health
        self.health += drained_health
        print(f"{self.name} used Soul Siphon on {target.name}, draining {drained_health} health! {self.name}'s health is now {self.health}.")

# Rogue abilities
# Rogue Shadow Dance creates a shadow images of the rogue granting the rogue a chance to dodge the next attack
# and the rogue can attack twice in one turn
def shadow_dance(player, opponent):
    dodge_chance = 0.5  # 50% chance to dodge the next attack
    player.dodge_chance = dodge_chance
    print(f"\n{player.name} enters Shadow Dance, gaining a {dodge_chance * 100}% chance to dodge the next attack!")
    if player.dodge_chance:
        print(f"{player.name} dodged the attack!")
    else:
        print(f"{player.name} failed to dodge the attack!")

# Rogue Backstab        
def backstab(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} vanishes in a puff of smoke reappearing behind {opponent.name} and uses Backstab for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")

# Archer abilities
# Archer Rapid Fire ability
def rapid_fire(player, opponent):
    damage = player.attack_power * 1.5  # Deal 1.5x attack power as damage
    opponent.health -= damage
    opponent.skip_turn = True  # Set the skip_turn flag for the opponent
    print(f"\n{player.name} uses Rapid Fire on {opponent.name} for {damage:.2f} damage!")
    print(f"{opponent.name} is stunned and will miss their next turn!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")

# Archer Power Shot       
def power_shot(player, opponent):
    damage = player.attack_power * 3  # Increased damage for Power Shot
    opponent.health -= damage
    print(f"\n{player.name} uses Power Shot on {opponent.name} for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")

# Paladin abilities
# Paladin Divine Strike
def divine_strike(player, opponent):
    damage = player.attack_power * 2
    opponent.health -= damage
    print(f"\n{player.name} strikes {opponent.name} with Divine Strike for {damage} damage!")
    if opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")

# Paladin Holy Shield that will apply protection to the paladin on the next turn
def holy_shield(player):
    shield_amount = player.max_health * 0.25  # 25% of max health
    player.health += shield_amount
    print(f"\n{player.name} blesses their Holy Shield, gaining {shield_amount} protection! Current health: {player.health}")
    if player.health > player.max_health:
        player.health = player.max_health  # Ensure health does not exceed max health    

# Paladin Holy Light Heal
def holy_light(player):
    heal_amount = player.holy_light_amount
    player.health += heal_amount
    print(f"\n{player.name} uses Holy Light and heals for {heal_amount} health! Current health: {player.health}")
    if player.health > player.max_health:
        player.health = player.max_health  # Ensure health does not exceed max health