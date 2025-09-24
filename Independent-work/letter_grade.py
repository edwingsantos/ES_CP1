#ES 1 letter grade 

grade = float(input(f"Please enter you class percentage grade: "))

if not grade:
    print("Please enter a valid grade ")
elif float(grade >=100.00 and 92.00 ):
    print("You have an A in this class! ")
elif float(grade >=90.00 and 91.99 ):
    print("You have an A- in this class")
elif float(grade >=87.00 and 89.99 ):
    print("You have a B+")
elif float(grade >=82.00 and 86.99 ):
    print("You have a B ")
elif float(grade >=80.00 and 81.99 ):
    print("You have a B- ")
elif float(grade >=77.00 and 79.99 ):
    print("You have a C+ ")
elif float(grade >=72.00 and 76.99 ):
    print("You have a C ")
elif float(grade >=70.00 and 71.99 ):
    print("You have a C- ")
elif float(grade >=67.00 and 69.99 ):
    print("You have a D+ ")
elif float(grade >=64.00 and 66.99 ):
    print("You have a D ")
elif float(grade >=55.00 and 63.99 ):
    print("You have a D- ")
else:
    print("You have an F")