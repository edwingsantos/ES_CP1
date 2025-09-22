# ES 1 user sing in
user_name1 = "Zane"
user_name2 = "Isabela"


#check if user has a account
user_name = input("What is your user name? (first name)")
if user_name == user_name1:
    zane_password = input("Hi Zane, can you put your password? (age)")
    if zane_password == 14:
        zane_info = input(" would you like to log in?  (yes/no)")
    if zane_info.lower() == "yes":
        print("You chose to preced, your user name is Zane, and your password is 14")
    else:
        print("You didnt chose to preced")
elif user_name == user_name2:
    isabela_info = input("Hi Isabela, would you like to log in  (yes/no)")
    if isabela_info.lower() == "yes":
          print("You chose to preced, your user name is Isabela, and your password is 14")
    else:
        print("You didnt chose to preced")



password = int(input("what is your password? (age)"))


    
