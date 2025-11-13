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
burger_order = input("what would you like you burger to be ")
if burger_order == "cheeseburger" or burger_order == "double bacon cheeseburger" or burger_order == "simple burger":
    True 
    order.append(burger_order)
else:
    False 
    print("can you please order somthing from the menu")

side_order =  input("what would you like your first side to be ")
if side_order == "salad" or side_order == "fries" or side_order == "onion rings" or side_order == "sweet potatoe":
    True 
    order.append(side_order)
    
else:
    False 
    print("can you please order somthing from the menu")

side_order2 =  input("what would you like your second side to be ")
if side_order2 == "salad" or side_order2 == "fries" or side_order2 == "onion rings" or side_order2 == "sweet potatoe":
    True 
    order.append(side_order2)
else:
    False 
    print("can you please order somthing from the menu")

drinks =  input("what would you like your drink to be ")
if drinks == "coke " or drinks == "sprite" or drinks == "root beer":
    True 
    order.append(drinks)
else:
    False 
    print("can you please order somthing from the menu")
print(order)

