import numpy as np
import random

class Simulation:


    def __init__(self):
        self.car_position = []
        self.cars = []


    def place_cars(self):


        # Take the fucking car object and put it on the damn road dumb ass
        # Car position + 33 for every car placed to space evenly










class Road:

    def __init__(self, length):
        self.length = length
        length = 1000



class Cars:

    def __init__(self):
        self.car_length = 5
        self.speed = 0
        self.max_speed = 33.33
        #need to track position here self.position = position maybe?

    def car(self):
        # can I make self.position check for a car before moving it?
        # if self.position - self.speed = another car or something like that

        while self.speed < 34:
            self.speed += 2
            while self.speed > 2:
               if random.randint(1, 100) <= 10:
                    self.speed -= 2
            else:
                return self.speed

        return self.speed

if __name__ == '__main__':
    pass
