import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from game_design import Gamedesign

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("TURTLE CROSSING PROJECT ( Ver. 1.0.0 )")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
gamedesign = Gamedesign()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.final_score()
            scoreboard.game_over()
    # If player crosses finish line
    if player.ycor() > 230:
        player.refresh_position()
        scoreboard.refresh_level()
        car_manager.increase_car_speed()

screen.mainloop()
