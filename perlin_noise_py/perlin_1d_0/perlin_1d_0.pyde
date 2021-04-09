# alex scott, early 2021
# graphing 1D Perlin noise

start = 0
inc = 0.01

def setup():
    size(400, 400)
    stroke(255)
    noFill()
    noiseDetail(3)
    background(55)

def draw():
    global start, inc
    background(55)
    beginShape()
    xoff = start
    for i in range(width):
        n = map(noise(xoff), 0, 1, 0, height)
        r = random(0, 1)*height
        vertex(i, n)
        xoff += inc
    endShape()
    start += inc
    
# additional reading!
# https://py.processing.org/reference/noiseDetail.html
# https://thecodingtrain.com/learning/noise/0.4-graphing-1d.html
# https://blog.hirnschall.net/perlin-noise/
