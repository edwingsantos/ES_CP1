#ES 1 flexible calculator
#print the greetings for the user, Welcome to the calculator. The avable operations would be: sum, avarage, max, min, product
print("Welcome to the calculator")
print("The avable operations would be: sum, avarage, max, min, product")
numbers = []
while True:
    user_choice  = input("what would you like the number to be?: ")
    if user_choice.isdigit():
        numbers.append(user_choice)
    elif user_choice == "done":
        print("You are done")
        break
    else:
        print("not an option")

