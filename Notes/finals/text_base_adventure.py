#ES 1 text base adventure
import random
stats = {
    "intelligence" : 75,
    "social_life" : 75,
    "happiness" : 75,
    "emotional_damage" : 25,
    "depression" : 0
}
information = {
    1 : "You hit me!!",
    2 : "You cheated on me multiple times!!",
    3 : "You lied a lot.",
    4 : "You ghosted me.",
    5 : "You talked to your ex.",
    6 : "You never said sorry.",
    7 : "You blamed me.",
    8 : "You embarrassed me.",
    9 : "You flirted with others.",
    10 : "You ignored my feelings.",
    11 : "You made me anxious.",
    12 : "You broke every promise.",
    13 : "You made me doubt myself.",
    14 : "You made fun of me.",
    15 : "You didnt support me.",
    16 : "You tried to control me.",
    17 : "You didnt listen.",
    18 : "You started fights.",
    19 : "You didnt care enough.",
    20 : "You guilt-tripped me.",
    21 : "You used my insecurities.",
    22 : "You compared me.",
    23 : "You stopped trying.",
    24 : "You assumed the worst.",
    25 : "You made me feel alone."
}
info_gathered = {
}


def bedroom(stats):
    while True:

        choice = input("What would you like to do?: ")
        if choice == "rest":
            actions_room.remove("rest")
            print("You got one of the best rest of your life.")
            print("Happiness +10")
            stats["happiness"] += 10
            print("Intelligence -5")
            stats["intelligence"] -= 5
            if "intelligence" == 0:
                stats["depression"] +=20
            print(stats)
            break
        elif choice == "check phone":
            print("You went through your phone and saw how your ex treated you")
            actions_room.remove("check phone")
            print("Intellince -10")
            stats["intelligence"] -=10
            if stats["intelligence"] <= 0:
                stats["depression"] +=20
            print("Happiness +10")
            stats["happiness"] += 10
            print("Social life +10")
            stats["social_life"] += 10
            print(stats)
            num = random.randint(1,25)
            info_gathered[num] = information[num]
            print(f"Information has been gathered: {information[num]}")
            break
        elif choice == "drawing":
            print("Your drawing made you relaxed.")
            actions_room.remove("drawing")
            print("Intelligence +10")
            stats["intelligence"] +=10
            print("Happiness+15")
            stats["happiness"] += 15
            print("emotional damage -5")
            stats["emotional_damage"] -= 5
            break
        else:
            print("please select an actual option")
            continue
    return

def school(stats):
    while True:
        choice = input("What would you like to do?: ")
        if choice == "1":
            print("Your teacher gave you great advice and you relise what your worth.")
            actions_school.remove("1)talk to favorite teacher")
            print("Intelligence +5")
            stats["intelligence"] +=10
            print("Happiness +5")
            stats["happiness"] +=5
            num = random.randint(1,25)
            info_gathered[num] = information[num]
            print(f"Information has been gathered: {information[num]}")
            actions_school.remove("1)talk to favorite teacher")
            break
        elif choice == "2":
            print("You sneaked into the principals office to find aswers ")

            print("Intelligence -15")
            stats["intelligence"] -=15
            if stats["intelligence"] <= 0:
                stats["depression"] +=20
            print("Social life -15")
            stats["social_life"] -=15
            if stats["social_life"] <= 0:
                stats["depression"] +=20
            principals_of = random.randint(1,2)
            if principals_of == 1:
                print("You dint find anything in the ofice.")
            
            elif principals_of == 2:
                for i in range(2):
                    num = random.randint(1,25)
                    info_gathered[num] = information[num]
                    print(f"Information has been gathered: {information[num]}")
            else:
                print("skdlja")
            break
        elif choice =="3":
            fight = random.randint(1,2)
            if fight == 1:
                print("You won and you have so much aura.")
                print("social life +15")
                stats["social_life"] +=15
                print("happiness +5")
                stats["happiness"] +=5
                print("emotinal damage -15")
                stats["emotional_damage"] -=15
                actions_school.remove("3)get in a fight")
                break
            else:
                print("You lost and everyone is laughing at you.")
                print("social life -15")
                stats["social_life"] -=15
                if stats["social_life"] <= 0:
                    stats["depression"] +=20
                print("happiness -10")
                stats["happiness"] -=10
                if stats["happiness"] <= 0:
                    stats["depression"] +=20
                print("emotinal damage +15")
                stats["emotional_damage"] +=15
                if stats["emotional_damage"] >= 100:
                    stats["depression"] +=20
                actions_school.remove("3)get in a fight")
            break
        else:
            print("Maybe you spelled something wrong, you might wanna check again.")
            continue
    return

def friends_house(stats):
    while True:
        choice = input("what would you like to do?: ")
        if choice == "play video games":
            game = random.randint(1,2)
            if game == 1:
                print("You are playing minecraft, it is a chill game")
                print("Happiness +10")
                stats["happiness"] +=10
                actions_friendshouse.remove("play video games")
            else:
                print("You and your friend are playing call of duty, you guys are fighting now")
                print("Happiness -10")
                stats["happiness"] -=10
                if stats["happiness"] <= 0:
                    stats["depression"] +=20
                print("Emotional damage +10")
                stats["emotional_damage"] +=10
                if stats["emotional_damage"] >= 100:
                    stats["depression"] +=20
                actions_friendshouse.remove("play video games")
                break
        elif choice == "talk":
            print("You guys are having a peacefull converstaion")
            print("Happiness +10")
            stats["happiness"]+=10
            actions_friendshouse.remove("talk")
            break
        elif choice == "start a fight":
            print("Welp, you started a fight, your friendship is not as strong anymore.")
            print("Social life -10")
            print("Happines -5")
            stats["social_life"] -=10
            if stats["social_life"] <= 0:
                    stats["depression"] +=20
            stats["happiness"] -=5
            if stats["happiness"] <= 0:
                    stats["depression"] +=20
            actions_friendshouse.remove("start a fight")
            break
        else:
            print("maybe you selected something wrong, plese select again")
            continue
    return

def kitchen(stats):
    print("You have entered the the kitchen")
    print("Oh no. Your mom is mad at you for not cleaning the dishes.")
    dishes1 = input("What would you like to say?: A) @$$#!  B) I will do them in a sec  C) I'm sorry, please select the letter").upper()
    if dishes1 == "A":
        print("Your mom is so mad at you she grounded you for a week, you can't go out, but you felt good.")
        print("Emotional damage +15. Happiness +1")
        stats["emotional_damage"] +=10
        if stats["emotional_damage"] >= 100:
                stats["depression"] +=20
        stats["happiness"]+=15
    elif dishes1 == "B":
            print("She said that now is not the time, she grounded you for a day")
            print("Emotional damage +15")
            stats["emotional_damage"] +=15
            if stats["emotional_damage"] >= 100:
                stats["depression"] +=20
    elif dishes1 == "C":
        print("She is way more mad at you for saying sorry and not fixing the problem.")
        print("Emotional damage +10")
        stats["emotional_damage"] +=10
        if stats["emotional_damage"] >= 100:
            stats["depression"] +=20
    else:
        print("Maybe you selected an wrong option please select an actual opition.")
    while True:
        choice = input("what would you like to do now")
        if choice == "eat":
            print("You are feelling great and you are happy.")
            print("Happiness +10. Emotional damage -5")
            stats["happiness"]+=10
            stats["emotional_damage"]-=5
            break
        elif choice == "cook":
            print("You are crazy good at cooking")
            print("Intelligence +5.  happiness +5")
            stats["intelligence"]+=5
            stats["happiness"]+=5
            break
        elif choice == "make mathcha":
            print("You are the biggest perfomative person!!, you are sooo tuff")
            print("Intelligence +5, social life +10, happiness +5, emotional damage -5")
            stats["intelligence"]+=5
            stats["social_life"]+=10
            stats["happiness"]+=5
            stats["emotional damage"]-=5
        elif choice == "check fridge":
            print("you check the fridge and theres nothing :(")
            print("happiness -5")
            stats["happiness"]-=5
            if stats["happiness"] <= 0:
                    stats["depression"] +=20
            break
        else:
            print("Maybe you spelled something wrong, please select something right")
            continue
    return

def cementary(stats):
    while True:
        choice = input("What would you like to do now")
        if choice == "talk to dead dad":
            print("You are crying now, thinking of the old times. Then you remember important stuff")
            print("Happiness -20, Emotional damage +20")
            stats["emotional_damage"] +=20
            if stats["emotional_damage"] >= 100:
                    stats["depression"] +=20
            stats["happiness"]-=20
            if stats["happiness"] <= 0:
                    stats["depression"] +=20
            for i in range(2):
                    num = random.randint(1,25)
                    info_gathered[num] = information[num]
                    print(f"Information has been gathered: {information[num]}")
        elif choice == "cry":
            print("It is a hard time, but you let your feelings out. Nothing happends but memories.")
            for i in range(2):
                    num = random.randint(1,25)
                    info_gathered[num] = information[num]
                    print(f"Information has been gathered: {information[num]}")
            print("Happiness -20")
            stats["happiness"] -20
            if stats["happiness"] <= 0:
                    stats["depression"] +=20

def walmart(stats):
    print("You have entered walmart")
    actions_walmart = ["Shout to cashier","steal"]
    print(f"The actions you can do are the following")
    for action in actions_walmart:
        print(action)
    while True:
        choice = input("What would you like to do now")
        if choice == "shout to cashier":
            print("WHY DO YOU SHOUT TO PLEPLE")
            print("social life -10")
            stats["social_life"] -=10
            if stats["social_life"] <= 0:
                    stats["depression"] +=20
        elif choice == "steal":
            print("You stole from walrmart")    

def park(stats):
    print("You are at the park")
    actions_park = ["chill","run","feed ducks"]
    print(f"Then actions you can do are the following: ")
    for action in actions_park:
        print(action)
        while True:
            choice = input("What would you like to do now")

def backyard(stats):
    print("You are in your backyard")
    actions_backyard = ["go in the trampoline","read","mow the grass"]
    print(f"Then actions you can do are the following: ")
    for action in actions_backyard:
        print(action)
        while True:
            choice = input("What would you like to do now")

def final_battle(stats):
    print("You are in the final battle now for stealing from walmart. ")
    print("Your ex saw you and is now telling everyone you were bad person")
    print(info_gathered)
print("This game is about you as a teenage self, the goal of this game is to win an argument against your ex in a text message fight about whose fault it was about the break up. In this game you will go through what it feels to be a Ucas student, you have a crazy mom and a crazy ex that is still bugging you about the break up. The obstacles in this game are keeping your grades acceptable, having a social life, doing most of your chores around the house, and dealing with the people in your life. You win this game by defeating the final boss, your ex, the two of you are going to be in an argument of whose fault was it about the break up, the life would be measured as emotional damage, the better you handle the obstacles, the less emotional damage you have, (by the way, if you read this i owe you  a penny) during the fight you can bring up stuff your ex did to you or how bad she was, you can find these useful things in the rooms around the house hidden. Finally, the game would give you options to choose from, and you have to choose the best one. Good luck and hope you live. :)")
while True:
    while 0 < stats["depression"]:
        True
    while 0 >= stats["depression"]:
        False
        break
    while True:
        places = ["bedroom", "school","friends house","kitchen", "cementary", "walmart","park","backyard"]
        print(f"The places you can go to are the following:")
        for there in places:
            print(there)
        where = input("where would you like to go?: ")
        if where == "bedroom":
            print("You are in your room.")
            actions_room = ["rest", "check phone", "drawing"]
            print(f"The actions are: ")
            for action in actions_room:
                print(action)
            bedroom(stats)
        elif where == "school":
            print("You have decided to go to school")
            actions_school = ["1)talk to favorite teacher", "2)sneak into principals office", "3)get in a fight"]
            print(f"The actions you can do are the following")
            for action in actions_school:
                print(action)
            school(stats)
        elif where == "friends house":
            print("You are in your friends house")
            actions_friendshouse = ["play video games","talk","start a fight"]
            print(f"The actions you can do are the following")
            for action in actions_friendshouse:
                print(action)
            friends_house(stats)
        elif where == "kitchen":
            actions_kitchen = ["eat","cook","make matcha","check fridge"]
            print(f"The actions you can do are the following:")
            for action in actions_kitchen:
                print(action)
            kitchen(stats)
        elif where == "cementary":
            print("You have entered the cementary")
            actions_cementary = ["talk to dead dad","cry"]
            print(f"The actions you can do are the following:")
            for action in actions_cementary:
                print(action)
            cementary(stats)   
        elif where == "walmart":

            walmart(stats)
        elif where == "park":

            park(stats)
        elif where == "backyard":

            backyard(stats)
        else:
            print("You maybe spelled something wrong, please re-type")
            continue