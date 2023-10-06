import turtle

side = 100

turtle.Screen()

triangle = turtle.Turtle()
triangle.shape('turtle')

triangle.left(45)
triangle.forward(141)
triangle.goto(0, 0)
triangle.setheading(0)
triangle.forward(100)
triangle.left(90)
triangle.forward(100)

turtle.done()