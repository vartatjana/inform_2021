from tkinter import *
from random import randrange, choice

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

def new_ball():
    global x, y, r, ball
    canv.delete(ball)
    x = randrange(100, 700)
    y = randrange(100, 500)
    r = randrange(30, 50)
    ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_ball)


def click(event):
    global points, x, text
    if (event.y - y) ** 2 + (event.x - x) ** 2 <= r ** 2:
        points += 1
        x = -1000  #если без этого и delete(ball), то можно тыкать много раз пока шарик не исчез и накручивать очки
        canv.delete(text)  #если так не сделать, то каждая цифра пишется поверх
        canv.delete(ball)
        text = canv.create_text(20, 20, text=str(points), font='Arial 20')

ball = canv.create_oval(-100, 0, 0, 0)
text = canv.create_text(20, 20, text=0, font='Arial 20')
points = 0
new_ball()
canv.bind('<Button-1>', click)

mainloop()
