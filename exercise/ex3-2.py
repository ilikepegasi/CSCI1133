import math
radius = float(input("Enter the radius: "))
height = float(input("Enter the cylinder height: "))
def cyl_volume(radius, height):
    base_area = radius*radius*math.pi
    return base_area * height

def hemi_volume(radius): 
    return (2/3)*radius*radius*radius*math.pi

silo_volume = cyl_volume(radius,height) + hemi_volume(radius)
print("Silo volume is:", silo_volume)
