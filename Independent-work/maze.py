#Es 1 maze
#  import random 
import random 
#import turtle as t for shorter 
import turtle as t 
#make a varable called m for outline of the maze, with t.turtle
m = t.Turtle()
wn = t.Screen()
wn.setup(1300,1300)
m.speed(10)
#make the outline of the maze
m.left(90)
m.forward(600)
m.right(90)
#make the exit 50 units shorter
m.forward(550)
m.penup()
m.forward(50)
m.right(90)
m.pendown()
m.forward(600)
m.right(90)
#make the beggining 50 shorter than the others
m.forward(550)
m.penup()
m.forward(50)
m.pendown()

#make a list for the rows of the grids, make six random randints to the side and six down, this is to determine if theres a wall or open space
grid_rows = [[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             ]
#make the same but for columbs now
grid_columbs = [[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
             ]
#make the turtle to go to the cornates you want by turning 
m.right(90)
    #and forward 100
m.forward(500)
m.right(90)
#make a variable for x, and if its 6 then it would break 
x=0

#make a loop so we dont have to make random randint many times 
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_rows[0][x] == 1:
        m.pendown()
        m.forward(100)
    #make this again but for columbs
    if grid_rows[0][x] == 0:
        m.penup()
        m.forward(100)

    x += 1

m.right(90)
m.forward(100)
m.right(90)
x=0
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_rows[1][x] == 1:
        m.pendown()
        m.forward(100)
    #make this again but for columbs
    if grid_rows[1][x] == 0:
        m.penup()
        m.forward(100)
    x += 1
    
m.left(90)
m.forward(100)
m.left(90)
x=0
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_rows[2][x] == 1:
        m.pendown()
        m.forward(100)
    #make this again but for columbs
    if grid_rows[2][x] == 0:
        m.penup()
        m.forward(100)
    x += 1

m.right(90)
m.forward(100)
m.right(90)
x=0
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_rows[3][x] == 1:
        m.pendown()
        m.forward(100)
    #make this again but for columbs
    if grid_rows[3][x] == 0:
        m.penup()
        m.forward(100)
    x += 1

m.left(90)
m.forward(100)
m.left(90)
x=0
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_rows[4][x] == 1:
        m.pendown()
        m.forward(100)
    #make this again but for columbs
    if grid_rows[4][x] == 0:
        m.penup()
        m.forward(100)
    x += 1

m.right(90)
m.forward(100)
m.right(90)
m.forward(100)
m.right(90)
x=0
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_columbs[0][x] == 1:
        m.pendown()
        m.forward(100)
#make this again but for columbs
    if grid_columbs[0][x] == 0:
        m.penup()
        m.forward(100)
    x += 1
m.left(90)
m.forward(100)
m.left(90)
x=0
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_columbs[1][x] == 1:
        m.pendown()
        m.forward(100)
    #make this again but for columbs
    if grid_columbs[1][x] == 0:
        m.penup()
        m.forward(100)
    x += 1
m.right(90)
m.forward(100)
m.right(90)
x=0
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_columbs[2][x] == 1:
        m.pendown()
        m.forward(100)
    #make this again but for columbs
    if grid_columbs[2][x] == 0:
        m.penup()
        m.forward(100)
    x += 1
m.left(90)
m.forward(100)
m.left(90)
x=0
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_columbs[3][x] == 1:
        m.pendown()
        m.forward(100)
    #make this again but for columbs
    if grid_columbs[3][x] == 0:
        m.penup()
        m.forward(100)
    x += 1
m.right(90)
m.forward(100)
m.right(90)
x=0
while True:
    if x == 6:
        break
    #if the random number is 1 is pendown and forward 100
    if grid_columbs[4][x] == 1:
        m.pendown()
        m.forward(100)
    #make this again but for columbs
    if grid_columbs[4][x] == 0:
        m.penup()
        m.forward(100)
    x += 1
m.hideturtle()

t.done()

s = t.Turtle()
