#ES 1 pssword checker
#





#print saying the instruction for the password, and the steps required for it 
print("Hi, you are going to make a password, you need at least 8 characters long, contains at least one uppercase letter,  contains at least one lowercase letter, contains at least one number and contains at least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)")\
#make a list that says the reqired lenght sould be 8
required_lenght = 8
#make a while loop, while True:, press enter
while True:
#name a varible named user_password, equals input("What would you like your password to be?: ")
    user_password = input("What would you like your password to be?: ")
#make an if statement asking the program that if user_password has a lower case using the method islower. 
    if user_password.islower():
#print that you have a lower case if the input is true
        print("you have a lower case!")
#Then break so the code stops
        break
#If the top if not true, the else statment will fix it 
    else:
        print("You dont have a lower case , please enter a lower case letter")
#write continue so it goes back to the begging of the loop 
        continue

#make another while loop fo upper case this thime
while True:
    user_password = input("What would you like your password to be?: ")
# make an if stament asking the progam tht if the password has a upper case 
    if user_password > required_lenght:
#if true, it will print it has upper case
        print("You have met the require lenght!")
#break so code doessnt run for ever
        break
#make an else statment if password not true
    else:
        print("You havent met the lenght requirent")
        continue  

#do evething it agian for letter lenght
while True:
#name a varible named user_password, equals input("What would you like your password to be?: ")
    user_password = input("What would you like your password to be?: ")
#make an if statement asking the program that if user_password has a lower case using the method islower. 
    if user_password:
#print that you have a lower case if the input is true
        print("you have a lower case!")
#Then break so the code stops
        break
#If the top if not true, the else statment will fix it 
    else:
        print("You dont have a lower case , please enter a lower case letter")
#write continue so it goes back to the begging of the loop 
        continue

