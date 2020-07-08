# звезда
import turtle
window = turtle.Screen()
window.title(u"звезда")
turtle.shape('turtle')

n = int(turtle.textinput(u"вершины звезды", "Введите количество вершин звезды: "))

l= 180 # длина линии
angle=180-180/n
turtle.left(180)
for i in range(n):
    turtle.forward(l)
    turtle.left(angle)

turtle.exitonclick()

