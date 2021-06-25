from __future__ import print_function
import numpy as np
import math
from .Ball import Ball

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

class Grass(object):
    """Class that models a grass tile.
    """    

    def __init__(self):
        self.has_ball = False

    def __repr__(self):
        """Overloads the default return on print funcion to print an g.

        Returns:
            [str]: [Green painted g string]
        """           
        return bcolors.OKGREEN + "g" + bcolors.ENDC

class Field(object):

    """ Class modeling a field object, ideally should be a singleton but this is not implemented.
    """    

    def __init__(self, height=10, width=50, robots=[]):
        """Constructor

        Args:
            height (int, optional): Field height. Defaults to 10.
            width (int, optional): Field width. Defaults to 50.
            robots (list, optional): List of Robot. Not in used currently. Defaults to [].
        """        
        self.height = height
        self.width = width
        self.robots = robots
        self._internal_array = [[Grass() for i in range(width)]
                                for j in range(height)]
        self.ball = Ball(self)

    def __getitem__(self, index):
        """Overloads bracket operator.

        Args:
            index (tuple): operator access in the style of [y][x].

        Returns:
            List: Field array
        """        
        return self._internal_array[index]

    def robot_in_robots(self, robot):
        """Funciton to test if a robot is in a field robots array.

        Args:
            robot (Robot): robot to test against.

        Returns:
            Boolean: True is tested robot is in robots array.
        """        
        for list_robot in self.robots:
            if(robot.id == list_robot.id):
                return True
        return False

    def add_robot(self, robot):
        """Add robot to field array.

        Args:
            robot (Robot): Robot to be added.
        """        
        if(not self.robot_in_robots(robot)):
            self.robots.append(robot)
            self._internal_array[robot.y_position][robot.x_position] = robot

    def print_field(self):
        """Function to print the field on the screen.
        """        
        for row in self._internal_array:
            for column in row:
                print(column, end=" ")
            print("")

    def game_playing(self, i):
        """Main function called on main, every tick.
        """
        for robot in self.robots:
            robot.game_playing(i)        
        self.ball.roll()
        self.print_field()
    
    def game_stopped(self):
        for robot in self.robots:
            robot.game_stopped()
