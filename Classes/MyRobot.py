from Classes.BaseRobot import BaseRobot
from random import randint


class MyRobot(BaseRobot):

    def __init__(self, id, field, x_position=0, y_position=0):
        super(MyRobot, self).__init__(x_position=x_position, y_position=y_position, field=field, id=id)

    def game_playing(self):
        random_number = randint(1,4)
        if(random_number == 1):
            self.walk_right()
        elif(random_number == 2):
            self.walk_down()
        elif(random_number == 3):
            self.walk_left()
        elif(random_number == 4):
            self.walk_up()

    def game_stopped(self):
        print("I'm stopped")
