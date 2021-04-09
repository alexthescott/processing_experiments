# alex scott, early 2021
# using 1D Perlin noise to move a circle in 2D 

xoff = 0.0
xincrement = 0.005

def setup():
    size(400, 400)
    background(0)
    noStroke()
    
def draw():
    # Create an alpha background
    fill(0, 10)
    rect(0, 0, width, height)

    # Get a noise value based on xoff and scale it according to the window's width
    global xoff
    x = noise(xoff) * width
    y = noise(xoff+10) * height # y value uses another point on the same 1D perlin graph

    # With each cycle, increment xoff
    xoff += xincrement

    # Draw the ellipse at the value produced by perlin noise
    fill(255)
    ellipse(x, y, 16, 16)
    
# additional reading!
# https://py.processing.org/reference/noise.html
# https://thecodingtrain.com/learning/noise/0.3-noise-vs-random.html
# https://blog.hirnschall.net/perlin-noise/
