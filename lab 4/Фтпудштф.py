import pygame
import math
import random
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()
FPS = 30

rect(screen, (60, 179, 113), (0, 0, 700, 430))
rect(screen, (130, 110, 80), (0, 430, 700, 270))
rect(screen, (218, 165, 32), (0, 0, 40, 470)) #trees
rect(screen, (218, 165, 32), (65, 0, 95, 700))
rect(screen, (218, 165, 32), (350, 0, 40, 470))
rect(screen, (218, 165, 32), (460, 0, 35, 520))
ellipse(screen, (190, 170, 150), (383, 597, 27, 19))
ellipse(screen, (90, 70, 40), (384, 598, 25, 17)) #leg
ellipse(screen, (190, 170, 150), (277, 589, 27, 19))
ellipse(screen, (90, 70, 40), (278, 590, 25, 17)) #leg
ellipse(screen, (190, 170, 150), (279, 539, 133, 83)) #body
ellipse(screen, (100, 80, 50), (280, 540, 130, 80))
ellipse(screen, (190, 170, 150), (282, 604, 27, 19))
ellipse(screen, (90, 70, 40), (283, 605, 25, 17)) #leg
ellipse(screen, (190, 170, 150), (369, 604, 27, 19))
ellipse(screen, (90, 70, 40), (370, 605, 25, 17)) #leg
ellipse(screen, (255, 0, 0), (365, 535, 35, 35)) #apple

for _ in range(32):
    bias_x = random.randint(0, 122)
    bias_y = random.randint(0, 53)
    x, y = [278+bias_x, 555+bias_y]
    curx = 400
    cury = 300

    angle = math.atan2(x - curx, y - cury)
    distance = math.sqrt(200 - (200 * math.cos(angle)))
    x = x + distance
    y = y + distance
    polygon(screen, (50, 40, 40), [[x, y], [x + 10,y], [x,y-80]])

ellipse(screen, (190, 170, 150), (379, 569, 63, 38)) #head
ellipse(screen, (100, 80, 50), (380, 570, 60, 35))
ellipse(screen, (0, 0, 0), (410, 578, 7, 7)) #eye
ellipse(screen, (0, 0, 0), (425, 574, 7, 7)) #eye
ellipse(screen, (0, 0, 0), (438, 585, 5, 5)) #nose
ellipse(screen, (255, 140, 0), (288, 540, 30, 30))
ellipse(screen, (255, 140, 0), (310, 554, 33, 33))
#ellipse(screen, (255, 0, 0), (365, 535, 35, 35))
ellipse(screen, (255, 255, 255), (340, 520, 12, 45))
ellipse(screen, (255, 0, 0), (320, 520, 55, 20))
ellipse(screen, (255, 255, 255), (326, 530, 5, 5))
ellipse(screen, (255, 255, 255), (334, 528, 5, 5))
ellipse(screen, (255, 255, 255), (346, 522, 5, 5))
ellipse(screen, (255, 255, 255), (360, 526, 5, 5))
ellipse(screen, (255, 255, 255), (352, 530, 5, 4))

pygame.display.update()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()