from random import randrange as rnd, choice # импорт операторов случайного выбора значений
import tkinter as tk
import math
import time


root = tk.Tk() # создание корневого окна
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

class Ball:
    def __init__(self, x=40, y=450): # рисуем шарик рандомного цвета с начальными координатами в  (40, 450) и заданной скоростью
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color) # рисуем сам шарик
        self.live = 30 # каждому шарику отводим время жизни, равное 30 прыжкам

    def set_coords(self): # задаём координаты шарика в текущий момент времени
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y <= 550: # проверяем находится ли шарик в границах экрана, то есть не пробьёт ли он пол (550, а не 600 с учётом толщины шарика)
            self.vy -= 1.2 # скорость по вертикали уменьшаем по горизонтале сохраняем, ведь учитываем баллистически только гравитацию
            self.y -= self.vy # смещаем шарик по оси ординат
            self.x += self.vx # смещаем шарик по оси абсции в соответсвии с преждней скоростью
            self.vx *= 0.99
            self.set_coords() # задаём парметры скоростьи и координат в случае выхода за границы экрана для дальнейшей реализации программы
        else:
            if self.vx ** 2 + self.vy ** 2 > 10: # если шарик намеревается пробить пол, то сбавим его скорость и вернём координаты до столкновения, изменим направление скорости по вертикали
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 499 # старт шарика с самолго пола вверх
            if self.live < 0: # если время жизни шарика истекло, удалим его
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1 # в каждый момент времени уменьшаем время жизни шарика (с каждый прыжком)
        if self.x > 780: # если шарик летит слишком далеко влево, развернём его по оси абсции и начнём движение с самоё границы левой стенки с учётом толщины шарика так что (779)
            self.vx = - self.vx / 2
            self.x = 779

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        d = math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)
        if d <= (self.r + obj.r):
            return True
        else:
            return False


class Gun:
    def __init__(self):
        self.f2_power = 10 #  начальное значений мощности выстред=ла
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7) # сам вид пушки - линия с заданным и координатами и толщины 7

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball] # добавление нового шарика в массив - очередной выстрел
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.live = 1

    def new_target(self): # создание цели в заданном диапазоне (красного цвета)
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t1 = Target()
screen1 = canv.create_text(400, 300, text='', font='28') # разиер тектового окна и шрифта
g1 = Gun()
bullet = 0 # количество выстрелов
balls = [] # масси шариков - снарядов


def new_game(event=''): # создание новой игры
    global Gun, t1, screen1, balls, bullet # инициализация действующих обЪектов, а именно, пушка, экран-дисплей, массив шариков, их количество
    t1.new_target() # новая цель
    bullet = 0 # количество выстрелов
    balls = [] # масси шариков - снарядов
    canv.bind('<Button-1>', g1.fire2_start) # привязка клавиш (операция bind) к панеле управления, здесь при зажатии левой кнопки мыши мгногвенный выстрел с дефолтными значениям скорости шарика
    canv.bind('<ButtonRelease-1>', g1.fire2_end) # при отпускании левой кнопки мыши шарик вылетает
    canv.bind('<Motion>', g1.targetting) #  увеличение начальной скорости шарика при зажатии левой кновки мыши

    z = 0.03
    t1.live = 1 #
    while t1.live or balls: #
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03) # частота обновления кадров FPS
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(Gun)
    root.after(750, new_game)

new_game()

root.mainloop() # метод вывода на экран реализации программы