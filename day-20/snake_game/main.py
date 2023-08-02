from turtle import Screen,Turtle,turtles

def create_screen():
    screen = Screen()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.exitonclick()
    return screen

def create_snake_tail(snake , length_required = 1):
    for _ in range(length_required):
        snake.goto(-20 * len(turtles()),0)
        snake = Turtle("square")
        snake.color("black")
        

# create_screen()
tup = Turtle("square")
create_snake_tail(tup,2)
screen = Screen()
screen.exitonclick()