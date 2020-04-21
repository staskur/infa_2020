import turtle
# больше квадратов
s=100     #длина стороны мелкого
shag=20   #расстояние между линиями
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

a=int(input())
