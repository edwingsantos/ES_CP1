#ES starter 
import turtle 
def draw_branch(lenght):
    if lenght > 5:
        for i in range(3):
            turtle.forward(lenght / 3)
            turtle.right(60)
n = turtle.Turtle

n.color("red")
n.penup()
n.goto(0,0)
n.pendown()

for i in range(6):
    draw_branch(600)
    n.right(60)