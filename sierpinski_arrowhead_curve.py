import turtle

t = turtle.Turtle()
t.speed(10)
t.width(2)

t.penup()
t.goto(-325, -250)
t.pendown()

rgb = [(240, 248, 255), (230, 230, 250), (176, 224, 230), (173, 216, 230),
       (135, 206, 250), (135, 206, 235), (0, 191, 255), (176, 196, 222),
       (30, 144, 255), (100, 149, 237), (70, 130, 180), (95, 158, 160),
       (96, 130, 182), (150, 222, 209), (159, 226, 191), (0, 163, 108),
       (8, 143, 143), (204, 204, 255), (147, 177, 225)]

idx = 0
t.getscreen().colormode(255)
t.getscreen().bgcolor(35, 63, 110)
t.color(rgb[idx])


def change_color():
    global idx
    if (idx + 1) == len(rgb):
        idx = 0
    else:
        idx = idx + 1
    t.color(rgb[idx])


# 2D L-System for Sierpiński Arrowhead Curve
# axiom: A
# rules: A -> BF-AF-B, B -> AF+BF+A
# angle: 60 degrees
# iterations: 7


def a(num):
    if num == 0:
        return
    else:
        change_color()
        b(num-1)
        t.forward(5)
        t.left(60)
        a(num-1)
        t.forward(5)
        t.left(60)
        b(num-1)


def b(num):
    if num == 0:
        return
    else:
        change_color()
        a(num-1)
        t.forward(5)
        t.right(60)
        b(num-1)
        t.forward(5)
        t.right(60)
        a(num-1)


a(7)

turtle.done()
