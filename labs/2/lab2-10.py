# цветок
import turtle
window = turtle.Screen()
window.title(u"цветок")
turtle.shape('turtle')

n = int(turtle.textinput(u"Развесистость цветка", "Введите количество лепестков: "))
def figura(x):
    for x in range(1,n+1):
        turtle.circle(50)
        turtle.left(360 / n)

figura (n)

turtle.exitonclick()
