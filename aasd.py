from turtle import *
tracer(0)
update()

k=20

for i in range(2):
    fd(10*k)
    rt(90)
    fd(20*k)
    rt(90)
    fd(10*k)
    lt(90) 
penup() 
fd(20*k)
pendown()
for i in range(2):
    fd(10*k)
    lt(90)
    fd(20*k)
    lt(90)
    fd(10*k)
    rt(90)
    fd(200*k)
penup()

for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(3 ,"red")

done()
