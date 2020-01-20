import pygame
import random
import time


class Breakout:
    def __init__(self):
        pygame.init()
        size = 800, 750
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.c = pygame.color.Color('yellow')
        drawing = False
        running = True
        self.p = []
        self.a = 400
        self.lives = 4
        self.level = 1
        self.rectans = []
        self.right = []
        self.up = []
        font = 0
        flags = False
        RIGHT = "to the right"
        LEFT = "to the left"
        STOP = "stop"
        motion = STOP
        p2 = 400
        flagrep = False
        pygame.mixer.music.load('fon music.wav')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.25)
        sound1 = pygame.mixer.Sound('block destroit.wav')
        sound2 = pygame.mixer.Sound('plitca.wav')
        self.dlina = 80
        self.rad = 10
        num1 = random.randint(1, 2)
        num2 = random.randint(1, 2)
        num3 = random.randint(1, 2)
        #self.polygon()
        self.score = 0
        clock = pygame.time.Clock()
        self.random_rects()
        while running:
            flag = False
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    flag = True
                    self.a = event.pos[0]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    flags = True
                    flagrep = False

                if event.type == pygame.KEYDOWN:
                    flags = True
                    if event.key == pygame.K_LEFT:
                        motion = LEFT
                    if event.key == pygame.K_RIGHT:
                        motion = RIGHT
                    if event.key == pygame.K_ESCAPE:
                        exit()
                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        motion = STOP

            if motion == LEFT:
                self.a -= 3
                if self.a < 1:
                    self.a = -self.a
            elif motion == RIGHT:
                self.a += 3
                if self.a > 760:
                    self.a = -self.a
            
            if self.lives == 4 and flags:
                self.p.append([self.a, p2])
                self.right.append(-1)
                self.up.append(-1)
                radius = 0
                self.lives -= 1
                
                
                    
            self.screen.fill((0, 0, 0))
            self.rects()
            #self.polygon()
            self.polygon()
            
            for i in range(len(self.p)):
                for j in self.rectans:
                    if ((j[1][0] <= self.p[i][0] and j[1][0] + j[1][2] >= self.p[i][0] and
                        self.p[i][1] - self.rad == j[1][1] + j[1][3] - 1)
                        or (j[1][0] <= self.p[i][0] and j[1][0] + j[1][2] >= self.p[i][0] and
                        self.p[i][1] - self.rad == j[1][1] - 1)
                        or (j[1][1] <= self.p[i][1] and j[1][1] + j[1][3] >= self.p[i][1] and
                        self.p[i][0] + self.rad == j[1][0] + j[1][2] - 1)
                        or (j[1][1] <= self.p[i][1] and j[1][1] + j[1][3] >= self.p[i][1] and
                        self.p[i][0] + self.rad == j[1][0] + j[1][2] - 1)):
                        
                        self.up[i] = -self.up[i]
                        self.rectans.remove(j)
                        sound1.play()
                        self.score += 1

                pygame.draw.circle(self.screen, self.c,
                                   (int(self.p[i][0]), int(self.p[i][1])), self.rad)
                self.p[i][0] += self.right[i]
                self.p[i][1] += self.up[i]
                if self.p[i][0] >= 801:
                    self.right[i] = -self.right[i]
                    sound2.play()
                if (self.p[i][1] + self.rad == 660 and self.p[i][0] <= min(690, self.a) + self.dlina and
                    self.p[i][0] >= min(800 - self.dlina, self.a)):
                    self.up[i] = -self.up[i]
                    sound2.play()
                if self.p[i][0] <= -1:
                    self.right[i] = -self.right[i]
                    sound2.play()
                if self.p[i][1] <= -1:
                    self.up[i] = -self.up[i]
                    sound2.play()
                if self.p[i][1] >= 660:
                    if self.lives > 0:
                        self.p.pop()
                        self.right.pop()
                        self.up.pop()
                        self.p.append([self.a, p2])
                        self.right.append(-1)
                        self.up.append(-1)
                        radius = 0
                        self.lives -= 1
                    else:
                        flagrep = True
                        self.rad = 10
                        self.dlina = 80
                        self.random_rects()
                        self.lives = 4
                        self.score = 0
                        self.p.pop()
                        self.right.pop()
                        self.up.pop()
                        
  
                if len(self.rectans) == 0:
                    self.newgame()

            font = pygame.font.Font(None, 25)
            font_mid = pygame.font.Font(None, 50)
            font_big = pygame.font.Font(None, 75)
            
            if flagrep:
                
                repeat = font.render("Вы проиграли, чтобы убрать уведомление нажмите пкм",True, (0,0,255))
                self.screen.blit(repeat, [200,400])
            
            text = font.render("live: "+str(self.lives),True, (0,0,255))
            self.screen.blit(text, [640,150])
            

            scores = font.render("Score: "+str(self.score),True, (0,0,255))
            self.screen.blit(scores, [640,170])

            lev = font.render("level: "+str(self.level),True, (0,0,255))
            self.screen.blit(lev, [640,190])

            
            if not flags:
                begin = font.render("для начала игры нажмите пкм или стрелочки",True, (0,200,0))
                self.screen.blit(begin, [275,400])
            if self.score >= 10 and self.score <= 11:
                begin = font.render("good",True, (0,200,0))
                self.screen.blit(begin, [375,400])
                if num1 == 1:
                    self.dlina = 40
                elif num1 == 2:
                    self.dlina = 160

            if self.score >= 20 and self.score <= 21:
                begin = font_mid.render("awesome",True, (0,200,0))
                self.screen.blit(begin, [325,400])
                if num2 == 1:
                    self.rad = 5
                elif num2 == 2:
                    self.rad = 20
            if self.score >= 30 and self.score <= 31:
                begin = font_big.render("amazingly",True, (0,200,0))
                self.screen.blit(begin, [275,400])

            if self.a < 0:
                begin = font.render("поздравляю вы нашли пасхалку",True, (0,200,0))
                self.screen.blit(begin, [175,400])
            pygame.display.flip()
            self.clock.tick(200)

    def newgame(self):
        self.level += 1
        self.random_rects()
        self.lives = 4
        self.score = 0
        self.rad = 10
        self.dlina = 80
        self.p.pop()
        self.right.pop()
        self.up.pop()
        
        
    def polygon(self):
        #drawing = True
        pygame.draw.rect(self.screen, (255, 255, 255), (min(self.a, 720), 660, self.dlina, 30))

    def random_rects(self):
        self.rectans = []
        if self.level == 1:
            for i in range(4):
                k = 0
                while k <= 700:
                    size = random.randint(40, 80)
                    self.rectans.append(((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                         (k, i * 30, size, 30)))
                    k += size
                
                self.rectans.append(((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                     (k, i * 30, 800 - k, 30)))
        elif self.level == 2:
            x = [380, 350, 330, 300, 270, 270, 300, 330, 350, 380]
            for i in range(1, 6):
                k = x[i - 1]
                for j in range(i):
                    size = 60
                    self.rectans.append(((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                         (k, i * 30, size, 30)))
                    k += size
            for i in range(6, 10):
                k = x[i - 1]
                for j in range(11 - i):
                    size = 60
                    self.rectans.append(((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                         (k, i * 30, size, 30)))
                    k += size
        elif self.level == 3:
            for i in range(5):
                k = 300
                for j in range(5):
                    size = 60
                    self.rectans.append(((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                         (k, i * 30, size, 30)))
                    k += size
        else:
            x = [150, 180, 210, 230, 260]
            for i in range(1, 6):
                k = x[i - 1]
                for j in range(11 - i):
                    size = 60
                    self.rectans.append(((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                         (k, i * 30, size, 30)))
                    k += size
            
            
            
                
                

    def rects(self):
        for i in self.rectans:
            pygame.draw.rect(self.screen, i[0], i[1])

    def repeat(self):
        text = font.render("для начала игры нажмите пкм или стрелочки",True, (0,0,255))
        self.screen.blit(text, [640,150])
        self.random_rects()
        self.lives = 4
        


def main():
    Breakout()


if __name__ == '__main__':
    main()
