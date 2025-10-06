#ES 1 rock paper scisors 

import random


choice = random.randint(1,3)
rock = 1
paper = 2
scisors = 3
user = int(input("Choose rock(1), paper(2), scisors(3): "))
count = 1
win = "You won"


while True:
    if choice == 1:
        print("conputer choose rock ")
    elif user == 3:
        print("you lost")
    elif user == 2:
        print(win)
    elif user == 1:
        print("its a tie")
        if win:
            break
    if choice == 2:
        print("conputer choose paper ")
    elif user == 1:
        print("you lost")
    elif user == 3:
        print(win)
    elif user == 2:
        print("its a tie")
        if win:
            break
    if choice == 3:
        print("conputer choose scisors ")
    elif user == 2:
        print("you lost")
    elif user == 1:
        print(win)
    elif user == 3:
        print("its a tie")
    if win:
            break 
        
        



     
