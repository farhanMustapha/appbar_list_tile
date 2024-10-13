import turtle
colors=["red","violet","yellow","purple","orange","blue"]
t=turtle.Pen()
turtle.speed(1000)
turtle.bgcolor("black")

for i in range(200):
    turtle.pencolor(colors[i%6])
    turtle.width(i/100 + 1)
    turtle.forward(i)
    turtle.left(59)

turtle.done()