#ES 1 pssword checker
#





#print saying the instruction for the password, and the steps required for it 
print("Hi, you are going to make a password, you need at least 8 characters long, contains at least one uppercase letter,  contains at least one lowercase letter, contains at least one number and contains at least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)")\
#make a list that says the reqired lenght sould be 8


#make a list fo the special chraracters 
special_characters = "!""@""#""$""%""^""&""*""()""_""+""-""=""[]""{}""|"";"":"","".""<"">""?"


#score is going to keep track of my score
score = 0
#make the password an input so the user can type
password = input("What would you like your password to be: ")
#Put N as password so i can make a loop later
N = password 
#Use lenght to check if it meet the lenght requiremment
lenght = len(password)
#make an if statement to check if the lenght is enough for 8 chracters
if lenght >= 8:
#print that you have met the lenght requirement if the if stement is true
    print("You have the lenght requirement")
#add one point to you score
    score+=1 
#make an if statemtnt if is not true
else:
    print("You didn't meet the lenght requirement")


#make a for loop using N in password
for N in password:
#check if N is lower case by saying is not true 
    if N.islower() != True:
#print that you have a lower case if the input is true
        print("you have a lower case!")
#add a point to your score
        score+=1
#Then break so the code stops
        break
#make an else statement if is not true
    else:
        print("You dont have a lower case")
for N in password:
#make another if statemnt for upper case now 
    if password.isupper():
        print("you have a upper case")
#add a point to your score
        score+=1
#Then break so the code stops
        break
#make an else statement if is not true    
    else:
        print("You dont have a upper case")

for N in password:
#Now make one but for special characters
#check if password is on my list
    if password in special_characters:
        print("You have one of the special chracters")
        #add one point 
        score+=1
        #break so code doesnt go for ever
        break
#make an else statement if is not true
    else:
        print("You dont have a special chracter")
for N in password:
#now make one for the number
#check if there is a number in my password
    if password.isdigit():
        print("You have a number")
        #add a point
        score+=1
        #break so code doesnt go for ever
        break
    #make an else statement if is not true
    else:
        print("You dont have a number")