from turtle import Screen
from snake import snake

class screen:
    
    def __init__(self) -> None:
        self.screen = Screen()
    
    def create_screen(self):
        self.screen.setup(width=600,height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
    
    def update_screen(self):
        self.screen.update()
    
    def exit_screen(self):
        self.screen.exitonclick()
        
    def listen_screen(self):
        self.screen.listen()
    
   