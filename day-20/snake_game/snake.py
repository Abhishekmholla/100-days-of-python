from turtle import Turtle, turtles


class snake:

    def __init__(self) -> None:
        self.snake_body = []

    def create_snake_tail(self, length_required=1):

        if len(turtles()) == 0:
            snake = Turtle("square")
            snake.color("black")
            snake.penup()
            self.snake_body.append(snake)

        for _ in range(1, length_required):
            snake.goto(-10 * len(turtles()), 0)
            snake = Turtle("square")
            snake.color("black")
            snake.penup()
            self.snake_body.append(snake)

    def move_snake_forward(self):
        for snake_num in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[snake_num].goto(
                self.snake_body[snake_num - 1].xcor(), self.snake_body[snake_num - 1].ycor())

        self.snake_body[0].forward(20)

    def change_direction(self, key):
        if key == "d":
            for snake_num in range(len(self.snake_body) - 1, 0, -1):
                self.snake_body[snake_num].goto(
                    self.snake_body[snake_num - 1].xcor()-90, self.snake_body[snake_num - 1].ycor())
        
    
    