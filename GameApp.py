import pygame, sys, random, time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("First Program")

mike_umbrella_image = pygame.image.load("images/umbrella.png")
mike_image = pygame.image.load("images/mike.png")
cloud_image = pygame.image.load("images/cloud.png")

screen = pygame.display.set_mode((1300,700))

clock = pygame.time.Clock()

last_hit_time = 0

raindrop_spawn_time = 0

class Cloud:
    def __init__(self):
        self.x = 500
        self.y = 0

    def rain(self):
        for i in range(10):
            raindrops.append(Raindrop(random.randint(self.x+75, self.x+300), self.y+150))

    def draw(self):
        screen.blit(cloud_image, (self.x, self.y))

    def move(self):
        if pressed_keys[K_RIGHT]:        
            self.x += 1
        if pressed_keys[K_LEFT]:        
            self.x -= 1

class Mike:
    def __init__(self):
        self.x = 600
        self.y = 350

    def draw(self):
        if time.time() > last_hit_time + 1:
            screen.blit(mike_image, (self.x, self.y))
        else:
            screen.blit(mike_umbrella_image, (self.x, self.y))

    def hit_by(self, raindrop):
        return pygame.Rect(self.x, self.y, 250, 300).collidepoint((raindrop.x, raindrop.y))

class Raindrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x, self.y+8), 1)

    def off_screen(self):
        return self.y > 800

raindrops = []
mike = Mike()
cloud = Cloud()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        pressed_keys = pygame.key.get_pressed()

        screen.fill((255,255,255))
        mike.draw()
        cloud.draw()
        cloud.rain()
        cloud.move()
        i = 0
        while i < len(raindrops):
            raindrops[i].move()
            raindrops[i].draw()
            flag = False
            if raindrops[i].off_screen():
                flag = True
            if mike.hit_by(raindrops[i]):
                flag = True
                last_hit_time = time.time()
            if flag:
                del raindrops[i]
                i -= 1
            i += 1
        pygame.display.update()
