# окружность
import turtle
turtle.shape('turtle')

n=36
l=10
turtle.penup()
turtle.forward(l)
turtle.pendown()
for i in range(n):
    turtle.forward(l)
    turtle.left(360/n)

a=int(input())
