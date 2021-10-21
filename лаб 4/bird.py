import pygame

from pygame.draw import *
pygame.init()
FPS = 30
pi = 3.14159

screen = pygame.display.set_mode((434, 615))
pygame.draw.rect(screen, (27, 27, 121), (0, 0, 434, 60))
pygame.draw.rect(screen, (142, 95, 212), (0, 60, 434, 96 ))
pygame.draw.rect(screen, (206, 136, 223), (0, 96, 434, 152))
pygame.draw.rect(screen, (223, 136, 172), (0, 152, 434, 234))
pygame.draw.rect(screen, (255, 154, 84), (0, 234, 434 , 300))
pygame.draw.rect(screen, (0, 102, 129), (0, 300, 434 , 615))


def easy_birds():
    pygame.draw.arc(screen, (255, 255, 255), (53, 16, 70, 60), pi/3, pi/1.1)
    pygame.draw.arc(screen, (255, 255, 255), (100, 8, 70, 60), pi/4, pi/1.2)
    pygame.draw.arc(screen, (255, 255, 255), (53, 16, 75, 60), pi/3, pi)
    pygame.draw.arc(screen, (255, 255, 255), (215, 104, 65, 35), pi/8, pi/1.1)
    pygame.draw.arc(screen, (255, 255, 255), (274, 104, 65, 35), pi/7, pi/1.14)
    pygame.draw.arc(screen, (255, 255, 255), (62, 193, 75, 60), pi/6, pi/1.3)
    pygame.draw.arc(screen, (255, 255, 255), (112, 206, 75, 60), pi/6, pi/1.5)


def painfull_bird():
    polygon(screen, (255, 255, 255), [(64, 309), (87, 327), (134, 345), (187, 357), (204, 423), (147, 435), (136, 430), (141, 438), (137, 455), (112, 454), (90, 443), (104, 402), (59, 390), (30, 354), (56, 366), (97, 376), (133, 374), (86, 350)])
    pygame.draw.lines(screen, (0, 0, 0), False, [(185, 423), (162, 377), (133, 374)])
    pygame.draw.lines(screen, (0, 0, 0), False, [(136, 430), (117, 414), (104, 402)])
    pygame.draw.ellipse(screen, (255, 255, 255), (135, 423, 110, 50))
    pygame.draw.ellipse(screen, (255, 255, 255), (228, 433, 57, 23))
    pygame.draw.ellipse(screen, (255, 255, 255), (271, 420, 40, 26))
    pygame.draw.ellipse(screen, (0, 0, 0), (297, 428, 7, 5))
    polygon(screen, (255, 222, 84), [(309, 429), (342, 426), (350, 433), (342, 441), (309, 437), (310, 432)])
    pygame.draw.lines(screen, (0, 0, 0), False, [(309, 429), (342, 426), (350, 433), (342, 441), (309, 437)])
    pygame.draw.lines(screen, (0, 0, 0), False, [(309, 429), (325, 433), (350, 433)])
    polygon(screen, (255, 231, 129),[(256, 503), (269, 498), (277, 497), (286, 503), (267, 503), (278, 503), (288, 510), (267, 506), (274, 508),(285, 516), (264, 507), (255, 509), (252, 528), (250, 510)])
    pygame.draw.lines(screen, False, (255, 231, 129),[(256, 503), (269, 498), (277, 497), (286, 503), (267, 503), (278, 503), (288, 510), (267, 506), (274, 508),(285, 516), (264, 507), (255, 509), (253, 532), (249, 511)])
    polygon(screen, (255, 231, 129),[(242, 516), (254, 514), (263, 513), (272, 519), (253, 519), (264, 519), (274, 526), (253, 525), (260, 524),(271, 532), (250, 523), (241, 525), (241, 549), (235, 527)])
    pygame.draw.lines(screen, False, (0, 0, 0),[(242, 516), (254, 514), (263, 513), (272, 519), (253, 519), (264, 519), (274, 526), (253, 525), (260, 524),(271, 532), (250, 523), (241, 525), (241, 550), (235, 527)])
    polygon(screen, (255, 255, 255),
            [(215, 470), (217, 490), (255, 503), (249, 512), (203, 496), (203, 501), (241, 516), (237, 525), (185, 509),
             (173, 493), (167, 470)])


def painfull_fish():
    polygon(screen, (69, 137, 148), [(222, 546), (256, 551), (227, 569)])
    polygon(screen, (102, 99, 113), [(290, 537), (270, 523), (308, 528), (310, 539)])
    pygame.draw.lines(screen, (0, 0, 0), True, [(290, 537), (270, 523), (308, 528), (310, 539)])
    pygame.draw.lines(screen, (0, 0, 0), True, [(222, 546), (257, 550), (226, 570)])
    polygon(screen, (102, 99, 113), [(311, 560), (323, 568), (308, 578), (303, 562)])
    pygame.draw.lines(screen, (0, 0, 0), True, [(311, 560), (323, 568), (308, 578), (303, 562)])
    polygon(screen, (102, 99, 113), [(282, 563), (281, 574), (264, 571), (274, 560)])
    pygame.draw.lines(screen, True, (102, 99, 113), [(282, 563), (281, 574), (264, 571), (274, 560)])
    pygame.draw.ellipse(screen, (69, 137, 148), (256, 536, 70, 28))
    pygame.draw.ellipse(screen, (0, 0, 0), (256, 536, 70, 28), 1)
    pygame.draw.circle(screen, (0, 50, 190), (313, 550), 5)
    pygame.draw.circle(screen, (0, 0, 0), (314, 551), 2)



easy_birds()
painfull_bird()
painfull_fish()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
