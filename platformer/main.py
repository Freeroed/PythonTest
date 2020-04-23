import pygame
from Platform import Platform
from Player import Player
WIN_SIZE = (640,480)
backgroundColor = ((10,120,10))

window = pygame.display.set_mode(WIN_SIZE)

#TODO добавить изменение цвета платформы
#TODO Добавить отрисовки игрока на уровень
screen  = pygame.Surface(WIN_SIZE)

level = [
    '----------------',
    '-              -',
    '-   ----       -',
    '-              -',
    '-      ----    -',
    '-              -',
    '-              -',
    '-              -',
    '-  ----        -',
    '-         --   -',
    '-              -',
    '----------------'
]
game_Objects = pygame.sprite.Group()

#Создание уровня
def build_Level(level):
    x = y = 0
    for row in level:
        for col in row:
            if (col == '-'):
                pl = Platform(x,y)
                game_Objects.add(pl)
            x += 40
        y += 40
        x = 0

hero  = Player(55,55)
build_Level(level)
game_Objects.add(hero)
timer = pygame.time.Clock()

left = rigth = 0
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

    screen.fill((backgroundColor))
    hero.update(left, rigth)
    game_Objects.draw(screen)
    window.blit(screen, (0,0))

    pygame.display.flip()
    timer.tick(60)