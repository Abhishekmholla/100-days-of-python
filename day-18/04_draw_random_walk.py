import random
import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
direction = [0,90,180,270]
my_turtle.speed(10)
my_turtle.pensize(15)
turtle.colormode(255)

for _ in range(200):
    my_turtle.forward(50)
    my_turtle.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    my_turtle.setheading(random.choice(direction))
   

screen = turtle.Screen()
screen.exitonclick()