import time
from snake import snake
from screen import screen

screen_entity = screen()
is_game_on = True
snake_entity = snake()
snake_entity.create_snake_tail(length_required=3)

while is_game_on:
    screen_entity.listen_screen()
    screen_entity.update_screen()
    snake_entity.move_snake_forward()
    screen_entity.screen_keypress(snake_entity, "d")
    time.sleep(0.1)
    
    


screen_entity.exit_screen()