import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Drone Movement Simulator")
screen.bgcolor("white")

# Create a drone turtle with the "turtle" shape
drone = turtle.Turtle()
drone.shape("turtle")
drone.color("green")

# Function to move the drone forward
def move_forward():
    drone.forward(50)
    print("Drone moved forward")

# Function to move the drone backward
def move_backward():
    drone.backward(50)
    print("Drone moved backward")

# Function to turn the drone left
def move_left():
    drone.left(90)
    print("Drone turned left")

# Function to turn the drone right
def move_right():
    drone.right(90)
    print("Drone turned right")

# Function to start the simulation
def start_simulation():
    screen.listen()
    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(move_left, "a")
    screen.onkey(move_right, "d")
    print("Simulation started. Use 'w', 's', 'a', 'd' to control the drone.")

# Function to reset the simulation
def reset_simulation():
    drone.goto(0, 0)
    drone.setheading(0)
    print("Simulation reset. Drone is back at the starting position.")

# Prompt user to start or reset the simulation
user_input = turtle.textinput("Start or Reset", "Enter 'start' to begin the simulation or 'reset' to reset the drone:")
if user_input.lower() == 'start':
    start_simulation()
elif user_input.lower() == 'reset':
    reset_simulation()

# Close the window on click
screen.exitonclick()
