# alex scott, early 2021
# in order to use images, go to sketch -> Add File... 
# https://py.processing.org/reference/image.html

x = 0
y = 0

x_vel = 1
y_vel = 1

r = 255
g = 255
b = 255

def new_color():
    global r, g, b
    r = random(100, 255)
    g = random(100, 255)
    b = random(100, 255)

def setup():
    global dvd
    size(300, 300)
    background(0)
    new_color()
    dvd = loadImage("dvd.png")

def draw():
    background(0)
    global dvd, x, y, x_vel, y_vel
    tint(r, g, b)
    image(dvd, x, y)
    
    x += x_vel
    y += y_vel
    
    if x + dvd.width >= width or x <= 0:
        new_color()
        x_vel *= -1
        
    if y + dvd.height >= height or y <= 0:
        new_color()
        y_vel *= -1
        
# Additional Reading
# https://github.com/CodingTrain/website/blob/main/CodingChallenges/CC_131_BouncingDVDLogo/P5/sketch.js
# https://editor.p5js.org/brunoruchiga/sketches/bmAOI_p9F
