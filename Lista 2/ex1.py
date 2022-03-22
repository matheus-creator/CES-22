import turtle      # Tess becomes a traffic light.

# Screen setup and turtle creation

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """
    Draws a nice housing to hold the traffic lights
    """

    global pen_size
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def advance_state_machine():
    """
    Changes the states of the state machine and the color of the shape
    """

    global state_num
    if state_num == 0:      # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:    # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:                   # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
    

# Question 1 - Adding some new key bindings

def change_color_to_red():
    """
    Changes the color of the shape to red
    """

    tess.fillcolor('red')


def change_color_to_green():
    """
    Changes the color of the shape to green
    """

    tess.fillcolor('green')


def change_color_to_blue():
    """
    Changes the color of the shape to blue
    """

    tess.fillcolor('blue')


def increase_pen_size():
    """
    Increments pen's size by one
    """

    global pen_size
    pen_size += 1
    if pen_size > 20:
        pen_size = 20
    tess.pensize(pen_size)


def decrease_pen_size():
    """
    Decrements pen's size by one
    """

    global pen_size
    pen_size -= 1
    if pen_size < 1:
        pen_size = 1
    tess.pensize(pen_size)


def change_bgcolor():
    """
    Changes the background color
    """

    global bg_color
    if bg_color == 0:      # Transition from state 0 to state 1
        wn.bgcolor("blue")
        bg_color = 1
    elif bg_color == 1:    # Transition from state 1 to state 2
        wn.bgcolor("red")
        bg_color = 2
    else:                   # Transition from state 2 to state 0
        wn.bgcolor("lightgreen")
        bg_color = 0


def increase_screen_size():
    """
    Increases the size of the screen
    """

    global screen_size
    aux = screen_size
    screen_size = [screen_size[0] * 1.5, screen_size[1] * 1.5]
    if screen_size[1] > 1000:
        screen_size = aux
    turtle.setup(screen_size[0], screen_size[1])


def decrease_screen_size():
    """
    Decreases the size of the screen
    """

    global screen_size
    aux = screen_size
    screen_size = [screen_size[0] / 1.5, screen_size[1] / 1.5]
    if screen_size[0] < 100:
        screen_size = aux
    turtle.setup(screen_size[0], screen_size[1])


def increase_shape_size():
    """
    Increases the size of the shape
    """

    global shape_size
    shape_size += 0.5
    if shape_size > 6:
        shape_size = 6
    tess.shapesize(shape_size)


def decrease_shape_size():
    """
    Decreases the size of the shape
    """

    global shape_size
    shape_size -= 0.5
    if shape_size < 1:
        shape_size = 1
    tess.shapesize(shape_size)


draw_housing()

tess.penup()

# Position tess onto the place where the green light should be

tess.forward(40)
tess.left(90)
tess.forward(50)

# Turn tess into a big green circle

tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states, 
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and 
# her fillcolor.

# Variables initialization

state_num = 0
pen_size = 3
bg_color = 0
shape_size = 3
screen_size = [400, 500]

# Bind the event handler to the some keys.

wn.onkey(advance_state_machine, "space")

wn.onkey(change_color_to_red, 'r')

wn.onkey(change_color_to_green, 'g')

wn.onkey(change_color_to_blue, 'b')

wn.onkey(increase_pen_size, "plus")

wn.onkey(decrease_pen_size, "minus")

wn.onkey(change_bgcolor, "c")

wn.onkey(increase_screen_size, "s")

wn.onkey(decrease_screen_size, "h")

wn.onkey(increase_shape_size, "i")

wn.onkey(decrease_shape_size, "d")


wn.listen()     # Listen for events
wn.mainloop()


