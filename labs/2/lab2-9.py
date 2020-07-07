# окружность
import turtle
from math import sin,pi
window = turtle.Screen()
window.title(u"Многоугольники")
turtle.shape('turtle')

#r=30  # радиус
#n=5   # количество секторов на длину окружности

def figura(radius,num):    # радиус и количество секторов на длину окружности
    dlina=abs(radius*2*sin(pi/num))   # длина стороны сектора положительное число
    turtle.penup()
    turtle.forward(radius)
    turtle.left(90-180/num)   # начальный угол поворота головы
    turtle.pendown()
    for i in range(num):
        turtle.left(360/num)
        turtle.forward(dlina)
    turtle.penup()
    turtle.home()
    return dlina

if __name__ == '__main__':
    r = 50   # начальный радиус
    for n in range(3, 13):
        figura(r,n)
        r+=25    # шаг увеличеняи радиуса

    window.exitonclick()  # ждем щелчка мышки убрать картинку
