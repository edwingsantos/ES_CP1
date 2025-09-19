#ES 1 conditional notes
import random
player_hp = 20
player_attack =5
player_defense =5
player_damage = 2

monsters_hp = 15
monster_attack = 13
monster__damage = 10
monster_defense = 2

hit_roll = random.randint(1,20) + player_attack
damage_roll = random.randint(1,8) + player_damage

if hit_roll == 20:
    print("You got a crit, that means you get to roll for damage twice!.")
    damage_roll = random.randint(1,8) + random.randint(1,8) + player_damage
    if damage_roll > monster_defense:
        print(f"you did {damage_roll-monster_defense}.")
        monsters_hp -= (damage_roll-monster_defense)
elif hit_roll == 1:
    print("You rolled a critical failure! Now the moster gets to attack you!")
    damage_roll = random.randint(1,12) + monster__damage
    player_hp -= (damage_roll - player_defense)
    print(f"The monster rolled {damage_roll}, your hp is now {player_hp}")
elif hit_roll >= 12:
    print(f"You hit! Roll for damage!.")
    damage_roll = random.randint(1,8) + player_damage
    if damage_roll > monster_defense:
        print(f"you did {damage_roll-monster_defense}.")
        monsters_hp -= (damage_roll-monster_defense)
    else:
        print("You did no damage.")
else:
    print("You missed.")

print("Your turn is over")



    