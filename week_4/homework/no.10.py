import turtle

side = 100

turtle.Screen()

triangle = turtle.Turtle()
triangle.shape('turtle')

for _ in range(3):
    triangle.forward(side)
    triangle.left(120)

turtle.done()