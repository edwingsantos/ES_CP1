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
    1 : "You hit me!!"
    #come up with the other 24
}


info_gathered = []

print("This game is about you as a teenage self, the goal of this game is to win an argument against your ex in a text message fight about whose fault it was about the break up. In this game you will go through what it feels to be a Ucas student, you have a crazy mom and a crazy ex that is still bugging you about the break up. The obstacles in this game are keeping your grades acceptable, having a social life, doing most of your chores around the house, and dealing with the people in your life. You win this game by defeating the final boss, your ex, the two of you are going to be in an argument of whose fault was it about the break up, the life would be measured as emotional damage, the better you handle the obstacles, the less emotional damage you have, (by the way, if you read this i owe you  a penny) during the fight you can bring up stuff your ex did to you or how bad she was, you can find these useful things in the rooms around the house hidden. Finally, the game would give you options to choose from, and you have to choose the best one. Good luck and hope you live. :)")
def bedroom():
    print("You are in your room.")
    actions_room = ["rest", "cheking phone", "drawing"]
    print(actions_room)
    while True:
        choice = input("What would you like to do?: ")
        if choice == "rest":
            print("You have dicided to rest. The action rest woul be taken off the actions for bedroom")
            actions_room.remove("rest")

            stats["happiness"] += 10
            stats["intelligence"] -= 5
            print(stats)


where = input("where would you like to go?: ")
if where == "bedroom":
    bedroom()