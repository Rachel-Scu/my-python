import turtle
#头
turtle.pensize(5)
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
#铃铛
turtle.goto(0,5)
turtle.pensize(15)
turtle.pencolor('red')
turtle.forward(50)
turtle.backward(100)
turtle.penup()
turtle.goto(0,-30)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor('black')
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(18)
turtle.end_fill()
#嘴巴
turtle.penup()
turtle.goto(0,30)
turtle.pendown()
turtle.circle(60,90)
turtle.circle(60,-180)
turtle.penup()
turtle.goto(0,30)
turtle.setheading(90)
turtle.pendown()
turtle.forward(75)
#胡子
#右边胡子
turtle.penup()
turtle.goto(10,90)
turtle.right(90)
turtle.pendown()
turtle.forward(65)
turtle.penup()
turtle.goto(10,80)
turtle.right(10)
turtle.pendown()
turtle.forward(60)
turtle.penup()
turtle.goto(10,100)
turtle.left(20)
turtle.pendown()
turtle.forward(60)
#左边胡子
turtle.penup()
turtle.goto(-10,90)
turtle.setheading(180)
turtle.pendown()
turtle.forward(65)
turtle.penup()
turtle.goto(-10,80)
turtle.left(10)
turtle.pendown()
turtle.forward(60)
turtle.penup()
turtle.goto(-10,100)
turtle.right(20)
turtle.pendown()
turtle.forward(60)
#眼睛
#左眼
turtle.penup()
turtle.goto(-20,175)
turtle.fillcolor('white')
turtle.pendown()
turtle.begin_fill()
turtle.circle(20,620)
turtle.end_fill()
turtle.fillcolor('black')
turtle.pendown()
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()
turtle.showturtle()
#右眼
turtle.penup()
turtle.goto(35,150)
turtle.fillcolor('white')
turtle.pendown()
turtle.begin_fill()
turtle.circle(20,590)
turtle.end_fill()
turtle.fillcolor('black')
turtle.pendown()
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()
#鼻子
turtle.pensize(3)
turtle.penup()
turtle.goto(-10,130)
turtle.showturtle()
turtle.fillcolor('red')
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
#文字
turtle.pensize(80)
turtle.pencolor('grey')
turtle.penup()
turtle.goto(-85,-70)
turtle.pendown()
turtle.write('我有一只机器猫，变大变小变漂亮')
turtle.hideturtle()

