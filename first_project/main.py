def final(items):
    print("welcome to the final door of the game, in this part you will need to fight the monster")
    fight = int(input("press 34567893465 to punch the monster or press 45 to get punched"))
    if fight == 34567893465:
        print("The monster lost 10 damage 4 hits left")
    elif fight == 45:
        print("oh no the monster hit you") 
        fighting_again = int(input("you won the first time try winning now hahaha... to punch him press 67 to get punched press 76"))
        if fighting_again == 67:
            print("hahaha i tricked you now you only have 5 health left")
        elif fighting_again == 76:
            print("you are smart you made the monster lose 35 health")
        else:
            print("you died")
    else:
        print("please select an actual answer")
        die = True 
        last_fight = int(input("Dont get tricked press 898998 to hit the monster or press 676776 to get beat up"))
        if last_fight == 898998:
            print("YOU SURVIVED AMAZING JOB WOOHOO")
        elif last_fight == 676776: 
            print("OH NO YOU DIED BOOHOO")
            die = True 
        else:
            print("you died")
            die = True 
            return final(items)

while True:
    choice = print("dka;d")
    if choice == "final":
        final(items)