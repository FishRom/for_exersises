import math

import pygame
import random


def draw(screen: pygame.Surface):
    pygame.draw.circle(screen, (0, 0, 0), (w // 2, h // 2), 50, 5)
    pygame.draw.circle(screen, (0, 0, 0), (300, 420), 70, 5)
    pygame.draw.circle(screen, (0, 0, 0), (280, 300), 3)
    pygame.draw.circle(screen, (0, 0, 0), (320, 300), 3)
    pygame.draw.polygon(screen, pygame.Color('orange'), [(280, 310), (300, 300), (285, 300)])
    pygame.draw.arc(screen, (0, 0, 0), (290, 310, 30, 30), math.pi, math.pi * 2)
    pygame.draw.aaline(screen, (0, 0, 0), (230, 400), (100, 250), 15)


if __name__ == '__main__':
    pygame.init()
    size = w, h = 600, 600
    screen = pygame.display.set_mode(size)
    color = pygame.Color(25, 60, 10)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 20, hsv[3])
    screen.fill(color)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()