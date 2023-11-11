import turtle

arr_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

t = turtle.Turtle()
turtle.Screen()

for i in arr_a:
    t.forward(i)
    t.stamp()
    t.backward(i)
    t.right(30)

turtle.mainloop()
turtle.bye()
