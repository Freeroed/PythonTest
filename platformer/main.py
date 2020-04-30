import pygame
from Platform import Platform
from Player import Player
WIN_SIZE = (640,480)
backgroundColor = ((10,120,10))

window = pygame.display.set_mode(WIN_SIZE)

class Camera:
    def __init__(self, width, height, camera_func):
        self.state = pygame.Rect(0, 0, width, height)
        self.camera_func = camera_func

    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    
def camera_func(camera, targer_rect):
    l = -targer_rect.x + WIN_SIZE[0]/2
    t = -targer_rect.y + WIN_SIZE[1]/2
    w, h = camera.width, camera.height

    l = min(0,l)
    l = max(-(camera.width - WIN_SIZE[0]), l)
    t = max(-(camera.height - WIN_SIZE[1]), t)
    t = min(0,t)

    return pygame.Rect(l, t, w, h)

#TODO добавить изменение цвета платформы
#TODO Добавить отрисовки игрока на уровень
screen  = pygame.Surface(WIN_SIZE)

level = [
    '-----------------------------------------------',
    '-                                             -',
    '-                                  ------     -',
    '-                                             -',
    '-                                             -',
    '-                   ----------                -',
    '-                                             -',
    '-   -------   ---                             -',
    '-                                             -',
    '-                   ------   ---              -',
    '-                                             -',
    '-                                    -------  -',
    '-                                             -',
    '-                                             -',
    '-                   ---      ------           -',
    '-                                             -',
    '-       --------                              -',
    '-                                             -',
    '-----------------------------------------------'
]

level_width = len(level[0])*40
level_height = len(level)*40

#Инициализация камеры
camera = Camera(level_width, level_height, camera_func)

game_Objects = pygame.sprite.Group()
platforms = []

#Создание уровня
def build_Level(level):
    x = y = 0
    for row in level:
        for col in row:
            if (col == '-'):
                pl = Platform(x,y)
                game_Objects.add(pl)
                platforms.append(pl)
            x += 40
        y += 40
        x = 0

hero  = Player(55,55)
build_Level(level)
game_Objects.add(hero)
timer = pygame.time.Clock()

left = rigth = up = 0
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] :
        left = True
    elif keys[pygame.K_RIGHT] :
        rigth = True
    else :
        left = rigth = False
    if keys[pygame.K_UP]:
        up = True
    else: 
        up = False

    screen.fill((backgroundColor))
    hero.update(left, rigth, up, platforms)
    camera.update(hero)
    for obj in game_Objects:
        screen.blit(obj.image, camera.apply(obj))
    #game_Objects.draw(screen)
    window.blit(screen, (0,0))
    pygame.display.flip()
    timer.tick(60)