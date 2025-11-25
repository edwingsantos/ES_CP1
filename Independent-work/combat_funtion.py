#ES 1 combat fucntion 
import random 

print("Welcome to training! First I need to know some things about you!")
input("what is your name?: ")
class_fighter = int(input("What class of fighter are you?" \
"1 if you are a fighter " \
"2 if you are a Mage " \
"3 if you are a Rouge: " ))

def class_fighter(fighter):
    if class_fighter == 1:
            print("You are a fighter, here are your stats: " \
        "Health: 30 " \
        "Damage: 23 ")
def class_fighter(Mage):
    if class_fighter == 2:
         print("You are a Mage, here are your stats: " \
        "Health: 35 " \
        "Damage: 19")
def class_fighter(fighter):
    if class_fighter == 3:
         print("You are a Rouge, here are your stats: " \
        "Health: 45 " \
        "Damage: 15" )
    
order = random.randint(1,2)


if order == 1:
     print("A Monster is attacking you, quick choose your attack ")
else:
     print("A Moster is attacking ")
     #hi 