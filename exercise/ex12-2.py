import math

class Cylinder:
    def __init__(self, diameter, height):
        self.r = diameter/2
        self.h = height
    def get_surface_area(self):
        return 2*math.pi*self.r**2 + 2*math.pi*self.r*self.h
    def get_volume(self):
        return self.h * math.pi * self.r*  self.r
    
