import math
import Classes.Field

class bcolors:
    """Colors used on terminal
    """    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Ball(object):
    """Class represeting a ball in a football game. Ideally, should be a Singleton.

    """    
    def __init__(self, field, x_position=25, y_position=7, x_speed=0.0, y_speed=0.0):
        """Constructor

        Args:
            field (Field): field that this ball play on.
            x_position (int, optional): Position on the x axis. Defaults to 25.
            y_position (int, optional): Position on the y axis. Defaults to 7.
            x_speed (float, optional): Speed on the x axis. Defaults to 0.0.
            y_speed (float, optional): Speed on the y axis. Defaults to 0.0.
        """
        self.x_position = x_position
        self.y_position = y_position
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.field = field
        self.field[y_position][x_position] = self

    def __repr__(self):
        """Overloads the default return on print funcion to print an O.

        Returns:
            str: Blue painted O string
        """        
        return bcolors.HEADER + "O" + bcolors.ENDC

    def get_positions(self):
        return (self.x_position, self.y_position)

    def get_speeds(self):
        return (self.x_speed, self.y_speed)

    def roll(self):
        """Function ran every tick of the game. Calculates movement based on the speed of the ball.
        """        
        #calculates positions to be based on speed
        next_x_position = int(math.floor(self.x_position + self.x_speed))
        next_y_position = int(math.floor(self.y_position + self.y_speed))

        #checks if the ball would be out of the field.
        if(next_x_position >= self.field.width):
            next_x_position = self.field.width - 1
        if(next_y_position >= self.field.height):
            next_y_position = self.field.height - 1
        if(next_x_position < 0):
            next_x_position = 0
        if(next_y_position < 0):
            next_y_position = 0

        #checks if the place that the ball would move is occuped by a grass tile
        if(isinstance(self.field[next_y_position][next_x_position], Classes.Field.Grass)):
            prev_grass = self.field[next_y_position][next_x_position]

            self.field[next_y_position][next_x_position] = self
            self.field[self.y_position][self.x_position] = prev_grass
            
            #updates positions
            self.x_position = next_x_position
            self.y_position = next_y_position

        #de-accelerate the balls
        self.x_speed = max(0, self.x_speed - 1) if self.x_speed > 0 else min(0, self.x_speed + 1)
        self.y_speed = max(0, self.y_speed - 1) if self.y_speed > 0 else min(0, self.y_speed + 1)
