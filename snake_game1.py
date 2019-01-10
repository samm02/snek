
import turtle

# Set up the screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off animantion on the screen

# main code goes here

# Snake head
head = turtle.Turtle()
head.speed(0) #animation speed of the turtle module



wn.mainloop() # keeps the window open