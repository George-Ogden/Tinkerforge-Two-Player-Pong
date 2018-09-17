import simpleguitk as simplegui
import random
import math
import time as wait
from Sensors import Linear_Poti,Rotary_Poti,RGB_LED_Button,Piezo_Speaker

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 800
HEIGHT = 600       
BALL_RADIUS = 5
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0


ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [-1,1]
time = 0
score1 = 0
score2 = 0

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    qx *= random.choice([1,-1])
    return [qx, qy]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel,time # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    time = 1
    wait.sleep(0.1)
    ball_vel = rotate((0,0),(7,0),random.choice([random.randrange(135,165),random.randrange(195,225)])/180*math.pi)
    
        
def tick():
    global time
    time += 1

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball()
    RGB_LED_Button.set_value(255,255,255)
    # draw ball
    score1 = 0
    score2 = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,time
    paddle2_pos = Rotary_Poti.get_value()*(HEIGHT-80)
    paddle1_pos = Linear_Poti.get_value()*(HEIGHT-80)
    if RGB_LED_Button.get_value() == 1:
        new_game()
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
        
    # update ball
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[0] *= 1
        ball_vel[1] *= -1
        
    if ball_pos[1] >= HEIGHT-BALL_RADIUS:
        ball_vel[0] *= 1
        ball_vel[1] *= -1
    
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS) and ball_pos[1] >= paddle1_pos and ball_pos[1] <= (paddle1_pos+80):
        ball_vel[0] *= -1
        ball_vel[1] *= 1
        
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS ) and ball_pos[1] >= paddle2_pos and ball_pos[1] <= (paddle2_pos+80):
        ball_vel[0] *= -1
        ball_vel[1] *= 1
        
    ball_pos[0] += time * ball_vel[0]
    ball_pos[1] += time * ball_vel[1]
    
    if ball_pos[0] <= PAD_WIDTH:
        if not(ball_pos[1] >= paddle1_pos and ball_pos[1] <= (paddle1_pos+80)):
            score2+=1
            RGB_LED_Button.set_value(255,0,0)
            Piezo_Speaker.set_value(0.1)
            spawn_ball()
            
    if ball_pos[0] >= WIDTH - PAD_WIDTH:
        if not(ball_pos[1] >= paddle2_pos and ball_pos[1] <= (paddle2_pos+80)):
            score1+=1
            RGB_LED_Button.set_value(0,255,0)
            Piezo_Speaker.set_value(0.1)
            spawn_ball()

            
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"Blue","White")
    # update paddle's vertical position, keep paddle on the screen
    
    canvas.draw_line([0,paddle1_pos],[0,80+paddle1_pos],16,"Green")
    canvas.draw_line([796,paddle2_pos],[796,80+paddle2_pos],8,"Red")
    
    canvas.draw_text(str(score1),[230,235],95,"Blue")
    canvas.draw_text(str(score2),[530,235],95,"Blue")
    
def button1():
    new_game()
    
    
        
def keydown(key):
    pass
        
def keyup(key):
    pass

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button("Reset",button1)

timer = simplegui.create_timer(1000,tick)


# start frame
new_game()
frame.start()
timer.start()
