import turtle

n = int(input('Enter the number of n: '))
t = turtle.Turtle()
for i in range(n):
    t.penup()
    t.goto(0 + (8 * i), 0 - (8 * i))
    t.pendown()
    for j in range(i + 3):
        t.left(180 - ((i + 1) * 180) / (i + 3))
        t.forward(40 + (12 * i))