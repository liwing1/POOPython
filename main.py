from Classes.Field import Field, Grass
import numpy as np
from Classes.MyRobot import MyRobot, AiRobot
from time import sleep
import threading
import os

kbdInput = ''

def kbdListener():
    global kbdInput, finished
    while(True):
        kbdInput = str(input()).lower()
        os.system("clear")
        print(kbdInput)


def trataInput(input):
    switch = {'w':4, 'a':3, 's':2, 'd':1}
    if input in switch.keys():
        return switch[input]
    return 0
    



grass_tile = Grass()
current_field = Field()
#robot_list = [ MyRobot(id = str(i), field=current_field, x_position=10-i, y_position=7) for i in range(10) ]
my_robot = MyRobot(id="1", field=current_field, x_position=22, y_position=7)
ai_robot = [AiRobot(id=str(i), field=current_field, x_position=2+i, y_position=7) for i in range(2,9)]

listener = threading.Thread(target=kbdListener)
listener.start()


game_counter = 0
while(True):
    if(game_counter <= 3):
        current_field.game_stopped()
        game_counter += 1
    else:
        if(kbdInput != ''):
            #print("kbdInput = %s",kbdInput)
            #current_field.ball.x_speed += 3
            #current_field.ball.y_speed += 1

            
            current_field.game_playing(trataInput(kbdInput))
            kbdInput = ''
        os.system("clear")
        current_field.game_playing(0)
    sleep(1)
    
