from pygame.sprite import Sprite
from pygame import Surface

GRAVITI = 0.4
PLAYER_SPEED = 7
class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((22,32))
        self.image.fill((128, 0, 128))
        self.rect = self.image.get_rect() #Создаём прямоугольник для дальнейшей работы
        self.speed_x = 0
        self.speed_y = 0
        self.rect.x = x
        self.rect.y = y
        self.onGround = False

    def update(self, left, right):
        if (right):
            self.speed_x = PLAYER_SPEED
        elif (left): 
            self.speed_x = - PLAYER_SPEED
        else:
             self.speed_x = 0
        if(not self.onGround):
            self.speed_y += GRAVITI
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x