'''
Напишите программу, в которой объект после нажатия на кнопку space будет из
центра передвигаться в рандомное направление. Если несколько раз нажать на пробел,
то уже будет несколько объектов.
Каждый объект должен двигаться с разной скоростью.
'''


import pygame
import random


class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.randint(1, 1)
        self.speed_y = random.randint(1, 1)
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

    def update(self):
        self.x += self.speed_x * self.direction_x
        self.y += self.speed_y * self.direction_y
        # Проверка столкновения с границами окна
        if self.x < 0 or self.x > width:
            self.direction_x *= -1

        if self.y < 0 or self.y > height:
            self.direction_y *= -1

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 10)


objects = []

if __name__ == '__main__':
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    objects.append(Object(800 // 2, 600 // 2))

        screen.fill(pygame.Color('black'))
        # Обновление и отрисовка каждого объекта
        for obj in objects:
            obj.update()
            obj.draw()

        pygame.display.flip()
    # Завершение работы Pygame
    pygame.quit()


###
