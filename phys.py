import turtle as tur
tur.shape('circle')
tur.color('blue')
tur.shapesize(0.5)
tur.speed(0)

x, y, v, u, t, T, g = 0.1, 0.1, 10, 50, 0, 0, 10

tur.goto(700, 0.1)
tur.goto(-300, 0.1)


while u > 0:
    if y > 0:
        x = v * T - 300
        y = u * t - (t**2 * g/2) + 0.1
        tur.goto(x, y)
        t += 0.01
        T += 0.01
    elif y <= 0:
        x = v * T - 300
        t = 0
        u /= 1.3
        y = u * t - (t ** 2 * g / 2) + 0.1
        tur.goto(x, y)
        t += 0.01
        T += 0.01
