# alex scott, early 2021

# store all ball objects in a list
ball_list = []
ball_count = 25

def setup():
    size(200, 200)
    background(50, 204, 150)
    noStroke()
    for i in range(ball_count):
        ball_size = (i + 5) / 2
        ball_list.append(ball(ball_size))
    
def draw():
    background(50, 204, 150)
    for i in range(ball_count):
        ball_list[i].draw()
    
class ball():
    def __init__(self, d):
        print("new ball, {} pixel diameter".format(d))
        self.d = d
        self.x = random(self.d, width-self.d)
        self.y = random(self.d, height-self.d)
        self.x_vel = random(-2, 2)
        self.y_vel = random(-2, 2)
        
    def draw(self):
        self.x += self.x_vel
        self.y += self.y_vel
        if self.x > width - self.d / 2 or self.x < self.d / 2:
            self.x_vel *= -1 
        if self.y > height - self.d / 2 or self.y < self.d / 2:
            self.y_vel *= -1
        circle(self.x, self.y, self.d)
