# спираль
import turtle
turtle.shape('turtle')

n=40
l=15
turtle.left(90)
for k in range(10):
    for i in range(n):
        turtle.forward(l)
        turtle.left(360/n)
        l=l+0.1

a=int(input())
