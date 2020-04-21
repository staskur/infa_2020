import turtle
# больше квадратов
s=100
shag=20
turtle.shape('turtle')
for j in range(10):
    turtle.penup()
    turtle.right(90)
    turtle.forward(shag)
    turtle.left(90)
    turtle.backward(shag)
    turtle.pendown()
    for i in range(4):
        turtle.forward(s)
        turtle.left(90)
    s=s+2*shag


#    turtle.forward(100)
#    turtle.left(90)
#turtle.forward(100)
#turtle.left(90)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)

a=int(input())
