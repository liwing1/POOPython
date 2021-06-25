from Classes.BaseRobot import BaseRobot, bcolors
from random import randint


class MyRobot(BaseRobot):

    def __init__(self, id, field, x_position=0, y_position=0):
        super(MyRobot, self).__init__(x_position=x_position, y_position=y_position, field=field, id=id)

    def game_playing(self, side):
        #side = randint(1,4)
        if(side == 1):
            self.walk_right()
        elif(side == 2):
            self.walk_down()
        elif(side == 3):
            self.walk_left()
        elif(side == 4):
            self.walk_up()

    def game_stopped(self):
        print("I'm stopped")

    def kick_ball(self, side):
        if(side == 1):
            self.field.ball.x_speed += 3
        elif(side == 2):
            self.field.ball.y_speed += 3
        elif(side == 3):
            self.field.ball.x_speed -= 3
        elif(side == 4):
            self.field.ball.y_speed -= 3

class AiRobot(BaseRobot):

    def __init__(self, id, field, x_position=0, y_position=0):
        super(AiRobot, self).__init__(x_position=x_position, y_position=y_position, field=field, id=id)

    def game_playing(self,_):
        side = randint(1,4)
        if(side == 1):
            self.walk_right()
        elif(side == 2):
            self.walk_down()
        elif(side == 3):
            self.walk_left()
        elif(side == 4):
            self.walk_up()

    def game_stopped(self):
        print("I'm stopped")

    def kick_ball(self, side):
        if(side == 1):
            self.field.ball.x_speed += 3
        elif(side == 2):
            self.field.ball.y_speed += 3
        elif(side == 3):
            self.field.ball.x_speed -= 3
        elif(side == 4):
            self.field.ball.y_speed -= 3

    def __repr__(self):
        return bcolors.FAIL + "R" + bcolors.ENDC