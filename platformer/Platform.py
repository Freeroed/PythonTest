from pygame.sprite import Sprite
from pygame.image import load
from os import path

class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        file_path = path.dirname(__file__) # Получения абсолютного пути к папке с игрой
        self.image = load(path.join(file_path, 'textures/brick.png')) #Загрузка картинки
        self.rect = self.image.get_rect() #Создаём прямоугольник для дальнейшей работы
        self.rect.x = x
        self.rect.y = y
