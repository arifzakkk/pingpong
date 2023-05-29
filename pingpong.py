from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('PingPong')
background = transform.scale(image.load('background.jpg'), (700, 500))
clock = time.Clock()




class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y,width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage),  (width, height))
        self.speed = 10
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
  
    def update_l(self):
        key_presed = key.get_pressed()
   
        if key_presed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_presed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    
    def update_r(self):
        key_presed = key.get_pressed()
        if key_presed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_presed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed





racket1 = Player('racket.png', 20,200,30,100,15)
racket2 = Player('racket.png', 50,200,30,100,15)
ball = GameSprite('tenis_ball.png', 300, 200, 50,50, 20)
finish = False
game = True
while game:
    window.blit(background, (0, 0))
    racket1.reset()
    racket1.update_l()
    racket2.reset()
    racket2.update_r()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False


    
    display.update()
    clock.tick(60)
