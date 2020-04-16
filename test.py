import pygame
import random
import sys
from os import path

#Описание класса кнопки меню
class Button():
    def __init__(self, x,y,font, name, font_color, width, heigth):
        self.x = x
        self.y = y
        self.font = font
        self.name = name
        self.font_color = font_color
        self.width = width
        self.heigth = heigth
        self.button = font.render(name, 1, font_color)

    def render(self, window):
        window.blit(self.button, (self.x, self.y))

    def check(self, mouse_x, mouse_y):
        print("")
        #TODO Дописать проверку попадания в зону кнопки

class Menu():
    def __init__(self, screen, color, buttons):
        self.screen = screen
        self.color = color
        self.buttons = buttons

    def menu(self):
        #menu_font = pygame.font.Font(None, 72)
        run = True
        while run:
            self.screen.fill(self.color)
            #start_button = menu_font.render("Начать", 1, (0,0,255))

            mousePosition = pygame.mouse.get_pos()
            for but in self.buttons:
                but.render(self.screen)
                

            #self.screen.blit(start_button, (int(win_W/2)-80,int(win_H/2)-40))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key ==pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_SPACE:
                        run = False
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 :
                    for but in self.buttons:
                        #TODO Дописать проверку нажатия на кнопку
                        but.check(mousePosition[0], mousePosition)


                    if (mousePosition[0] > win_W/2-80 and mousePosition[0] < win_W/2+80 and mousePosition[1] > win_H/2-40 and mousePosition[1] < win_H/2+40):
                        run = False
            pygame.display.flip()

#Создание класса ракетки
class Pand():
    #Конструктор
    def __init__(self, x, y, width, heitht, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.heitht = heitht
        self.color = color
        self.speed = speed

    #Отрисовка
    def print(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.heitht))
        #self.count_position()

    #Рассчёт позиции
    def count_position(self, upOfDown, win_h):
        if(upOfDown == 'up' and self.y > 0):
            self.y -=self.speed
        if(upOfDown == 'down' and self.y + self.heitht < win_h):
            self.y +=self.speed
        

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

#Создание ракетки игрока
player_pand = Pand(rect_x, rect_y , rect_W, rect_H, (255,0,0), player_speed)

#Настройка расположения музыки
sound_dir = path.join(path.dirname(__file__), 'sound')
jump_sound = pygame.mixer.Sound(path.join(sound_dir, 'Ball_jump.wav'))

#Создаём объект меню
menu_font = pygame.font.Font(None, 72)
start_button = Button(int(win_W/2)-80,int(win_H/2)-40, menu_font, 'Start', (0,0,255), 80, 40 )
#TODO Реализовать кнопку выхода из игры
buttons = [start_button]
menu = Menu(window, (252, 15, 192), buttons)
menu.menu()

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
            if i.key == pygame.K_ESCAPE:
                menu.menu()
    #Обработка нажатия клавиш. Сравнение значения элемента массива с названием клавиши и выполнение соответствующего действия
    if keys[pygame.K_DOWN] :
        player_pand.count_position('down', win_H)
    if keys[pygame.K_UP] :
        player_pand.count_position('up', win_H)
    
    #Движения бота за шариком
    if (bot_rect_y+(rect_H/2) < game_ball.y and bot_rect_y + rect_H <= win_H) and game_ball.x>= win_W/2:
        bot_rect_y+=bot_speed
    if (bot_rect_y+(rect_H/2) > game_ball.y and bot_rect_y >= 0)and game_ball.x>= win_W/2:
        bot_rect_y-=bot_speed

    #Отрисока прямоугоника (Окно, (Цвет), (коорддинаты левого верхнего угла, ширины и высота))
    #pygame.draw.rect(window,(210,40,0),(rect_x,rect_y,rect_W,rect_H))
    player_pand.print(window)
    # Изменение положения шарика. К текущему положению прибавляется скорость по двум осям
    pygame.draw.rect(window,(210,40,0), (bot_rect_x,bot_rect_y, rect_W, rect_H))
    game_ball.print(window)
    # Проверка столкновений со стенками и отскок от них
    

    #Проверка столкновения шарика с ракетками игрока и бота
    if (game_ball.x-game_ball.radius <= rect_W):
        if game_ball.y >= player_pand.y and game_ball.y <= player_pand.y+player_pand.heitht:
            game_ball.speed_x*=-1
            game_ball.speed_x=int(game_ball.speed_x * 1.15)
            jump_sound.play()
    if (game_ball.x + ball_R >= win_W- rect_W):
        if game_ball.y >= bot_rect_y and game_ball.y <= bot_rect_y+rect_H:
            game_ball.speed_x*=-1
            game_ball.speed_x=int(game_ball.speed_x * 1.15)
            jump_sound.play()

    #Проверка забития голов
    if game_ball.x + game_ball.radius >= win_W or game_ball.x - game_ball.radius <= 0:
        if game_ball.x + game_ball.radius >= win_W:
            jump_sound.play()
        if game_ball.x - game_ball.radius <= 0:
            player_score += 1
 
        game_ball.spawn(int(win_W/2), int(win_H/2))

    #Отскок шарика от вертикальных и горизонтальных границ       
    if game_ball.y + game_ball.radius >= win_H or game_ball.y - game_ball.radius <= 0:
        game_ball.speed_y*= -1
        jump_sound.play()
    
    
    # Обновление окна приложения. Выполняется в конце цикла
    pygame.display.update()
    

    