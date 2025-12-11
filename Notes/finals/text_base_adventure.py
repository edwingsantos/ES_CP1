#ES 1 text base adventure
import random

stats = {
    'intelligence' : 75,
    'social_life' : 75,
    'happiness' : 75,
    'emotional_damage' : 25,
    'depression' : 0
}

information = {
    1 : "You hit me!!",
    2 : "Hi"
    #come up with the other 24
}
info_gathered = {


}
places = ["bedroom", "school","friends house","kitchen", "cementary", "walmart","park","backyard"]

def bedroom(stats):
    print("You are in your room.")
    actions_room = ["rest", "check phone", "drawing"]
    print(f"The actions are: ")
    for action in actions_room:
        print(action)
    while True:
        choice = input("What would you like to do?: ")
        if choice == "rest":
            print("You have dicided to rest. The action rest woul be taken off the actions for bedroom")
            actions_room.remove("rest")
            stats["happiness"] += 10
            stats["intelligence"] -= 5
            if "intelligence" == 0:
                stats["depression"] +=20
            print(stats)
            break
        elif choice == "check phone":
            print("You have decided to check your phone this action would not be able to be accesed")
            actions_room.remove("check phone")
            print("Intellince -10")
            stats["intelligence"] -=10
            if stats["intelligence"] <= 0:
                stats["depression"] +=20
            stats["happiness"] += 10
            stats["social_life"] += 10
            print(stats)
            num = random.randint(1,2)
            if num == 1:
                print(f"You have gathered info for checking your phone. {information[1]}")
                info_gathered[1] = "You hit me!!"
                print(f"{info_gathered[1]}")
            elif num == 2:
                print(f"You have gathered info for checking your phone. {information[2]}")
                info_gathered[2] = "hi"
                print(f"{info_gathered[2]}")
            break
        elif choice == "drawing":
            print("You have decided to draw. This action would not be able to be accesed")
            actions_room.remove("drawing")
            stats["intelligence "] +=10
            stats["happiness"] += 15
            stats["emotional_damage"] -= 5
            break
        else:
            print("please select an actual option")
            continue
    return

def school(stats):
    print("You have decided to go to school")
    actions_school = ["talk to favorite teacher", "sneak into principals ofice", "get in a fight"]
    print(actions_school)
    while True:
        choice = input("What would you like to do?: ")
        if choice == "talk to favorite techer":
            print("You have dicided to talk to your fav teacher")

def friends_house(stats):
    print("You are in your friends house")

def kitchen(stats):
    #Make the fight with your mom  the first time you enter the kitchen , every time you enter it you have to fight, but you get more resources
    print("You have entered the the kitchen")

def cementary(stats):
    print("You have entered the cementary")

def walmart(stats):
    print("You have entered walmart")

def park(stats):
    print("You are at the park")

def backyard(stats):
    print("You are in your backyard")

print("This game is about you as a teenage self, the goal of this game is to win an argument against your ex in a text message fight about whose fault it was about the break up. In this game you will go through what it feels to be a Ucas student, you have a crazy mom and a crazy ex that is still bugging you about the break up. The obstacles in this game are keeping your grades acceptable, having a social life, doing most of your chores around the house, and dealing with the people in your life. You win this game by defeating the final boss, your ex, the two of you are going to be in an argument of whose fault was it about the break up, the life would be measured as emotional damage, the better you handle the obstacles, the less emotional damage you have, (by the way, if you read this i owe you  a penny) during the fight you can bring up stuff your ex did to you or how bad she was, you can find these useful things in the rooms around the house hidden. Finally, the game would give you options to choose from, and you have to choose the best one. Good luck and hope you live. :)")
while True:
    while "depression" < stats["depression"]:
        True
    if "depression" >= stats["depression"]:
        False
        break
    while True:
        where = input("where would you like to go?: ")
        if where == "bedroom":
            bedroom(stats)
            continue
        if where == "school":
            school(stats)
        if where == "school":
            school(stats)