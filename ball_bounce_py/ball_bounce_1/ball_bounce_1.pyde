# alex scott, early 2021

"""
the goal of this program is to illustrate WHY object orientation is needed
after a student finishes ball_bounce_0, ball_bounce_1 shows us there must be
a better way to add a second bouncing ball to the screen! 

Adding a second bouncing ball required adding additional conditional statments,
new variables, and new function calls. ball_bounce_2 introduces OOP
"""

# ball_a
a_x = 100
a_y = 100
a_xspeed = 2.5
a_yspeed = 2
a_ball_size = 25

# ball_b 
b_x = 50
b_y = 50
b_xspeed = 2
b_yspeed = 2.5
b_ball_size = 30

def setup():
    size(200, 200)
    noStroke()

def draw():
    background(255)
    # global allows us to modify vars in draw() after their declaration 
    global a_x, a_y, a_xspeed, a_yspeed, b_x, b_y, b_xspeed, b_yspeed
    a_x = a_x + a_xspeed
    a_y = a_y + a_yspeed
    b_x = b_x + b_xspeed
    b_y = b_y + b_yspeed
    if (a_x > width - a_ball_size//2) or (a_x < a_ball_size//2):
        a_xspeed = a_xspeed * -1
    if (a_y > height - a_ball_size//2) or (a_y < a_ball_size//2):
        a_yspeed = a_yspeed * -1
    if (b_x > width - b_ball_size//2) or (b_x < b_ball_size//2):
        b_xspeed = b_xspeed * -1
    if (b_y > height - b_ball_size//2) or (b_y <b_ball_size//2):
        b_yspeed = b_yspeed * -1
    fill(0)
    circle(a_x, a_y, a_ball_size)
    fill(128)
    circle(b_x, b_y, b_ball_size)
