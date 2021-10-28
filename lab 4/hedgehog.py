import pygame
import math
import random
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 555))
clock = pygame.time.Clock()
FPS = 30

#background
rect(screen, (40, 161, 90), (0, 0, 700, 430))
rect(screen, (108, 93, 82), (0, 334, 400, 550))

#trees
rect(screen, (213, 172, 0), (0, 0, 30, 362))
rect(screen, (213, 172, 0), (50, 0, 95, 550))
rect(screen, (213, 172, 0), (280, 0, 40, 362))
rect(screen, (213, 172, 0), (365, 0, 28, 406))

def fly_agaric(a) :
    ellipse(screen, (255, 255, 255), (178+a, 533, 15, 45))
    ellipse(screen, (255, 0, 0), (163+a, 523, 45, 15))
    circle(screen, (255, 255, 255), (170+a, 526), 2)
    circle(screen, (255, 255, 255), (180+a, 528), 2)
    circle(screen, (255, 255, 255), (190+a, 526), 2)
    circle(screen, (255, 255, 255), (200+a, 528), 2)

fly_agaric(0)
fly_agaric(50)
fly_agaric(100)
fly_agaric(150)
fly_agaric(200)



def hedgehog(a, b, c):
    ellipse(screen, (70, 52, 52), (207+a, 445+b, 150*c, 60*c)) #body

    ellipse(screen, (255, 255, 255), (207+a, 445+b, 150*c, 60*c), 1)

#feet
    ellipse(screen, (70, 52, 52), (206 + a, 488 + b, 20 * c, 6 * c))
    ellipse(screen, (70, 52, 52), (219 + a, 496 + b, 20 * c, 6 * c))
    ellipse(screen, (70, 52, 52), (323 + a, 496 + b, 20 * c, 6 * c))
    ellipse(screen, (70, 52, 52), (339 + a, 487 + b, 20 * c, 6 * c))

    ellipse(screen, (255, 255, 255), (206 + a, 488 + b, 20 * c, 6 * c), 1)
    ellipse(screen, (255, 255, 255), (219 + a, 496 + b, 20 * c, 6 * c), 1)
    ellipse(screen, (255, 255, 255), (323 + a, 496 + b, 20 * c, 6 * c), 1)
    ellipse(screen, (255, 255, 255), (339 + a, 487 + b, 20 * c, 6 * c), 1)

#head
    ellipse(screen, (70, 52, 52), (331+a, 471+b, 35*c, 16*c))

    ellipse(screen, (255, 255, 255), (331+a, 471+b, 35*c, 16*c), 1)

#eyes
    circle(screen, (0, 0, 0), (350+a, 478+b), 2*c)
    circle(screen, (0, 0, 0), (354+a, 474+b), 2*c)



    for _ in range(80):
        displacement_x = random.randint(-60*c, 60*c)
        displacement_y = random.randint(-20*c, 20*c)
        x, y = [280 + a + displacement_x, 475 + b + displacement_y]

        polygon(screen, (31, 21, 21), [[x, y], [x + 4*c, y - 48*c], [x + 8*c, y]])

    circle(screen, (255, 0, 0), (307+a, 446+b), 20*c) #apple

    circle(screen, (255, 255, 255), (307+a, 446+b), 20*c, 1)

    circle(screen, (201, 114, 52), (234+a, 446+b), 20*c) #first orange

    circle(screen, (255, 255, 255), (234+a, 446+b), 20*c, 1)

    circle(screen, (201, 114, 52), (240+a, 443+b), 20*c) #second orange

    circle(screen, (255, 255, 255), (240+a, 443+b), 20*c, 1)

# fly agaric
    ellipse(screen, (255, 255, 255), (254+a, 413+b, 16*c, 46*c))
    ellipse(screen, (255, 0, 0), (237+a, 410+b, 46*c, 16*c))
    circle(screen, (255, 255, 255), (245+a, 417+b), 2*c)
    circle(screen, (255, 255, 255), (255+a, 415+b), 2*c)
    circle(screen, (255, 255, 255), (265+a, 417+b), 2*c)
    circle(screen, (255, 255, 255), (275+a, 415+b), 2*c)

    for _ in range(80):
        displacement_x = random.randint(-60 * c, 60 * c)
        displacement_y = random.randint(-20 * c, 20 * c)
        x, y = [280 + a + displacement_x, 475 + b + displacement_y]

        polygon(screen, (31, 21, 21), [[x, y], [x + 4*c, y - 48*c], [x + 8*c, y]])


hedgehog(0, 0, 1)

hedgehog(-154, -110, 1)
rect(screen, (213, 172, 0), (50, 0, 95, 550))

hedgehog(-294, 54, 1)

hedgehog(130, -130, 1)


pygame.display.update()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()