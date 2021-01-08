from turtle import Screen, Turtle
from random import randint, choice

#Set up the track
track = Turtle(visible=False)
track.speed('fastest')
track.penup()
track.goto(-100, 200)

for step in range(15):
    track.write(step, align='center')
    track.right(90)
    track.forward(10)
    track.pendown()
    track.forward(160)
    track.penup()
    track.backward(170)
    track.left(90)
    track.forward(20)

track.goto(200, 250)
track.write("Finish Line", align='center')
track.pendown()
track.right(90)
track.forward(300)

#Make vince
vince = Turtle('turtle')
vince.speed('fastest')
vince.color('red')
vince.penup()
vince.goto(-120, 160)
vince.pendown()

#make lawrence
lawrence = Turtle('turtle')
lawrence.speed('fastest')
lawrence.color('blue')
lawrence.penup()
lawrence.goto(-120, 130)
lawrence.pendown()

#Make Trina
trina = Turtle('turtle')
trina.speed('fastest')
trina.color('green')
trina.penup()
trina.goto(-120, 100)
trina.pendown()

#Make the screen
screen = Screen()

#main game loop
while True:
    turtle = choice([vince, lawrence, trina])
    turtle.forward(randint(1, 5))
    if turtle.xcor() > 200:
        break

turtle.color('gold')

screen.exitonclick()
