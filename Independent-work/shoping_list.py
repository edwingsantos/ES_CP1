# ES 1 Shopping List Manager

shoping_list = []
action = input("What do you want to be in your shoping list?: ")
shoping_list.append(action)
while True:
    more = input("Would you wish to add or delete more stuff? (yes/no):  ")
    if more == "yes":
        action = input("What else do you want to be in your shoping list?:")
        shoping_list.append(action)
        more = input("Would you wish to add or delete more stuff?:  ")
        if more =="yes":
            rather = input("would you like to delete or add an item?: ")
            if rather == "add":
                action = print("What else do you want to be in your shoping list?:")
            else:
                action = input("What would you like to delete from your list")
                shoping_list.remove(action)
                
    else:
        print("You are done with you list!")
        print(shoping_list)
