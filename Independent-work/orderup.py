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
    print(f"{key} is {drinks[key]}")
print("")
print("SIDES")
for key in sides.keys():
    print(f"{key} is {sides[key]}")
print("")