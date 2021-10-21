import turtle
t = turtle.Pen()
t.shape('turtle')
t.color('black')

def face():
    t.down()
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.up()

def eye_one():
    t.down()
    t.fillcolor('blue')
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.up()

def eye_two():
    t.down()
    t.fillcolor('blue')
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.up()

def nose():
    t.down()
    t.color('black')
    t.pensize(8)
    t.left(180)
    t.forward(50)
    t.up()

def mouse():
    t.color('red')
    t.down()
    t.circle(-70, 180, 30)
    t.up()

t.up()
t.goto (100, 0)
t.left(90)
face()
t.goto(-30, 50)
eye_one()
t.goto(60, 50)
eye_two()
t.goto(0, 30)
nose()
t.goto(70, -10)
mouse()
turtle.exitonclick()
