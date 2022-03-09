import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.color('#FA30BB')
tess.pensize(3)

x_pos = 0
y_pos = 0
size = 20

for i in range(5):
    tess.pendown()
    for i in range(4):
        tess.forward(size)
        tess.left(90)

    size += 20
    x_pos -= 10
    y_pos -=10
    tess.penup()
    tess.goto(x_pos, y_pos)

wn.mainloop()