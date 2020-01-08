import pygame
import random
import os

class Breakout:
    def __init__(self):
        size = 800, 800
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.c = pygame.color.Color('yellow')
        #drawing = False
        running = True
        self.p = []
        self.a = 400
        self.rectans = []
        self.right = []
        self.up = []
        #self.polygon()
        clock = pygame.time.Clock()
        #self.random_rects()
        #self.load_image()
        #screen_rect = (0, 0, width, height)
        while running:
            flag = False
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    #drawing = True  # РІРєР»СЋС‡Р°РµРј СЂРµР¶РёРј СЂРёСЃРѕРІР°РЅРёСЏ
                    # Р·Р°РїРѕРјРёРЅР°РµРј РєРѕРѕСЂРґРёРЅР°С‚С‹ РѕРґРЅРѕРіРѕ СѓРіР»Р°
                    p1 = random.randint(1, 799)
                    p2 = random.randint(120, 799)
                    self.p.append([p1, p2])
                    self.right.append(random.choice([-1, 1]))
                    self.up.append(random.choice([-1, 1]))
                    radius = 0
                    
                if event.type == pygame.MOUSEMOTION:
                    flag = True
                    self.a = event.pos[0]
            

                
                    
            self.screen.fill((0, 0, 0))
            self.rects()
            #self.polygon()
            #self.polygon()
            
            for i in range(len(self.p)):
                for j in self.rectans:
                    if j[1][0]<= self.p[i][0] and j[1][0] + j[1][2] >= self.p[i][0] and self.p[i][1] == j[1][1] + j[1][3] - 1:
                        self.up[i] = -self.up[i]
                        self.rectans.remove(j)
                pygame.draw.circle(self.screen, self.c,
                                   (int(self.p[i][0]), int(self.p[i][1])), 10)
                self.p[i][0] += self.right[i]
                self.p[i][1] += self.up[i]
                if self.p[i][0] >= 801:
                    self.right[i] = -self.right[i]
                if self.p[i][1] == 758 and self.p[i][0] <= min(720, self.a) + 80 and self.p[i][0] >= min(720, self.a):
                    self.up[i] = -self.up[i]
                if self.p[i][0] <= -1:
                    self.right[i] = -self.right[i]
                if self.p[i][1] <= -1:
                    self.up[i] = -self.up[i]
            pygame.display.flip()
            self.clock.tick(200)
            
        
    def polygon(self):
        #drawing = True
        pygame.draw.rect(self.screen, (255, 255, 255), (min(self.a, 720), 760, 80, 30))

    def random_rects(self):
        for i in range(4):
            k = 0
            while k <= 700:
                size = random.randint(40, 80)
                self.rectans.append(((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                     (k, i * 30, size, 30)))
                k += size
            
            self.rectans.append(((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                 (k, i * 30, 800 - k, 30)))
            
        
    def rects(self):
        for i in self.rectans:
            pygame.draw.rect(self.screen, i[0], i[1])
    
    #def load_image(name, colorkey=None):
    #    fullname = os.path.join('data', name)
    #    image = pygame.image.load(fullname).convert()
    #    if colorkey is not None:
    #        if colorkey == -1:
    #            colorkey = image.get_at((0, 0))
    #            mage.set_colorkey(colorkey)
    #    else:
    #        image = image.convert_alpha()
    #    return image
            
        


    
        

        
def main():
    Breakout().run()


if __name__ == '__main__':
    main()