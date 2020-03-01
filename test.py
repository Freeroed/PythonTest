import pygame
# Переменная отвечающая за счётчик FPS
clock = pygame.time.Clock()
# Переменная, отвечающая за запуск игры
Run = True
# Ширина и высота окна
win_W=1000
win_H=500
# Инициализация основного окна приложения ((Ширина, высота))
window = pygame.display.set_mode((win_W,win_H))
# Настройки для шарика
ball_x = 200
ball_y = 200
speed_x = 4
speed_y = 3
ball_R=30
#Настройки для ракетки игрока
rect_x=0
rect_y=0
rect_W=30
rect_H=150

# Основной цикл игры
while Run:
    # Настройка FPS
    clock.tick(30)
    # Заливка фона определённым цветом.
    # Цвет указывается в модели RGB(R,G,B), где насыщенность цвета указватся в пределах 0-255
    window.fill((0,40,50))
    # Получение массива всех нажатых клавиш
    keys=pygame.key.get_pressed()
    #Основной цикл обработки игровых событий
    for i in pygame.event.get():
        # Обработка события закрытия приложения. Тип события сравнивается с искомым (QUIT)
        if i.type == pygame.QUIT:
            # Если происходит событие закрытия, то игра останавливается и закрывается
            Run = False
        # Обработка события нажатия клавиши
        if i.type == pygame.KEYDOWN:
            # Проверка того, какая клавиша нажата
            if i.key == pygame.K_f:
                speed_y+= 3
    #Обработка нажатия клавиш. Сравнение значения элемента массива с названием клавиши и выполнение соответствующего действия
    if keys[pygame.K_DOWN] and not(rect_y+rect_H >= win_H):
        rect_y+=20
    if keys[pygame.K_UP] and not(rect_y <= 0):
        rect_y-=20
    
    # Отрисовка круга pygame.draw.circle(Окно, на котором надо отрисовать, (цвет), (Координаты центра), радиус)
    pygame.draw.circle(window,(255,150,0),(ball_x,ball_y),ball_R)
    #Отрисока прямоугоника (Окно, (Цвет), (коорддинаты левого верхнего угла, ширины и высота))
    pygame.draw.rect(window,(210,40,0),(rect_x,rect_y,rect_W,rect_H))
    # Изменение положения шарика. К текущему положению прибавляется скорость по двум осям
    ball_x+= speed_x
    ball_y+= speed_y
    # Проверка столкновений со стенками и отскок от них
    if ball_x + ball_R >= win_W or ball_x - ball_R <= 0:
        speed_x*= -1
    if ball_y + ball_R >= win_H or ball_y - ball_R <= 0:
        speed_y*= -1
    # Обновление окна приложения. Выполняется в конце цикла
    pygame.display.update()
    

    