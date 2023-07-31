from turtle import Turtle,Screen

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)
    
def move_counter_clockwise():
    my_turtle.left(10)

def move_clockwise():
    my_turtle.right(10)

def clear_screen():
   my_turtle.reset()
    
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.speed(10)

screen = Screen()
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_counter_clockwise,"a")
screen.onkey(move_clockwise,"d")
screen.onkey(clear_screen,"c")
screen.exitonclick()