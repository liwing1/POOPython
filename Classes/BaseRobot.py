from abc import ABCMeta, abstractmethod
from Classes.Field import Grass


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class BaseRobot(object):
    __metaclass__ = ABCMeta

    def __init__(self, id, x_position=0, y_position=0, field=None):
        self.x_position = x_position
        self.y_position = y_position
        self.field = field
        self.id = id
        self.field.add_robot(self)

    def __repr__(self):
        return bcolors.FAIL + "R" + bcolors.ENDC

    def walk_right(self):
        next_x = self.x_position + 1
        if(self.x_position < self.field.width - 1):
            # not on the edge of the field
            if(isinstance(self.field[self.y_position][next_x], Grass)):
                self.field[self.y_position][self.x_position] = self.field[self.y_position][next_x]
                self.field[self.y_position][next_x] = self
                self.x_position += 1


    def walk_left(self):
        next_x = self.x_position - 1
        if(self.x_position > 0):
            # not on the edge of the field
            if(isinstance(self.field[self.y_position][next_x], Grass)):
                self.field[self.y_position][self.x_position] = self.field[self.y_position][next_x]
                self.field[self.y_position][next_x] = self
                self.x_position -= 1


    def walk_up(self):
        next_y = self.y_position - 1
        if(self.y_position > 0):
            # not on the edge of the field
            if(isinstance(self.field[next_y][self.x_position], Grass)):
                self.field[self.y_position][self.x_position] = self.field[next_y][self.x_position]
                self.field[next_y][self.x_position] = self
                self.y_position -= 1


    def walk_down(self):
        next_y = self.y_position + 1
        if(self.y_position < self.field.height - 1):
            # not on the edge of the field
            if(isinstance(self.field[next_y][self.x_position], Grass)):
                self.field[self.y_position][self.x_position] = self.field[next_y][self.x_position]
                self.field[next_y][self.x_position] = self
                self.y_position += 1


    @abstractmethod
    def game_stopped(self):
        """Function for when the game is starting.
        """

    @abstractmethod
    def game_playing(self):
        """ Function for when the game is playing.
        """
    
    # @abstractmethod
    # def kick_ball(self, side):
    #     """Function called when the robot wants to kick the ball.

    #     Args:
    #         side (int): int representing the side the robot wants to kick. 0 = right, 1 = down, 2 = left, 3 = up.
    #     """        
