import turtle as t
import random

score = 0
playing = False
my_speed = 10

tr=t.Turtle()
tr. shape("turtle")
tr.color("red")
tr.speed(0)
tr.up()
tr.goto(0, 200)

tb=t.Turtle()
tb.shape("turtle")
tb.color("blue")
tb.speed(0)
tb.up()
tb.goto(-200,0)

tg = t.Turtle()
tg.shape("circle")
tg.color("green")
tg.speed(0)
tg.up()
tg.goto(0, -200)

ty = t.Turtle()
ty.shape("circle")
ty.color("yellow")
ty.speed(0)
ty.up()
ty.goto(200, 0)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)
    
def turn_left():
    t.setheading(180)
    
def turn_down():
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing=True
        t.clear()
        play()

def play():
    global score
    global playing
    global my_speed

    t. forward(my_speed)

    if random.randint(1,5) == 3:
        ang = tr.towards(t.pos())
        tr.setheading(ang)

    speed = score+5

    if speed>15:
        speed=15
    
    tr.forward(speed)

    if random.randint(1,10) ==5:
        ang2 = tb.towards(t.pos())
        tb.setheading(ang2)

    speed2 = score+8

    if speed2>15:
        speed2=15
        
    tb.forward(speed2)

    if my_speed>15:
        my_speed = 15
   
    
    if t.distance(tr)<12:
        text = "Score :" + str(score) 
        message("Game Over" , text) 
        playing = False  
        score = 0
        my_speed=10
        tr.goto(0, 200)
        tb.goto(-200,0)
        tg.goto(0, -200)
        ty.goto(200, 0)
        tr.setheading(0)
        tb.setheading(0)

        
    if t.distance(tb)<12:
        text = "Score :" + str(score) 
        message("Game Over" , text) 
        playing = False  
        score = 0
        my_speed=10
        tr.goto(0, 200)
        tb.goto(-200,0)
        tg.goto(0, -200)
        ty.goto(200, 0)
        tr.setheading(0)
        tb.setheading(0)

    if t.distance(tg) <12:
        score = score+1
        t.write(score)
        star_x = random.randint(-230,230)
        star_y = random.randint(-230,203)
        tg.goto(star_x,star_y)
 
    if t.distance(ty) <12:
        my_speed = my_speed +0.5 
        star_xr = random.randint(-230,230)
        star_yr = random.randint(-230,203)
        star_xb = random.randint(-230,230)
        star_yb = random.randint(-230,203)
        tr.goto(star_xr,star_yr)
        tb.goto(star_xb,star_yb)
     
        star_x1 = random.randint(-230,230)
        star_y1 = random.randint(-230,203)
        ty.goto(star_x1,star_y1)

    if playing:
        t.ontimer(play,100)

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("",15))
    t.home()
        
t.title("Turtle Run Program") 
t. setup(500,500)
t.bgcolor("gray")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")

t.listen()

message("Turtle Run Game", "[Space]")



















    



