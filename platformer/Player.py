from pygame.sprite import Sprite, collide_rect
from pygame import Surface

GRAVITI = 0.4
PLAYER_SPEED = 7
JUMP_POWER = 10
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

    def update(self, left, right, up, platforms):
        if (right):
            self.speed_x = PLAYER_SPEED
        elif (left): 
            self.speed_x = - PLAYER_SPEED
        else:
             self.speed_x = 0
        if(not self.onGround):
            self.speed_y += GRAVITI
        if(up and self.onGround and self.speed_y == 0):
            self.speed_y += -JUMP_POWER
            self.onGround = False

        self.onGround = False
        self.rect.x += self.speed_x
        self.check_colled(self.speed_x, 0, platforms)
        self.rect.y += self.speed_y
        self.check_colled(0, self.speed_y, platforms)
        
    def check_colled(self, speed_x, speed_y, platforms):
        for platform in platforms:
            if collide_rect(self, platform):
                if (speed_x > 0):
                    self.rect.right = platform.rect.left
                if (speed_x < 0):
                    self.rect.left = platform.rect.right
                if (speed_y > 0):
                    self.rect.bottom = platform.rect.top
                    self.speed_y = 0
                    self.onGround = True
                if (speed_y < 0):
                    self.rect.top = platform.rect.bottom
                    self.speed_y = 0