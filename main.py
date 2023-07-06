import math

import pygame
import random


def draw(screen: pygame.Surface):
    #font = pygame.font.Font('C://WINDOWS//Fonts//segoeuil.ttf', 36)
    #text = font.render('Hello!', True, (12, 34, 56))
    #text_x = w // 2 - text.get_width() // 2
    #text_y = h // 2 - text.get_height() // 2
    #screen.blit(text, (text_x, text_y))
    #rect = pygame.Rect(0, 0, 30, 30)
    #screen.fill((34, 56, 67), (w // 2, h // 2, 30, 70))
    #for i in range(10):
     #   screen.fill((255, 56, 23), (random.random() * w, random.random() * h, 1, 1))
    pygame.draw.rect(screen, (255, 56, 66), (0, 0, 80, 90))
    pygame.draw.circle(screen, (255, 56, 89), (w // 2, h // 2), 70)
    pygame.draw.ellipse(screen, (255, 56, 89), (45, 56, 100, 90))
    pygame.draw.arc(screen, (255, 255, 1), (350, 360, 90, 90), 0, math.pi)
    pygame.draw.polygon(screen, pygame.Color('orange'), [(35, 45), (60, 120), (35, 120)])



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