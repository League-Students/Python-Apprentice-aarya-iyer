import turtle
tina = turtle.Turtle()
tina.shape('turtle')

# Set up the screen
screen = turtle.Screen()

# Define functions to move Tina in different directions
def move_up():
    tina.setheading(90)
    tina.forward(20)

def move_down():
    tina.setheading(270)
    tina.forward(20)

def move_left():
    tina.setheading(180)
    tina.forward(20)

def move_right():
    tina.setheading(0)
    tina.forward(20)

# Bind the arrow keys to the movement functions
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
