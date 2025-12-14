#ES 1 implementation
import random
stats = {
    "intelligence": 75,
    "social_life": 75,
    "happiness": 75,
    "emotional_damage": 25,
    "depression": 0
}
information = {
    1: "You hit me!!", 
    2: "You cheated on me multiple times!!",
    3: "You lied a lot.", 
    4: "You ghosted me.",
    5: "You talked to your ex.",
    6: "You never said sorry.",
    7: "You blamed me.",
    8: "You embarrassed me.",
    9: "You flirted with others.",
    10: "You ignored my feelings.",
    11: "You made me anxious.", 
    12: "You broke every promise.",
    13: "You made me doubt myself.", 
    14: "You made fun of me.",
    15: "You didnt support me.", 
    16: "You tried to control me.",
    17: "You didnt listen.", 
    18: "You started fights.",
    19: "You didnt care enough.", 
    20: "You guilt-tripped me.",
    21: "You used my insecurities.", 
    22: "You compared me.",
    23: "You stopped trying.", 
    24: "You assumed the worst.",
    25: "You made me feel alone."
}
info_gathered = {
}
actions_room = ["1)rest", "2)check phone", "3)drawing"]
actions_school = ["1)talk to favorite teacher", "2)sneak into principals office", "3)get in a fight"]
actions_friendshouse = ["1)play video games", "2)talk", "3)start a fight"]
actions_kitchen = ["1)eat", "2)cook", "3)make matcha", "4)check fridge"]
actions_cementary = ["1)talk to dead dad", "2)cry"]
actions_walmart = ["1)Shout to cashier", "2)steal"]
actions_park = ["1)chill", "2)run", "3)feed ducks"]
actions_backyard = ["1)go in the trampoline", "2)read", "3)mow the grass"]

def bedroom(stats, actions_room):
    while True:
        choice = input("What would you like to do?: ")
        if choice == "1" in actions_room:
            actions_room.remove("1)rest")
            print("You got one of the best rest of your life.")
            print("Happiness +10")
            stats["happiness"] += 10
            print("Intelligence -5")
            stats["intelligence"] -= 5
            break

        elif choice == "2" in actions_room:
            actions_room.remove("2)check phone")
            print("You went through your phone and saw how your ex treated you")
            print("Intellince -10")
            stats["intelligence"] -= 10
            print("Happiness +10")
            stats["happiness"] += 10
            print("Social life +10")
            stats["social_life"] += 10
            num = random.randint(1, 25)
            info_gathered[num] = information[num]
            print(f"Information has been gathered: {information[num]}")
            break

        elif choice == "3" in actions_room:
            actions_room.remove("3)drawing")
            print("Your drawing made you relaxed.")
            print("Intelligence +10")
            stats["intelligence"] += 10
            print("Happiness+15")
            stats["happiness"] += 15
            print("emotional damage -5")
            stats["emotional_damage"] -= 5
            break

def school(stats, actions_school):
    while True:
        choice = input("What would you like to do?: ")
        if choice == "1" in actions_school:
            actions_school.remove("1)talk to favorite teacher")
            print("Your teacher gave you great advice and you relise what your worth.")
            print("Intelligence +5")
            stats["intelligence"] += 10
            print("Happiness +5")
            stats["happiness"] += 5
            num = random.randint(1, 25)
            info_gathered[num] = information[num]
            print(f"Information has been gathered: {information[num]}")
            break

        elif choice == "2" in actions_school:
            actions_school.remove("2)sneak into principals office")
            print("You sneaked into the principals office to find aswers ")
            print("Intelligence -15")
            stats["intelligence"] -= 15
            print("Social life -15")
            stats["social_life"] -= 15
            break

        elif choice == "3" in actions_school:
            actions_school.remove("3)get in a fight")
            fight = random.randint(1, 2)
            if fight == 1:
                print("You won and you have so much aura.")
                print("social life +15")
                stats["social_life"] += 15
                print("happiness +5")
                stats["happiness"] += 5
                print("emotinal damage -15")
                stats["emotional_damage"] -= 15
            else:
                print("You lost and everyone is laughing at you.")
                print("social life -15")
                stats["social_life"] -= 15
                print("happiness -10")
                stats["happiness"] -= 10
                print("emotinal damage +15")
                stats["emotional_damage"] += 15
            break

def friends_house(stats, actions_friendshouse):
    while True:
        choice = input("what would you like to do?: ")
        if choice == "1" in actions_friendshouse:
            actions_friendshouse.remove("1)play video games")
            game = random.randint(1, 2)
            if game == 1:
                print("You are playing minecraft, it is a chill game")
                print("Happiness +10")
                stats["happiness"] += 10
            else:
                print("You and your friend are playing call of duty, you guys are fighting now")
                print("Happiness -10")
                stats["happiness"] -= 10
            break

        elif choice == "2" in actions_friendshouse:
            actions_friendshouse.remove("2)talk")
            print("You guys are having a peacefull converstaion")
            print("Happiness +10")
            stats["happiness"] += 10
            break

        elif choice == "3" in actions_friendshouse:
            actions_friendshouse.remove("3)start a fight")
            print("Welp, you started a fight, your friendship is not as strong anymore.")
            print("Social life -10")
            print("Happines -5")
            stats["social_life"] -= 10
            stats["happiness"] -= 5
            break

def kitchen(stats, actions_kitchen):
    print("You have entered the the kitchen")
    print("Oh no. Your mom is mad at you for not cleaning the dishes.")
    dishes1 = input("What would you like to say?: A) @$$#!  B) I will do them in a sec  C) I'm sorry, please select the letter").upper()

    if dishes1 == "A":
        print("Your mom is so mad at you she grounded you for a week, you can't go out, but you felt good.")
        print("Emotional damage +15. Happiness +1")
        stats["emotional_damage"] += 10
        stats["happiness"] += 15

    elif dishes1 == "B":
        print("She said that now is not the time, she grounded you for a day")
        print("Emotional damage +15")
        stats["emotional_damage"] += 15

    elif dishes1 == "C":
        print("She is way more mad at you for saying sorry and not fixing the problem.")
        print("Emotional damage +10")
        stats["emotional_damage"] += 10

    while True:
        choice = input("what would you like to do now?: ")
        if choice == "1" in actions_kitchen:
            actions_kitchen.remove("1)eat")
            print("You are feelling great and you are happy.")
            print("Happiness +10. Emotional damage -5")
            stats["happiness"] += 10
            stats["emotional_damage"] -= 5
            break

        elif choice == "2" in actions_kitchen:
            actions_kitchen.remove("2)cook")
            print("You are crazy good at cooking")
            print("Intelligence +5.  happiness +5")
            stats["intelligence"] += 5
            stats["happiness"] += 5
            break

        elif choice == "3" in actions_kitchen:
            actions_kitchen.remove("3)make matcha")
            print("You are the biggest perfomative person!!, you are sooo tuff")
            print("Intelligence +5, social life +10, happiness +5, emotional damage -5")
            stats["intelligence"] += 5
            stats["social_life"] += 10
            stats["happiness"] += 5
            stats["emotional_damage"] -= 5
            break

        elif choice == "4" in actions_kitchen:
            actions_kitchen.remove("4)check fridge")
            print("you check the fridge and theres nothing :(")
            print("happiness -5")
            stats["happiness"] -= 5
            break

def cementary(stats, actions_cementary):
    while True:
        choice = input("What would you like to do now?:")
        if choice == "1" in actions_cementary:
            actions_cementary.remove("1)talk to dead dad")
            print("You are crying now, thinking of the old times. Then you remember important stuff")
            print("Happiness -20, Emotional damage +20")
            stats["emotional_damage"] += 20
            stats["happiness"] -= 20
            for _ in range(2):
                num = random.randint(1, 25)
                info_gathered[num] = information[num]
                print(f"Information has been gathered: {information[num]}")
            break

        elif choice == "2" in actions_cementary:
            actions_cementary.remove("2)cry")
            print("It is a hard time, but you let your feelings out. Nothing happends but memories.")
            for _ in range(2):
                num = random.randint(1, 25)
                info_gathered[num] = information[num]
                print(f"Information has been gathered: {information[num]}")
            print("Happiness -20")
            stats["happiness"] -= 20
            break

def walmart(stats, actions_walmart):
    while True:
        choice = input("What would you like to do now?: ")
        if choice == "1" in actions_walmart:
            actions_walmart.remove("1)Shout to cashier")
            print("WHY DO YOU SHOUT TO PLEPLE")
            print("social life -10")
            stats["social_life"] -= 10
            break

        elif choice == "2" in actions_walmart:
            actions_walmart.remove("2)steal")
            print("You stole from walrmart")
            print("intelligence -10")
            stats["intelligence"] -= 10
            final_battle(stats)
            break

def park(stats, actions_park):
    while True:
        choice = input("What would you like to do now")
        if choice == "1" in actions_park:
            actions_park.remove("1)chill")
            print("You are such a chill guy")
            print("Emotional damage -5")
            stats["emotional_damage"] -= 5
            break

        elif choice == "2" in actions_park:
            actions_park.remove("2)run")
            print("You fell relaxed")
            print("emotional damage -5")
            stats["emotional_damage"] -= 5
            break

        elif choice == "3" in actions_park:
            actions_park.remove("3)feed ducks")
            print("The bully at your school saw you and now is making fun of you")
            print("Social life -10")
            stats["social_life"] -= 10
            break

def backyard(stats, actions_backyard):
    while True:
        choice = input("What would you like to do now")
        if choice == "1" in actions_backyard:
            actions_backyard.remove("1)go in the trampoline")
            print("You jump around and feel happier")
            print("Happiness +5")
            stats["happiness"] += 5
            break

        elif choice == "2" in actions_backyard:
            actions_backyard.remove("2)read")
            print("You read a good book and feel smarter")
            print("Intelligence +5")
            stats["intelligence"] += 5
            break

        elif choice == "3" in actions_backyard:
            actions_backyard.remove("3)mow the grass")
            print("It was tiring, but your parents are proud of you")
            print("Emotional damage -5")
            stats["emotional_damage"] -= 5
            break

def final_battle(stats):
    print("You are in the final battle now for stealing from walmart. ")
    print("Your ex saw you and is now telling everyone you were bad person")
    print(info_gathered)

    ex_emotional_damage = 25

    while ex_emotional_damage < 100 and stats["emotional_damage"] < 100:
        print("Your emotional damage:", stats["emotional_damage"])
        print("Ex emotional damage:", ex_emotional_damage)

        if not info_gathered:
            break

        for key in info_gathered:
            print(key, ":", info_gathered[key])

        num = int(input("Pick the number you want to use: "))
        if num in info_gathered:
            print("You say:", info_gathered[num])
            ex_emotional_damage += 20
            stats["emotional_damage"] -= 5
            del info_gathered[num]
        else:
            stats["emotional_damage"] += 10

print("This game is about you as a teenage self, the goal of this game is to win an argument against your ex in a text message fight about whose fault it was about the break up.")
while True:
    places = ["bedroom", "school", "friends house", "kitchen", "cementary", "walmart", "park", "backyard"]
    print("The places you can go to are the following:")
    for place in places:
        print(place)
    where = input("Where would you like to go?: ").lower()
    if where == "bedroom":
        print("You are in your room.")
        for action in actions_room:
            print(action)
        bedroom(stats, actions_room)
        if stats["depression"] >= 100:
            print("You are too depressed to continue. Game over.")
            break
    elif where == "school":
        print("You have decided to go to school")
        for action in actions_school:
            print(action)
        school(stats, actions_school)
        if stats["depression"] >= 100:
            print("You are too depressed to continue. Game over.")
            break
    elif where == "friends house":
        print("You are in your friends house")
        for action in actions_friendshouse:
            print(action)
        friends_house(stats, actions_friendshouse)
        if stats["depression"] >= 100:
            print("You are too depressed to continue. Game over.")
            break
    elif where == "kitchen":
        for action in actions_kitchen:
            print(action)
        kitchen(stats, actions_kitchen)
        if stats["depression"] >= 100:
            print("You are too depressed to continue. Game over.")
            break
    elif where == "cementary":
        print("You have entered the cementary")
        for action in actions_cementary:
            print(action)
        cementary(stats, actions_cementary)
        if stats["depression"] >= 100:
            print("You are too depressed to continue. Game over.")
            break
    elif where == "walmart":
        print("You have entered walmart")
        for action in actions_walmart:
            print(action)
        walmart(stats, actions_walmart)
        if stats["depression"] >= 100:
            print("You are too depressed to continue. Game over.")
            break
    elif where == "park":
        print("You are at the park")
        for action in actions_park:
            print(action)
        park(stats, actions_park)
        if stats["depression"] >= 100:
            print("You are too depressed to continue. Game over.")
            break
    elif where == "backyard":
        print("You are in your backyard")
        for action in actions_backyard:
            print(action)
        backyard(stats, actions_backyard)
        if stats["depression"] >= 100:
            print("You are too depressed to continue. Game over.")
            break