import turtle
t = turtle.Turtle()
t.shape('turtle')
n = int(turtle.textinput(u'Введите количество вершин', 'Введите количество вершин: '))
def stars(n):
    t.left(180 - (180 / n))
    t.forward(200)
x = 1
while x <= n:
    stars(n)
    x += 1
turtle.exitonclick()