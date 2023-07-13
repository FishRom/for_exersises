import os.path
import sys
from random import randrange

import pygame.image


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print('not found file')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
    return image


if __name__ == '__main__':
    screen = pygame.display.set_mode((620, 620))
    running = True
    screen.fill((0, 0, 0))
    image = load_image('data/mario_2.png', -1)
    img_1 = image.subsurface((200, 0, 100, 100))
    img_2 = pygame.transform.scale(image, (100, 100))

    all_sprite = pygame.sprite.Group()

    sprite_mario = pygame.sprite.Sprite(all_sprite)
    sprite_mario.image = img_2
    sprite_mario.rest = sprite_mario.image.get_rect()

    sprite_mario.rect.x = randrange(20, 600)
    sprite_mario.rect.y = randrange(20, 600)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(img_2, (0, 0))
        pygame.display.flip()