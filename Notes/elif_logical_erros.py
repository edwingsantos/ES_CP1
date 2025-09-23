#ES 1 Elif and Logical Operators Notes

grade= 100

if grade > 100:
    print(f"You got extra credit, you got {grade-100} extra credit points")
elif grade == 100:
    print("Your grade if perfect!")
else:
    print("Try harder")

username = "fer"
password = "1234"
user = input("Enter your user name: ")
pword = input("Enter you password: ")


if not user or not pword:
    print("please enter a valid input")
elif user == username and pword == password:
    print("Welcom fer")
elif user == username:
    print("password incorrect")
else:
    print("incorrect credentials")