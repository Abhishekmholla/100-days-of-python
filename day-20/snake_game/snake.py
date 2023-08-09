from turtle import Turtle, turtles


class snake:

    def move_snake_forward(self):
        for snake_num in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[snake_num].goto(
                self.snake_body[snake_num - 1].xcor(), self.snake_body[snake_num - 1].ycor())

        self.snake_body[0].forward(20)
