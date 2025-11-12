#ES 1 orderup 
#Make list for burgers and make burgers with their prices 
burgers = {
    "cheeseburger": 12.99,
    "double bacon cheeseburger": .99,
    "simple burger": 34.99
}
#make a list for the drinks now with their prices 
drinks = {
    "coke":1.99,
    "sprite":1.99,
    "root beer":1.99,
}
#Make another list for the sides with their prices
sides = {
    "salad":4.99,
    "fries":3.99,
    "onion rings":3.99,
    "sweet potatoe":3.99
}

#print the greetings to the restaraunt
print("Hello welcome to drinks burgers and sides, the menu is the following.")
print("")
#print burgers in upper case so we know the category
print("BURGERS")
#loop keys in burger.key
for key in burgers.keys():
    #and print key and then burger[key]
    print(f"{key} is {burgers[key]}")
    #print("") so there is a space for the next category 
print("")
#print drinks in upper case so we know is a category
print("DRINKS")
#loop keys in drinks
for key in drinks.keys():
    #repeat last steps but for drinks and sides 
    print(f"{key} is {drinks[key]}")
print("")
print("SIDES")
for key in sides.keys():
    print(f"{key} is {sides[key]}")
print("")
#make a list as your order so it safes 
order = []
#ask the user what burger they want 
user_int = input("what would you like you burger to be ")
#make a loop for keys in burgers.keys()
for key in burgers.keys():
    #make an if statement that if key is equal to simple burger
    if key == "simple burger":
        #append the type of burger they chose 
        order.append('simple burger')
        #and also append the price
        order.append(burgers["simple burger"])

    elif key == "cheeseburger":
        #append the type of burger they chose 
        order.append('cheeseburger')
        #and also append the price
        order.append(burgers["cheeseburger"])


    elif key == "double bacon cheeseburger":
        #append the type of burger they chose 
        order.append('double bacon cheeseburger')
        #and also append the price
        order.append(burgers["double bacon cheeseburger"])

    else:
        print("choose an actual thing from the menu")


print(order)