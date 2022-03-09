import turtle

def draw_poly(t, n, sz):
    """
    Make turtle t draw a n-sided polygon of size sz.
    """

    angle = 180 * (n-2) / n
    for i in range(n):
        t.forward(sz)
        t.left(180-angle)


wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.color('#FA30BB')
tess.pensize(3)

draw_poly(tess, 8, 50)
wn.mainloop()