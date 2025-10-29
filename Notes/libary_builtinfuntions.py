#ES 1 libary built in functions 
import turtle as t
import random
colors = ["orange","green","blue","purple","red"]
side = random.randint(10,500)

t.color(random.choice(colors))
t.shape("turtle")
t.shapesize(12)
t.fillcolor(random.choice(colors))

t.begin_fill()
for x in range(1,4):
    t.speed(100)
    t.forward(side)
    t.right(90)

t.end_fill()

t.penup()
t.goto(50,50)
t.pendown()

t.fillcolor("orange")
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()




t.done()