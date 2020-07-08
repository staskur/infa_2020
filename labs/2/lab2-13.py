# смайлик
import turtle
window = turtle.Screen()
window.title(u"смайлик")
turtle.shape('turtle')

# желтая морда
turtle.left(90)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()
# левый синий глаз
turtle.left(90)
turtle.goto(-140,50)
turtle.fillcolor("blue")
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()
# правый синий глаз
turtle.goto(-60,50)
turtle.fillcolor("blue")
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()
# черный нос
turtle.goto(-100,20)
turtle.color("black")
turtle.pensize(8)
turtle.left(90)
turtle.pendown()
turtle.forward(30)
turtle.penup()
# красный рот
turtle.goto(-50,-20)
turtle.color("red")
turtle.pensize(9)
turtle.pendown()
turtle.circle(-50,180)
turtle.penup()

turtle.exitonclick()
