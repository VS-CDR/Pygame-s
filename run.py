import sys
import pygame
from random import randint


class Ball:
    def __init__(self, screen_size):
        self.ball = pygame.image.load("basketball.png")
        self.geometry = self.ball.get_rect()
        self.size = self.width, self.height = screen_size[0], screen_size[1]
        self.geometry.x = self.width // 2
        self.geometry.y = self.height // 2
        self.direction = [randint(1, self.geometry.x // 32), randint(1, self.geometry.y // 32)]

    def draw_ball(self, screen):
        self.move()
        screen.blit(self.ball, self.geometry)

    def move(self):
        if (self.geometry.x + self.geometry.width <= 800) and (self.geometry.x >= 0):
            if (self.geometry.x + self.geometry.width == 800) or (self.geometry.x == 0):
                self.direction[0] = -self.direction[0]
            self.geometry.x += self.direction[0]
        else:
            self.direction[0] = -self.direction[0]
            self.geometry.x += self.direction[0]

        if (self.geometry.y + self.geometry.height <= 600) and (self.geometry.y >= 0):
            if (self.geometry.y + self.geometry.height == 600) or (self.geometry.y == 0):
                self.direction[1] = -self.direction[1]
            self.geometry.y += self.direction[1]
        else:
            self.direction[1] = -self.direction[1]
            self.geometry.y += self.direction[1]

    def resized_screen(self, screen_size):
	self.geometry.x = (self.geometry.x // self.width) * screen_size[0]
        self.geometry.y = (self.geometry.y // self.height) * screen_size[1]
        self.size = self.width, self.height = screen_size[0], screen_size[1]

        # self.geometry.x = self.width // 2
        # self.geometry.y = self.height // 2


def main():
    colors = {"BLACK": (0, 0, 0), "GREEN": (0, 255, 0)}
    size = width, height = 800, 600
    pygame.init()
    screen = pygame.display.set_mode(size)

    ball = Ball(size)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.VIDEORESIZE:
                size = width, height = event.w, event.h
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                ball.resized_screen()

        screen.fill(colors["BLACK"])
        ball.draw_ball(screen)

        pygame.display.flip()
        pygame.time.wait(32)

    sys.exit()


if __name__ == '__main__':
    main()
