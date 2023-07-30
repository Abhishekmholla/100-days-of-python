import random
import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
turtle.colormode(255)
my_turtle.speed(0)


for _ in range(200):
    my_turtle.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    my_turtle.circle(100)
    my_turtle.setheading(my_turtle.heading() + 5)

    

screen = turtle.Screen()
screen.exitonclick()