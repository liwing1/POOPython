from Classes.Field import Field, Grass
import numpy as np
from Classes.MyRobot import MyRobot
from time import sleep
import threading

kbdInput = ''


def kbdListener():
    global kbdInput, finished
    while(True):
        kbdInput = raw_input()
        print(kbdInput)


grass_tile = Grass()
current_field = Field()
my_robot = MyRobot(id="1", field=current_field, x_position=10, y_position=7)

listener = threading.Thread(target=kbdListener)
listener.start()


game_counter = 0
while(True):
    if(game_counter <= 3):
        current_field.game_stopped()
        game_counter += 1
    else:
        if(kbdInput != ''):
            current_field.ball.x_speed += 3
            current_field.ball.y_speed += 1
            kbdInput = ''
        current_field.game_playing()
        print("")
    sleep(1)
