#ES 1 combat fucntion 
import random 
def player_choice():
print("Welcome to training! First I need to know some things about you!")
input("what is your name?: ")
class_fighter = input("What class of fighter are you?" \
"1 if you are a fighter " \
"2 if you are a Mage " \
"3 if you are a Rouge: " )
while True:
    if class_fighter == 1:
        print("You are a fighter, here are your stats: " \
        "Health: 30 " \
        "Damage: 23 ")
        break
    elif class_fighter == 2:
         print("You are a Mage, here are your stats: " \
        "Health: 35 " \
        "Damage: 19")
         break
    else:
         print("You are a Rouge, here are your stats: " \
        "Health: 45 " \
        "Damage: 15" )
         break
    
scenario = random.randint(1,5)


if scenario == 1:
    print("The scenario is the hunted cave: Opponet is batman " \
    "Health 45 Damage: 25")
    


