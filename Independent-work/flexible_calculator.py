#ES 1 flexible calculator
#print the greetings for the user, Welcome to the calculator. The avable operations would be: sum, avarage, max, min, product
print("Welcome to the calculator")
print("The avable operations would be: sum, avarage, max, min, product")
#make a dictionary named numbers that is empty
choice = input("What funtion do you want to do?: ")


numbers = []
#make a while true loop 
while True:
    #make a variable inside of the loop called user choice and make it that the input what numbers they want in it 
    user_choice  = input("what would you like the number to be?: ")
    #if the user choice is a digit
    if user_choice.isdigit():
        #add it to the numbers libary
        numbers.append(user_choice)
    #make an elif statement if they type done break and print your done
    elif user_choice == "done":
        print("You are done")
        break
    #make an else statement that if its something else you print not an option
    else:
        print("not an option")



def numbers(*args):
    if choice == sum:
        for number in args:
            number + number
            print(numbers)