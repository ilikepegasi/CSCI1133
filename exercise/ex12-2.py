import math

class Cylinder:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
    def get_surface_area(self):
        return math.pi*self.diameter**2 + math.pi*self.diameter*self.height
    def get_volume(self):
        return self.height*math.pi*(0.5*math*self.diameter)**2