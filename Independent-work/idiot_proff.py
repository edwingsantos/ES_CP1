#ES 1 idiot proof

name = input("Hello what is your name?: ").strip().title( )

phone_number = (input("Hello " + name + ", what is your phone number?: ")).strip() 
phone_number = " ".join([phone_number[:-4][i:i+3] for i in range(4, len(phone_number) - 4, 3)]) + " " + phone_number[-4:]
gpa = float(input("What is your GPA?: "))

print(gpa + name + phone_number)