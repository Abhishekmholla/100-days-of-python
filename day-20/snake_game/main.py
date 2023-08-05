import time
from turtle import Screen,Turtle,turtles

snake_body =[]
is_game_on = True

def create_screen():
    screen = Screen()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.exitonclick()
    return screen

def create_snake_tail(length_required = 1):
    if len(turtles()) == 0:
        snake = Turtle("square")
        snake.color("black")
        snake.penup()
        snake_body.append(snake)
    
    for _ in range(1,length_required):
        snake.goto(-10 * len(turtles()),0)
        snake = Turtle("square")
        snake.color("black")
        snake.penup()
        snake_body.append(snake)
        
    return snake

def move_snake_forward():
    for snake_num  in range(len(snake_body) - 1 ,0,-1):
        snake_body[snake_num].goto(snake_body[snake_num -1].xcor(), snake_body[snake_num -1].ycor())

    snake_body[0].forward(20)
        
# create_screen()

snake = create_snake_tail(length_required=3)
screen = Screen()

while is_game_on:
    screen.update()
    move_snake_forward()
    time.sleep(0.1)


screen.exitonclick()