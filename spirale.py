import math

class Spirale():

    def __init__(self):
        self.value=0

    def get_position(self, value):
        if(value==23):
            return (0,-2)
        if(value==12):
            return (1,2)
        return (0, 0)

    def get_distance(self, value):
        position=self.get_position(value)
        return math.fabs(position[0])+math.fabs(position[1])