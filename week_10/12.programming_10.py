import turtle
import random

t = turtle.Turtle()
turtle.Screen()

t.shape('turtle')


def square(length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)


def draw_square(x, y, c):
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.color(c)
    square(50)
    t.end_fill()


for c in ['yellow', 'red', 'purple', 'blue']:
    draw_square(random.randint(1, 100), random.randint(1, 100), c)

turtle.mainloop()
turtle.bye()
