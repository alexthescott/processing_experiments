# alex scott, early 2021 

from random import randint

# position variables
x = 100
y = 100

# velocity variables
x_vel = 2.5
y_vel = 2

# ball size variables
diameter = 25.0
radius = diameter // 2

# because the circle will be white, I've avoided light color choices
# the color range inside of processing is from 0 - 255
r = randint(0, 200)
g = randint(0, 200)
b = randint(0, 200)

def setup():
    size(200, 200)
    noStroke()

def draw():
    # decide what random color the background should be 
    background(r, g, b)
    
    # global allows us to modify variables inside of draw() after their initilization 
    global x, y, x_vel, y_vel
    
    # move our current position by the velocity
    x = x + x_vel
    y = y + y_vel
    
    # chance velocity if we bounce along the edge of the screen
    if (x > width - radius) or (x < radius):
        x_vel = x_vel * -1
    if (y > height - radius) or (y < radius):
        y_vel = y_vel * -1
        
    # draw the circle
    circle(x, y, diameter)
