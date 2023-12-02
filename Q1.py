import turtle

# Initialize the turtle screen
screen = turtle.Screen()
screen.title("Drone Movement Simulation")
screen.bgcolor("white")

# Create the drone turtle
drone = turtle.Turtle()
drone.shape("triangle")
drone.color("red")
drone.speed(2)

# Function to move the drone forward
def move_forward():
    drone.forward(50)

# Function to move the drone backward
def move_backward():
    drone.backward(50)

# Function to move the drone left
def move_left():
    drone.left(90)

# Function to move the drone right
def move_right():
    drone.right(90)

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Main loop to keep the window open
turtle.done()