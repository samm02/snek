
import turtle
import time

delay = 0.1

# Set up the screen

wn = turtle.Screen()
wn.title("SNEK")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off animantion on the screen

# main code goes here

# Snake head
head = turtle.Turtle()
head.speed(0) #animation speed of the turtle module
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snek food
food = turtle.Turtle()
food.speed(0) #animation speed of the turtle module
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Function
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()
    move()
    time.sleep(delay)

wn.mainloop() # keeps the window open