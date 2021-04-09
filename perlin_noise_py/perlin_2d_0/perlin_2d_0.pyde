# alex scott, early 2020

inc = 0.1
scl = 10
start = 10

def setup():
    size(400, 400)
    global rows, cols
    cols = width // scl
    rows = height // scl
    noStroke()
    
def draw():
    global start
    yoff = start
    for x in range(rows):
        xoff = start
        for y in range(cols):
            r = noise(xoff, yoff) * 255
            fill(r)
            rect(x*scl, y*scl, scl, scl)
            xoff += inc
        yoff += inc
    start += inc / 60
