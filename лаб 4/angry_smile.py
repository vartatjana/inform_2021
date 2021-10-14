import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((300, 300))

rect(screen, (218, 218, 218), (0, 0, 300, 300))
circle(screen, (255, 255, 0), (150, 150), 75)
circle(screen, (0, 0, 0), (150, 150), 75, 1)
circle(screen, (255, 0, 0), (112, 134), 15)
circle(screen, (0, 0, 0), (112, 134), 15, 1)
circle(screen, (0, 0, 0), (112, 134), 7)
circle(screen, (255, 0, 0), (187, 134), 11)
circle(screen, (0, 0, 0), (187, 134), 11, 1)
circle(screen, (0, 0, 0), (187, 134), 5)
polygon(screen, (0, 0, 0), [(112,187), (187,187), (187,200), (112,200)])
polygon(screen, (0, 0, 0), [(76,86), (135,123), (132,130), (72,93)])
polygon(screen, (0, 0, 0), [(164,123), (223,100), (225,107), (166,129)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()