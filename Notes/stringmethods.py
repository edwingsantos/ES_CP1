# ES 1 string methos notes

subject = "computer programming 1!"

print(subject.upper())
print(subject.center(20))

name = print("what is your full name?").strip().title()


color = input("what is your favorite color?").strip().lower()
print("That is cool. I like " + color + " too!")
print("That is cool. I like " + {color} + " too!".format(name=name,color=color))

pi = "3.14159"
print(f"we all know pi is equl to {pi:.3f}")
