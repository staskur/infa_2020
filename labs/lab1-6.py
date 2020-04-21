import turtle
turtle.shape('turtle')
# звезда
n=12
r=100

for i in range(0,n,1):
    turtle.forward(r)
    turtle.stamp()
    turtle.backward(r)
    turtle.left((360/n)*1)

a=int(input())