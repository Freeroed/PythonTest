from pygame.sprite import Sprite
from pygame import Surface

class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((40,40))
        self.image.fill((210, 105, 30))
        self.rect = self.image.get_rect() #Создаём прямоугольник для дальнейшей работы
        self.rect.x = x
        self.rect.y = y
