import pygame
import random

#Создание класса Шарика
class Ball:
    #Конструктор
    def __init__(self, x, y, radius, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    #Метод отрисовки
    def print(self, window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)
        self.count_position()
    
    #Метод рассчёта позиции
    def count_position(self):
        self.x += self.speed_x
        self.y += self.speed_y

    #Спаун нового шарика
    def spawn(self, x, y):
        self.x = x
        self.y = y
        speed_x = random.randint(-15,15)
        speed_y = random.randint(-6, 6)
        while (speed_x <= 4 and speed_x >= -4):
            speed_x = random.randint(-15,15)
        while (speed_y <= 3 and speed_y >= -3):
            speed_y = random.randint(-15,15)
           
        if ball_y + ball_R >= win_H or ball_y - ball_R <= 0:
            speed_y*= -1
        self.speed_x = speed_x
        self.speed_y = speed_y

pygame.init()
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
speed_x = 15
speed_y = 3
ball_R=30
#Настройки для ракетки игрока
rect_x=0
rect_y=0
rect_W=30
rect_H=150
player_speed=20

#Настройка ракетки бота
bot_rect_x = win_W-rect_W
bot_rect_y = 0
bot_speed = 5

#Настройка шрифта вывода счёта
score_font = pygame.font.Font(None, 72)

#Счёт игроков
player_score = 0
bot_score = 0 

#Создание шарика
game_ball = Ball(int(win_W/2), int(win_H/2), 30, 15, 3, (255,0,0))
game_ball.spawn(int(win_W/2), int(win_H/2))
# Основной цикл игры
while Run:
    # Настройка FPS
    clock.tick(30)
    # Заливка фона определённым цветом.
    # Цвет указывается в модели RGB(R,G,B), где насыщенность цвета указватся в пределах 0-255
    window.fill((255,255,255))
    
    #Свойства вывода текста
    p_score = score_font.render(str(player_score), 1, (0,0,255))
    b_score = score_font.render(str(bot_score), 1, (0,0,255))
    #Отрисвка счёта
    window.blit(b_score, (int(win_W/2-100),30))
    window.blit(p_score, (int(win_W/2+100),30))
    
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
        rect_y+=player_speed
    if keys[pygame.K_UP] and not(rect_y <= 0):
        rect_y-=player_speed
    
    #Движения бота за шариком
    if (bot_rect_y+(rect_H/2) < game_ball.y and bot_rect_y + rect_H <= win_H) and game_ball.x>= win_W/2:
        bot_rect_y+=bot_speed
    if (bot_rect_y+(rect_H/2) > game_ball.y and bot_rect_y >= 0)and game_ball.x>= win_W/2:
        bot_rect_y-=bot_speed

    #Отрисока прямоугоника (Окно, (Цвет), (коорддинаты левого верхнего угла, ширины и высота))
    pygame.draw.rect(window,(210,40,0),(rect_x,rect_y,rect_W,rect_H))
    # Изменение положения шарика. К текущему положению прибавляется скорость по двум осям
    pygame.draw.rect(window,(210,40,0), (bot_rect_x,bot_rect_y, rect_W, rect_H))
    game_ball.print(window)
    # Проверка столкновений со стенками и отскок от них
    

    #Проверка столкновения шарика с ракетками игрока и бота
    if (game_ball.x-game_ball.radius <= rect_W):
        if game_ball.y >= rect_y and game_ball.y <= rect_y+rect_H:
            game_ball.speed_x*=-1
            game_ball.speed_x=int(game_ball.speed_x * 1.15)
    if (game_ball.x + ball_R >= win_W- rect_W):
        if game_ball.y >= bot_rect_y and game_ball.y <= bot_rect_y+rect_H:
            game_ball.speed_x*=-1
            game_ball.speed_x=int(game_ball.speed_x * 1.15)

    #Отскок шарика от вертикальных и горизонтальных границ
    if game_ball.x + game_ball.radius >= win_W or game_ball.x - game_ball.radius <= 0:
        if game_ball.x + game_ball.radius >= win_W:
            bot_score += 1
        if game_ball.x - game_ball.radius <= 0:
            player_score += 1

        #БУДЕМ СПАВНИТЬ    
        game_ball.spawn(int(win_W/2), int(win_H/2))
           
    if game_ball.y + game_ball.radius >= win_H or game_ball.y - game_ball.radius <= 0:
        game_ball.speed_y*= -1
    
    
    # Обновление окна приложения. Выполняется в конце цикла
    pygame.display.update()
    

    