import math

class Spirale():

    def first(self, cycle):
        return 4*cycle*cycle+1-4*cycle

    def cycle(self, index):
        return (self.isqrt(index) + 1)//2
    
    def length(self, cycle):
        return 8 * cycle

    def isqrt(self, x):
        """Calculates the integer square root of a number"""
        if x < 0:
            raise ValueError('square root not defined for negative numbers')
        n = int(x)
        if n == 0:
            return 0
        a, b = divmod(n.bit_length(), 2)
        x = 2**(a+b)
        while True:
            y = (x + n//x)//2
            if y >= x:
                return x
            x = y

    def get_position(self, index):
        c = self.cycle(index)
        offset=index-self.first(c)

        dx=c-1
        dy=-c+1

        offset=index-self.first(c)
        if(offset>0):
            if(offset>c*6):
                dx+=1
                dy+=c*2-1
                dx=dx-c*2            
                dy=dy-c*2
                
                dx=dx+offset-c*6
            elif(offset>c*4):
                dx+=1
                dy+=c*2-1

                dx=dx-c*2

                dy=dy-offset+c*4
            elif(offset>c*2):
                dx+=1
                dy+=c*2-1
                dx=dx-offset+c*2
            else:
                dx+=1
                dy=dy+offset-1


        return dx, dy

    def get_distance(self, value):
        position=self.get_position(value)
        return math.fabs(position[0])+math.fabs(position[1])