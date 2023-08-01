import random   
from turtle import Turtle,Screen

start_cordinate = -300
end_cordinate = 330
is_race_on = False
turtles = []
turtle_colours = ["red",'green','orange','blue','brown','black']
screen = Screen()

screen.screensize(canvwidth=1000,canvheight=1000)
user_input = screen.textinput(title="Make your bet", prompt=f"Who will win the race? Colour options: {','.join(turtle_colours)}?  Enter a colour: ")

def create_turtle(turtle_colour):
    turtle = Turtle(shape="turtle")
    turtle.color(turtle_colour)
    return turtle

def move_turtle_to_a_position(turtle: Turtle,x_cordinate: int, y_cordinate:int):
    turtle.speed(10)
    turtle.penup()
    turtle.goto(x=x_cordinate,y=y_cordinate)


for turtle_id in range(6):
    start_cordinate += 90
    my_turtle = create_turtle(turtle_colours[turtle_id])
    move_turtle_to_a_position(my_turtle,x_cordinate=-300, y_cordinate = start_cordinate)
    turtles.append(my_turtle)

if user_input:
    is_race_on = True
    
while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() > end_cordinate:
            if turtle.color()[1] != user_input:
                print(f"You lose!! The winner is {turtle.color()[1]} turtle")
            else:
                print(f"You win!! The winner is {turtle.color()[1]} turtle")
            is_race_on = False
            break
screen.exitonclick()