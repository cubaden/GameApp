import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("First Program")

mike_umbrella_image = pygame.image.load("images/umbrella.png")

screen = pygame.display.set_mode((1000,600))

clock = pygame.time.Clock()

raindrop_spawn_time = 0

class Mike:
    def __init__(self):
        self.x = 300
        self.y = 100

    def draw(self):
        screen.blit(mike_umbrella_image, (self.x, self.y))

    def hit_by(self, raindrop):
        return pygame.Rect(self.x, self.y, 170, 300).collidepoint((raindrop.x, raindrop.y))

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = -8
        self.speed = random.randint(5, 18)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x, self.y+8), 1)
    def off_screen(self):
        return self.y > 800

raindrops = []
mike = Mike()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        raindrops.append(Raindrop())
        #pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_RIGHT]:        
        #    xpos += 1
        #if pressed_keys[K_LEFT]:        
        #    xpos -= 1
        screen.fill((255,255,255))
        mike.draw()
        i = 0
        while i < len(raindrops):
            raindrops[i].move()
            raindrops[i].draw()
            if raindrops[i].off_screen() or mike.hit_by(raindrops[i]):
                del raindrops[i]
                i -= 1
            i += 1
        pygame.display.update()
