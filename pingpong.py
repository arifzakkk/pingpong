from pygame import *
window = display.set_mode((700, 500))
display.set_caption('PingPong')
background = transform.scale(image.load(''), (700, 500))
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
    def update(self):
        key_presed = key.get_pressed()
   
        if key_presed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_presed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
    def fire(self):
        fire.play()
        bullet = Bullet('bullet.png', self.rect.x, self.rect.y,20, 50,  20)
        bullets.add(bullet)



game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False



    window.blit(background, (0, 0))

    display.update()
    clock.tick(60)