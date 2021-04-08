# alex scott, early 2021
# Click to drop circles on the screen
# press "c" to clear the screen

# setup() -> https://py.processing.org/reference/setup.html
def setup():
    size(200, 200)
    background(255)
    
# draw() -> https://py.processing.org/reference/draw.html
def draw():
    if mousePressed:
        fill(0)
        circle(mouseX, mouseY, 5)
    
    if keyPressed and key == "c":
        background(255)
        
    if key == "s":
        saveFrame()
        
# Additional Reading
# https://py.processing.org/reference/keyPressed_var.html
# https://py.processing.org/reference/key.html
# https://py.processing.org/reference/mousePressed_var.html
# https://py.processing.org/reference/mouseX.html
# https://py.processing.org/reference/mouseY.html
