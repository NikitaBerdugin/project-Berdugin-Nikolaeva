import pygame
import random
import os
# не рабовает ошибка 
#File "c:/Users/Admin/Desktop/yandex/тест4.py", line 23, in __init__
#    self.load_image()
#  File "c:/Users/Admin/Desktop/yandex/тест4.py", line 65, in load_image
#    fullname = os.path.join('data', name)
#  File "C:\python\lib\ntpath.py", line 117, in join
#    genericpath._check_arg_types('join', path, *paths)
#  File "C:\python\lib\genericpath.py", line 152, in _check_arg_types
#    raise TypeError(f'{funcname}() argument must be str, bytes, or '
#TypeError: join() argument must be str, bytes, or os.PathLike object, not 'Breakout'

class Breakout:
    def __init__(self):
        size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(size)
        self.cord = 0
        self.x = 0
        self.y = 0
        self.vx = -1
        self.vy = -1
        fps = 100
        self.running = True
        self.flag = False
        self.clock = pygame.time.Clock()
        screen_rect = (0, 0, self.width, self.height)
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.load_image()
        self.load_level()
        self.tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.png')}
        self.tile_width = self.tile_height = 50
        self.generate_level()
        level_x, level_y = generate_level(load_level('level.txt'))
        self.start()

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    self.x, self.y = event.pos
                    self.flag = True
                    flag = True
                if event.type == pygame.MOUSEMOTION:
                    flag = True
                    self.cord = event.pos[0]
            #self.polygon()
            self.ball()
            self.all_sprites.update()
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)
            self.clock.tick(100)
            pygame.display.flip()

    def polygon(self):
        pygame.draw.rect(self.screen, pygame.Color('white'), (min(self.cord, 720), 760, 80, 30))
    
    
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

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname).convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def load_level(filename):
        filename = "data/" + filename
        # читаем уровень, убирая символы перевода строки
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        # и подсчитываем максимальную длину    
        max_width = max(map(len, level_map))
        # дополняем каждую строку пустыми клетками ('.')    
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))

    class Tile(pygame.sprite.Sprite):
        def __init__(self, tile_type, pos_x, pos_y):
            super().__init__(self.tiles_group, self.all_sprites)
            self.image = self.tile_images[tile_type]
            self.rect = self.image.get_rect().move(self.tile_width * pos_x, self.tile_height * pos_y)  
    
    def generate_level(level):
        x, y = None, None, None
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y)
                elif level[y][x] == '#':
                    Tile('wall', x, y)
                elif level[y][x] == '$':
                    Tile('wall', x, y)
        return x, y

    def destruction(self):
        pass

def main():
    Breakout().run()


if __name__ == '__main__':
    main()