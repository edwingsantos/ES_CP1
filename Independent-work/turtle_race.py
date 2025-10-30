#Es 1 turlte race
#import turtle as t for shorter 
import turtle as t
#import random
import random

speed = random.randint(1,10)
#name your turtles as number
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
#make you turtles different colors and shaped as turtles
t1.color("red")
t1.shape("turtle")
t2.color("purple")
t2.shape("turtle")
t3.color("yellow")
t3.shape("turtle")
t4.color("blue")
t4.shape("turtle")
t5.color("orange")
t5.shape("turtle")

t1.hideturtle()
t1.penup()
t1.goto(-400,50)
t1.pendown()
t1.showturtle()



t2.hideturtle()
t2.penup()
t2.goto(-400,70)
t2.pendown()
t2.showturtle()


t3.hideturtle()
t3.penup()
t3.goto(-400,90)
t3.pendown()
t3.showturtle()


t4.hideturtle()
t4.penup()
t4.goto(-400,110)
t4.pendown()
t4.showturtle()

t5.hideturtle()
t5.penup()
t5.goto(-400,130)
t5.pendown()
t5.showturtle()

end = t.Turtle()

end.hideturtle()
end.penup()
end.goto(500,600)
end.pendown()
end.sety(-600)
end.showturtle()

speed = random.randint(100,200)

for num in range(speed):
    t1.forward(random.randint(50,100))
    t2.forward(random.randint(50,100))
    t3.forward(random.randint(50,100))
    t4.forward(random.randint(50,100))
    t5.forward(random.randint(50,100))
    x1 = t1.xcor()

if t1 == end:
    print("red won")
elif t2 == end:
    print("purple")
elif t3 == end:
    print("yellow")
elif t4 == end:
    print("blue")
elif t5 == end:
    print("orange")


t.done()