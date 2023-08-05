from turtle import Screen

class screen:
    
    def __init__(self) -> None:
        self.screen = Screen()
    
    def create_screen(self):
        self.screen.setup(width=600,height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
    
 