import pygame
import random
import os


class Breakout:
    def __init__(self):
        size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(size)
        self.cord = []
        self.x = 0
        self.y = 0
        self.vx = -1
        self.vy = -1
        fps = 100
        self.running = True
        self.flag = False
        self.clock = pygame.time.Clock()
        screen_rect = (0, 0, self.width, self.height)
        self.start()

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    self.x, self.y = event.pos
                    self.cord.append([self.x, self.y])
                    self.flag = True
                    flag = True
            self.polygon()
            self.ball()
            self.clock.tick(100)
            pygame.display.flip()

    def polygon(self):
        pygame.draw.rect(self.screen, pygame.Color('white'), (min(self.x, 720), 760, 80, 30))
    
    
    def ball(self):
        if self.flag:
            self.screen.fill((0, 0, 0))
            if self.x >= (self.width-5) or self.x <= 5:
                self.vx = -self.vx
            if self.y >= (self.height-5) or self.y <= 5:
                self.vy = -self.vy
            pygame.draw.circle(self.screen, pygame.Color('white'), (int(self.x), int(self.y)), 10)
            self.x += self.vx
            self.y += self.vy
    
    def brick(self):
        pass

    def destruction(self):
        pass

def main():
    Breakout().run()


if __name__ == '__main__':
    main()