# пружуна
import turtle
window = turtle.Screen()
window.title(u"пружина")
turtle.shape('turtle')

n = 6   # количество витков
r = 30  # радиус большой
turtle.left(90)
for i in range(n):
    turtle.circle(-r,180)
    turtle.circle(-r/5,180)

turtle.exitonclick()
