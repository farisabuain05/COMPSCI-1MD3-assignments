'''COMPSCI 1MD3 Assignment 1: Drawing a fence and calculating perimeter with turtle graphics.

Use turtle graphics to create fenceposts based on user input.
Draw fencing between each fencepost, and calculate (continuosly update) the fence's perimeter
Display perimeter once full fence shape has been created.

Faris Abuain, McMaster, May 2024.'''


## Import turtle graphics module and built-in math module

import turtle
import math


## Set up the turtle graphics screen

turtle.setup(900, 450) 
screen = turtle.Screen()


## Set up turtle (his name is Drew!)

drew = turtle.Turtle()
drew.shape("turtle")

length = 10   # side length of hexagonal fence posts

perimeter = 0   # initialize perimeter variable


## User inputs the number of fenceposts they would like to draw:

num_posts = int(screen.numinput("How many fenceposts do you have? ", "Fenceposts: ")) 


## Draw first post:

x = screen.numinput("x","What is x pos: ")   # input x position of fencepost (centrepoint)
y = screen.numinput("y","What is y pos: ")   # input y position of fencepost (centrepoint)
drew.up()
drew.goto(x-length/2, y+length*math.sin(math.pi/3))   # goes to hexagon's top-left corner relative to the centrepoint, where shape will be drawn from
drew.down()
drew.fillcolor("blanchedalmond")   # sets colour for hexagonal fenceposts
drew.begin_fill()
for _ in range(6):   # draw hexagons
    drew.forward(length)
    drew.right(60)
drew.end_fill()

previous_fence = x, y   # save position of previous fence

start_fence = x, y   # save the first post's centre position as a separate variable so we can return to close fence


## Draw rest of posts:

for _ in range(num_posts-1):   # num_posts - 1 because we've already drawn one of the posts
    x = screen.numinput("x","What is x pos: ")
    y = screen.numinput("y","What is y pos: ")
    drew.color("black")   # reset pen colour
    drew.up()
    drew.goto(x-length/2, y+length*math.sin(math.pi/3))   # same as above (go to corner relative to centre)
    drew.down()
    drew.fillcolor("blanchedalmond") 
    drew.begin_fill()
    drew.pensize(0.5)
    for _ in range(6): 
        drew.forward(length)
        drew.right(60)
    drew.end_fill()
    drew.up()
    drew.goto(previous_fence)   # return turtle to previous_fence
    drew.down()
    drew.pensize(5)   # reset pensize and colour
    drew.color("red")
    drew.goto(x,y)   # draw a line from previous_fencepost to current fence_post
    x_distance = x - previous_fence[0]
    y_distance = y - previous_fence[1]
    perimeter += math.sqrt(x_distance**2 + y_distance**2)   # add the distance between fenceposts (length of fence segment) to 'perimeter'
    previous_fence = x, y  

drew.goto(start_fence)   # once all fenceposts are drawn, return to original fencepost to close the fence shape

x_distance = start_fence[0] - previous_fence[0]
y_distance = start_fence[1] - previous_fence[1]

perimeter += math.sqrt(x_distance**2 + y_distance**2)   # find length of segment of fence that closes shape and add it to the perimeter

perimeter = round(perimeter / 45, 2)   # divide perimeter (in pixels) by 45 (45 pixels per metre) to obtain perimeter in metres, then round to 2 decimal places

drew.color("black")   # reset pensize and colour
drew.pensize(0.5)


## Display the perimeter of the fence (in metres) at the bottom of the screen:

drew.up()
drew.goto(-100, -200) 
drew.write(f"The perimeter of the fence is {perimeter} metres", align="center", font=("courier",15,"bold"))

drew.hideturtle()

turtle.done()   # end program.
