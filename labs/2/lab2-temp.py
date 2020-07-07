# бабочка
import turtle
window = turtle.Screen()
window.title(u"бабочка")
turtle.shape('turtle')

n = int(turtle.textinput(u"крылья бабочки", "Введите количество пар крыльев: "))
r = 20
turtle.left(90)
for x in range(1,n+1):
    turtle.circle(r)
    turtle.circle(-r)
    r+=10

turtle.exitonclick()
