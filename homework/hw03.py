import math


# Example functions for background reading

def nickels_to_cents(nickels):
    '''
    Purpose:
        Converts from a given number of nickels to
        the number of cents they represent
    Parameter(s):
        nickels: The number of nickels we have (int)
    Return Value:
        The amount in cents we have (int)
    '''
    total = nickels * 5
    return total

def degrees_to_radians(deg):
    '''
    Purpose:
        Converts from degrees to radians
    Parameter(s):
        deg: The number of degrees in a given angle (float/int)
    Return Value:
        The given angle's measure in radians (float)
    '''
    radians = deg * math.pi / 180
    return radians




# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose:
        Converts a Celsius temperature degree value to a Fahrenheit temperature degree value
    Parameter(s):
        celsius: The temperature degree value in celsius (float/int)
    Return Value:
        The given value's equivalent degree value in Fahrenheit (float)
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def print_25_stars():
    '''
    Purpose:
        Prints 25 stars, 5 sets of 5 each on a different line
    Parameter(s):
        None
    Return Value:
        None
    '''
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    

# Part B: Projectile Motion

def trajectory(speed, height, angle):
    '''
    Purpose: 
        Calculates the horizontal distance a projectile flies, its initial horizontal speed, initial vertical speed, and flight time based on its 
        initial speed, height, and angle of release, assuming Earth gravity and no other factors. It then prints the initial horizontal speed, initial 
        vertical speed, and flight time, before returning the horizontal flight distance.
    Parameter(s):
        speed: The initial speed of the projectile, without direction, in m/s (float/int)
        height: The initial vertical distance the projectile has from the reference frame, in m (float/int)
        angle: The initial angle in degrees the object is thrown at the point of release relative to the horizontal reference plane (float/int)
    Return Value:
        The horizontal distance a projectile flies in meters based on its initial speed, height, and angle of release, assuming Earth gravity and no
        other factors (float)
    '''
    angle_rads = degrees_to_radians(angle)
    initial_speed_h = speed * math.cos(angle_rads)
    initial_speed_v = speed * math.sin(angle_rads)
    flight_time = (initial_speed_v + math.sqrt((initial_speed_v ** 2) + (19.6 * height))) / 9.8
    flight_distance = flight_time * initial_speed_h
    print(f"Horizontal Speed: {initial_speed_h} m/s")
    print(f"Vertical Speed: {initial_speed_v} m/s")
    print(f"Flight Time: {flight_time} s")
    return flight_distance




# Part C: Who needs loops?
def print_7():
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
def print_4():
    print_7()
    print_7()
    print_7()
    print_7()
def print_85():
    print_4()
    print_4()
    print_4()
    print("Who needs loops?")