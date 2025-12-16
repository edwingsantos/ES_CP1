# MV 1st Doors final 
#MV 1st Doors Final Game 


#import random for the rooms
import random 
#start is True 
die = False

#Introduce the user to the game 
    #print("Welcome to doors! this is an adventure horror game")
start = print("Welcome to doors! This is a textbase adventure horror game")
    #Give the instuccions of how the game works 
start = print("in this game you will need to get through 50 doors all different and you will need to watch out for monsters and hints, You will need to survive until door 50 to complete the game if you die there is no coming back. Good luck :)")
start == print("These are the objects in the game")
doors_objects = {
        "Bandages" : "+20 health", 
        "Flashlights" : "safety when light turns off",
        "Candles" : "safety when lights turn off",
        "Keys" : "To unlock next room",
        "Food" : "+5 health", 
        "Cross" : "safety from monsters",
        "papers" : "Hints at keys in door 50",
        "lockpick" : "Replaces key",
        "vitamins" : "+5 health", 
    }


def entrance(items):
            key = int(input("Which key would you like to pick 1-3?"))
            if key == 1:
                print("wrong key try again")
            if key == 2: 
                        print("You got it the door unlocked")
            if key == 3:
                    print("wrong key try again")
                    return entrance(items) 


def hallway(items):
    print("In this hallway you have found a 3 drawer wardrobe which drawer would yoy like to open?")
    drawer = int(input("pick a drawer 1-3"))
    if drawer == 2:
        print("you got a bandaid")
    if drawer == 2: 
        ("ROAR! the monster bit you")
        user_stats == print(45/50)
    if drawer == 3:
        print("aww you found nothing :|")
        def room1(items):
            print("The door is locked find the key")
            check = int(input("if you would like to check the room press 1 or 2 for thecloset"))
            if check == 1:
                print("You found the key on the ground")
                print("chk chk...oh no..")
                whoops = int(input("There are 2 doors with different numbers which would you like to pick one or two"))
                if whoops == 2:
                    print("it unlocked! good choice")
                if whoops == 1:
                    print("oh no timmothy attacked you")
                    user_stats = print(35/50)
            if check == 2:
                print("oh no there is nothing")
                return hallway(items)
            
print(doors_objects)
user_stats = print("your beginning health is 50/50") 
user_speed = print("your beginning speed is 10/10")


def room2(items): 
    print("This room has a bed and a closet, would you like to explore?")
    wander = int(input("Press 1 to wander or press 2 to continue to the next room"))
    if wander == 1: 
        item = int(input("press 6 to explore the bed or press 7 to explore the closet... you can only pick one ;)"))
        if item == 6: 
            print("YOU FOUND A CROSS! THATS EXTRA LEGENDARY YOU CAN USE THIS ON A MONSTER TO CHAIN THEM")
        if item == 7: 
            print("There is nothing Womp Womp :)")
            return room2(items) 
            
def room3(items): 
    monster = int(input("would you like to explore? press 1 if yes press 2 to move through"))
    if monster <= 3: 
        rush = int(input("Oh no, the lights are flickerign press 10 to go to the closet press 67 to hide in the wardrobe"))
        if rush == 10: 
            print("YAY, YOU SURVIVED WOOHOOO")
        if rush == 67: 
            print("NOO MY DEAR FRIEND YOU DIED!")
            die = True 
            return room3(items) 

def room5(items): 
    locked_door = int(input("this room is locked press 76 to check the bed and 89 to check the closet to find the key"))
    if locked_door == 89:
        check = int(input("To check the bed now press 99"))
        if check == 99: 
            locked = int(input("Good job.. you found a lockpick press 3 to use it"))
            if locked == 3:
                print("Great job lets move on")
            if locked_door == 76: 
                locked = int(input("Good job.. you found a lockpick press 3 to use it"))
                if locked == 3: 
                    print("great job lets move on")
                    return room5(items)


def room6(items): 
    hallway_locked = int(input("You are now in a hallway that has a locked door.. press 3 to go left, press 100 to turn right or press 45 to go straight ahead"))
    if hallway_locked == 3:
        beds = int(input("there is a bed a drawer and a typewriter press 1 to search the bed press 8 to checck the drawer and 67 to check the typewriter "))
        if beds == 1: 
            print("theres nothing there")
            check = int(input("press 8 to check the drawer and 67 to check the typewriter"))
            if check == 8: 
                print("theres nothing there")
                check_again = int(input("press 67 to check the typewriter"))
                if check_again == 67: 
                    print("there's nothing there..")
        if beds == 8:
            print("theres nothing there") 
            check = int(input("press 1 to check the bed and 67 to check the typewriter"))
            if check == 1: 
                print("theres nothing there")
                check_again = int(input("press 67 to check the typewriter"))
                if check_again == 67: 
                    print("there's nothing there..")
        if beds == 67: 
            print("There's nothing there..")
            check = int(input("press 1 to check the bed and 8 to check the drawer"))
            if check == 1: 
                print("theres nothing there")
                check_again = int(input("press 8 to check the drawer"))
                if check_again == 8: 
                    print("there's nothing there..")
        if hallway_locked == 100: 
            typewriter = int(input("This room has a bed and a wardrobe press 45 to check the bed or press 60 to check the wardrobe beware you can only pick one.."))
            if typewriter == 60: 
                print("oh no there is nothing there..")
            if typewriter == 45: 
                print("youuu found the key!")
                return room6(items) 



def room7(items):
    eyes = int(input("This room has a monster turn left(press 5) to escape it"))
    if eyes == 5: 
        print("good job you survived!")
    else: 
        print("you died") 
        die = True 
        return room7(items)

def room8(items): 
    print("You have reached the outdoors you are in the courtyard you need a ket to get back in")
    direction = int(input("Would you like to go left = 1, right = 2, forward = 4?"))
    if direction == 1: 
        print("you found an empty chest")
    if direction == 2: 
        print("You found a lockpick")
        lockpick = int(input("Press 6 to use the lockpick"))
        if lockpick == 6:
            print("Great you moved on")
        else: 
            ("let's continue")
    if direction == 4: 
        print("you found the key!..good luck in the next part..")
        return room8(items)


def chase(running): 
    print("woah you have reached a long hallway")
    run = int(input("Press 7 to continue")) 
    if run == 7:
        print("OH NO SEEK HAS COME TO CHASE YOU!!!")
        survive = int(input("The bookshelf fell press 19867 to continue"))
        if survive == 19867: 
            print("phew that was a close one..") 
        else: 
            print("you died")
            die = True
        survive2 = int(input("There is a bookshelf in the way press 4689856 to continue"))
        if survive2 == 4689856: 
            print("phew you survived")
        else: 
            print("ypu died")
            die = True
        survive3 = int(input("There is one last obstacle survive without burning! press 2010 to survive"))
        if survive3: 
            print("YAY YOU SURVIVED AGAINST SEEK")
        else: 
            print("you died..")
            die = True 
            return chase(running)


def room9(items): 
    locked_door = int(input("this room is locked press 76 to check the bed and 89 to check the closet to find the key"))
    if locked_door == 89:
        check = int(input("To check the bed now press 99"))
        if check == 99: 
            locked = int(input("Good job.. you found a lockpick press 3 to use it"))
            if locked == 3:
                print("Great job lets move on")
            if locked_door == 76: 
                locked = int(input("Good job.. you found a lockpick press 3 to use it"))
                if locked == 3: 
                    print("great job lets move on")
                    return room9(items)


def room10(items):
        empty = input("this room is empty :)")
        return room10(items)



def room11(items): 
    locked_door = int(input("this room is locked press 76 to check the bed and 89 to check the closet to find the key"))
    if locked_door == 89:
        check = int(input("To check the bed now press 99"))
        if check == 99: 
            locked = int(input("Good job.. you found a lockpick press 3 to use it"))
            if locked == 3:
                print("Great job lets move on")
            if locked_door == 76: 
                locked = int(input("Good job.. you found a lockpick press 3 to use it"))
                if locked == 3: 
                    print("great job lets move on")
                    return room11(items)




def hallway2(items):
    print("In this hallway you have found a 3 drawer wardrobe which drawer would yoy like to open?")
    drawer = int(input("pick a drawer 1-3"))
    if drawer == 2:
        print("you got a bandaid")
    if drawer == 2: 
        ("ROAR! the monster bit you")
        user_stats == print(45/50)
    if drawer == 3:
        print("aww you found nothing :|")
        return hallway(items)


def room12(items):
    print("The door is locked find the key")
    check = int(input("if you would like to check the room press 1 or 2 for thecloset"))
    if check == 1:
        print("You found the key on the ground")
        print("chk chk...oh no..")
        whoops = int(input("There are 2 doors with different numbers which would you like to pick one or two"))
        if whoops == 2:
            print("it unlocked! good choice")
        if whoops == 1:
            print("oh no timmothy attacked you")
            user_stats = print(35/50)
    if check == 2:
        print("oh no there is nothing")
        return room12(items)




starts = int(input("to play press 3: "))
if starts == 3:
    while die == False:
        entrance("key")
        hallway("drawer")
        hallway("check")
        hallway("whoops")
        room2("wander")
        room2("item")
        room3("monster")
        room3("rush")
        room5("locked_door")
        room5("check")
        room5("locked")
        room6("hallway_locked")
        room6("beds")
        room6("check")
        room6("check_again")
        room6("typewriter")
        room7("eyes")
        room8("direction")
        room8("lockpick")
        chase("run")
        chase("survive")
        chase("survive2")
        chase("survive3")
        room9("locked_door")
        room9("check")
        room9("locked")
        room10("empty")
        room11("locked_door")
        room11("check")
        room11("locked")
        hallway2("drawer")
        room12("check")
        room12("whoops")
        


       






        

#Make a function for the final obstacle 
#show : Wow, great job you have made it to door 50, you will have to collect 4 keys in order to escape...This room is like a garage and a monster will be in here... when the monster is near you must stop moving. The keys will be hidden in drawers or just on the ground.. good luck and dont get caught


    #Ask the user what way they would like to go every time 
    #make it so the monster appears once in a while and the user has to stop moving 
    #Make it so if the user moves the user dies 
    #after the user collects all keys the must quietly go unlock the door 
    #If they get caught they die 
    #make dead ends where the user can die 
    #once the user makes it out they will get the award 
    #if the user died ask them to play again 

    #once user wins give them a trophy of achievement 
    #ask them to play

