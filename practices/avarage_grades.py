#ES 1rst avarage grades
class1 = input("what is your grade for your first period?: ")

class2 = input("what is your grade for your second period?: ")

class3 = input("what is your grade for your third period?: ")

class4 = input("what is your grade for your fourth period?: ")

class5 = input("what is your grade for your fith period?: ")

class6 = input("what is your grade for your sixth period?: ")

class7 = input("what is your grade for your seventh period?: ")


grade_total = class1+class2+class3+class4+class5+class6+class7

final_grade = int(grade_total)/7
print("your final grade is", round(final_grade, 2))
