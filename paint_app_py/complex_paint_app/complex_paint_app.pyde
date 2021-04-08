# Click to draw, and press "c" to clear the screen

prior_x = 0
prior_y = 0

# setup() -> https://py.processing.org/reference/setup.html
def setup():
    size(400, 400)
    background(255)
    strokeWeight(5)
    
# draw() -> https://py.processing.org/reference/draw.html
def draw():
    global prior_x, prior_y
    if mousePressed:
        fill(0)
        line(mouseX, mouseY, prior_x, prior_y)
        prior_x = mouseX
        prior_y = mouseY
    else:
        prior_x = mouseX
        prior_y = mouseY
    
    if keyPressed and key == "c":
        background(255)
    
