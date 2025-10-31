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
#make you turtles different colors and shaped as turtles, naming them accordint to the number of the rutle 
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
#were are going to place our turtles at the beggining of the line, by hidding the turtle 
t1.hideturtle()
#we bring up the turtle
t1.penup()
#make i go to the starting cordnates
t1.goto(-400,50)
#bring down the turlte 
t1.pendown()
#and show the turtle 
t1.showturtle()


# reapeat the past steps, and do the same for all the turtles 
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
# we are going to make the speed a number from one hundreed two hundred
speed = random.randint(100,200)
# now wea re making a for loop that num is in range(speed)
for num in range(speed):
#make the turtle go forward a random number
    t1.forward(random.randint(50,100))
# if the turtle crosses the x azis of 500 then print that that turtle won and break so is stops
    if t1.xcor() >= 500:
        print("red won")
        break
#repeat for every turtle 
    t2.forward(random.randint(50,100))
    if t2.xcor() >= 500:
        print("purple")
        break
    t3.forward(random.randint(50,100))
    if t3.xcor() >= 500:
        print("yellow")
        break
    t4.forward(random.randint(50,100))
    if t4.xcor() >= 500:
        print("blue")
        break
    t5.forward(random.randint(50,100))
    if t5.xcor >= 500:
        print("orange")
        break 

#turlte is done 
t.done()