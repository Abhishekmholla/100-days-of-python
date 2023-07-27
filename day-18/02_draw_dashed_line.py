import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

for _ in range(10):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
    
screen = turtle.Screen()
screen.exitonclick()