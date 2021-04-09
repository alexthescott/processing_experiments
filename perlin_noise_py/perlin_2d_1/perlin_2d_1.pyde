inc = 0.1
scl = 25

particles = []

def setup():
    size(400, 400)
    background(0)
    global rows, cols, start, flowField
    cols = width // scl
    rows = height // scl
    start = 10
    flowField = []
    noStroke()
    
    for i in range(100):
        particles.append(Particle())

    yoff = start
    for x in range(rows):
        xoff = start
        for y in range(cols):
            angle = noise(xoff, yoff) * TWO_PI
            v = PVector.fromAngle(angle)
            flowField.append(v)
            xoff += inc
        yoff += inc

    
def draw():
    global flowField, start
    yoff = start
    fill(255, 20)
    rect(0, 0, width, height)
    for x in range(rows):
        xoff = start
        for y in range(cols):
            angle = noise(xoff, yoff) * TWO_PI
            v = PVector.fromAngle(angle)
            index = x + y * cols
            flowField[index] = v
            strokeWeight(2)
            stroke(0, 50)
            push()
            translate(x * scl, y * scl)
            rotate(v.heading())
            # line(0, 0, scl, 0)
            pop()
            xoff += inc
        yoff += inc
    start += inc / 10
    
    strokeWeight(2)
    for i in range(len(particles)):
        particles[i].show()
        particles[i].follow(flowField)
    
class Particle:
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.vel = PVector.random2D()
        self.acc = PVector(0, 0)
        self.maxspeed = 1
    
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)
        self.vel.limit(self.maxspeed)
        
    def follow(self, vectors):
        x = self.pos.x // scl
        y = self.pos.y // scl
        index = floor(x + y * cols)
        index = min(index, 255)
        force = vectors[index]
        self.applyForce(force)
    
    def applyForce(self, force):
        self.acc.add(force)
        
    def show(self):
        stroke(0)
        point(self.pos.x, self.pos.y)
        self.edges()
        self.update()
        
    def edges(self):
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = width
        if self.pos.y > height:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = height
        
        
        
        
        
        
        
        
        
        
        
