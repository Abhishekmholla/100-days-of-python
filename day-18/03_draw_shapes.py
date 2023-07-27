import random
import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

for number_of_sides in range(3,11):
    angle = round(360 / number_of_sides) 
    my_turtle.color(random.choice(["red",'green','orange']))
    for _ in range(number_of_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)
    
screen = turtle.Screen()
screen.exitonclick()