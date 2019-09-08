#------------------------------------------------------
# Program: Tetris Game
# Author: Ron Hanji
# Date: 6/18/2018
# Description: A game of Tetris
#------------------------------------------------------
import pygame
import random
from os import path,remove
import Key_Module

pygame.init()
pygame.mixer.init()
pieces_dir = path.join(path.dirname(__file__), 'Tetris Pieces')
buttons_dir = path.join(path.dirname(__file__), 'Buttons')
Keys_dir = path.join(path.dirname(__file__),'Keyboard_Keys')
Pic_dir = path.join(path.dirname(__file__),'Pictures')
snd_dir = path.join(path.dirname(__file__),'Sounds')
f = open('Highscores.txt', 'r+')

LEFT_offset = 5
RIGHT_offset = 7
scale = 20

WIDTH = 240+(LEFT_offset+RIGHT_offset-1)*scale
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PINK = (255,0,255)
LIGHT_BLUE = (0,255,255)
ORANGE = (255,165,0)
LIGHT_PINK = (255,204,229)
NAVY = (0,0,128)
DARK_NAVY = (0,0,50)
###----MAKE SURE TO DOWNLOAD THIS FONT FROM THE FONTS FOLDER----###
font = pygame.font.match_font("KenVector Future Regular")
###-------------------------------------------------------------###


font_2 = pygame.font.match_font('arial')
# Load in Sounds
Theme_Song = pygame.mixer.Sound(path.join(snd_dir,'Theme Song.wav'))
click_sound = pygame.mixer.Sound(path.join(snd_dir,'click1.ogg'))

# Load in images
Blue = pygame.image.load(path.join(pieces_dir, "blue.png")).convert()
Red = pygame.image.load(path.join(pieces_dir, "red2.png")).convert()
Green = pygame.image.load(path.join(pieces_dir, "green.png")).convert()
Orange = pygame.image.load(path.join(pieces_dir, "orange.png")).convert()
Gray = pygame.image.load(path.join(pieces_dir, "gray.png")).convert()
Purple = pygame.image.load(path.join(pieces_dir, "purple.png")).convert()
White = pygame.image.load(path.join(pieces_dir, "white.png")).convert()
Pink = pygame.image.load(path.join(pieces_dir, "pink.png")).convert()


Blue_Button = pygame.image.load(path.join(buttons_dir, "Blue_Button.png")).convert()
Yellow_Button = pygame.image.load(path.join(buttons_dir, "Yellow_Button.png")).convert()

Start_Btn_Y = pygame.transform.scale(Yellow_Button, (scale*7,scale*2))
Start_Btn_B = pygame.transform.scale(Blue_Button, (scale*7,scale*2))

Inst_Btn_Y = pygame.transform.scale(Yellow_Button, (scale*15,scale*2))
Inst_Btn_B = pygame.transform.scale(Blue_Button, (scale*15,scale*2))

Score_Btn_Y = pygame.transform.scale(Yellow_Button, (scale*14,scale*2))
Score_Btn_B = pygame.transform.scale(Blue_Button, (scale*14,scale*2))

Exit_Btn_Y = pygame.transform.scale(Yellow_Button, (scale*5,scale*2))
Exit_Btn_B = pygame.transform.scale(Blue_Button, (scale*5,scale*2))

Again_Btn_Y = pygame.transform.scale(Yellow_Button, (scale*12,scale*2))
Again_Btn_B = pygame.transform.scale(Blue_Button, (scale*12,scale*2))



Red_Arrow = pygame.image.load(path.join(buttons_dir, "Red_Arrow.png")).convert()
Red_Arrow.set_colorkey(BLACK)
Red_Arrow = pygame.transform.scale(Red_Arrow,(scale*2,scale*2))

Yellow_Arrow = pygame.image.load(path.join(buttons_dir, "Yellow_Arrow.png")).convert()
Yellow_Arrow.set_colorkey(BLACK)
Yellow_Arrow = pygame.transform.scale(Yellow_Arrow,(scale*2,scale*2))

Grey_Arrow = pygame.image.load(path.join(buttons_dir, "Grey_Arrow.png")).convert()
Grey_Arrow.set_colorkey(BLACK)
Grey_Arrow = pygame.transform.scale(Grey_Arrow,(scale*2,scale*2))

Green_Arrow = pygame.image.load(path.join(buttons_dir, "Green_Arrow.png")).convert()
Green_Arrow.set_colorkey(BLACK)
Green_Arrow = pygame.transform.scale(Green_Arrow,(scale*2,scale*2))


Right_Arrow = pygame.image.load(path.join(Keys_dir, "Right_Arrow.png")).convert()
Right_Arrow.set_colorkey(BLACK)
Right_Arrow = pygame.transform.scale(Right_Arrow,(scale*2,scale*2))

Left_Arrow = pygame.image.load(path.join(Keys_dir, "Left_Arrow.png")).convert()
Left_Arrow.set_colorkey(BLACK)
Left_Arrow = pygame.transform.scale(Left_Arrow,(scale*2,scale*2))

Down_Arrow = pygame.image.load(path.join(Keys_dir, "Down_Arrow.png")).convert()
Down_Arrow.set_colorkey(BLACK)
Down_Arrow = pygame.transform.scale(Down_Arrow,(scale*2,scale*2))

Enter_Key = pygame.image.load(path.join(Keys_dir, "Enter_Key.png")).convert()
Enter_Key = pygame.transform.scale(Enter_Key,(scale*6,scale*4))
Enter_Key.set_colorkey(BLACK)

Space_Key = pygame.image.load(path.join(Keys_dir, "Space_Key.png")).convert()
Space_Key = pygame.transform.scale(Space_Key,(scale*6,scale*4))
Space_Key.set_colorkey(BLACK)

P_Key = pygame.image.load(path.join(Keys_dir, "P_Key.png")).convert()
P_Key = pygame.transform.scale(P_Key,(scale*2,scale*2))
P_Key.set_colorkey(BLACK)

Esc_Key = pygame.image.load(path.join(Keys_dir, "Escape_Key.png")).convert()
Esc_Key = pygame.transform.scale(Esc_Key,(scale*2,scale*2))
Esc_Key.set_colorkey(BLACK)

Piece_Dropping = pygame.image.load(path.join(Pic_dir, "Piece_Dropping.png")).convert()
Piece_Dropping = pygame.transform.scale(Piece_Dropping,(scale*9,scale*12))

Shapes = [Blue,Red,Green,Orange,Gray,Purple,White,Pink]
Shapes = list(map(lambda x: pygame.transform.scale(x,(scale,scale)), Shapes))
##-----------SHAPES----------##
matrix_T = [
    [1,1,1],
    [0,1,0],
    [0,0,0]
]
matrix_Z = [
    [2,2,0],
    [0,2,2],
    [0,0,0]
]
matrix_S = [
    [0,3,3],
    [3,3,0],
    [0,0,0]
]
matrix_L = [
    [0,4,0],
    [0,4,0],
    [0,4,4]
]
matrix_J = [
    [0,5,0],
    [0,5,0],
    [5,5,0]
]
matrix_O = [
    [6,6],
    [6,6]
]
matrix_I = [
    [0,7,0],
    [0,7,0],
    [0,7,0],
    [0,7,0]
]
matrix_P = [
    [8,8,0],
    [8,8,0],
    [8,0,0]
    ]
##----------------------------##

Shape_List = [matrix_T,matrix_Z,matrix_S,matrix_L,matrix_O,matrix_J,matrix_I,matrix_P]

# A player class
class Player():
    def __init__(self):
        self.x = 9
        self.y = 0
        self.shape = random.choice(Shape_List)
        self.speed = 1
        self.nextShape = random.choice(Shape_List)

    def reset(self):
        global ns_counter
        ns_counter = 0
        self.x = 9
        self.y = 0
        self.shape = self.nextShape
        self.speed = 1
        self.nextShape = random.choice(Shape_List)

    def update(self):  
        self.y += self.speed
        if collide(game_arena, player):
            player.y -= 1
            merge(game_arena,player)
            ns_counter = 0
            self.reset()

# a class for the back pieces
class Back():
    def __init__(self):
        self.y = None
        self.x = None
        self.shape = None
        self.speedx = 0
        self.speedy = 0
        
    def set_up(self):
        self.shape = random.choice(Shape_List)
        pos = random.randrange(4)
        speed = random.randrange(6,10)
        if pos == 0:
            self.y = 0
            self.x = random.randrange(0,WIDTH//scale-len(self.shape[0]))
            self.speedx = 0
            self.speedy = 1/FPS*speed
        elif pos == 1:
            self.y = HEIGHT//scale
            self.x = random.randrange(0,WIDTH//scale-len(self.shape[0]))
            self.speedx = 0
            self.speedy = -1/FPS*speed
        elif pos == 2:
            self.y = random.randrange(0,HEIGHT//scale-len(self.shape))
            self.x = 0
            self.speedx = 1/FPS*speed
            self.speedy = 0
        else:
            self.y = random.randrange(0,HEIGHT//scale-len(self.shape))
            self.x = WIDTH//scale
            self.speedx = -1/FPS*speed
            self.speedy = 0

    def update(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x < 0 or self.x > WIDTH//scale or self.y < 0 or self.y > HEIGHT//scale:
            self.set_up()

# a function to make images transparent. used for the back pieces go it from:
# https://nerdparadise.com/programming/pygameblitopacity
def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

# a funciton to create a 2 dimensional list with a given width and height
def createMatrix(w,h):
    matrix = []
    l=[]
    for i in range(h):
        for f in range(w):
            l.append(0)
        matrix.append(l)
        l=[]
    return matrix
# a fuction to draw a shape based on its numerical value. w is an argument
# of wether or not it is a back piece
def draw_shape(matrix,x,y,w=False):
    for row in matrix:
        c=0
        for i in row:
            if i != 0:
                if w:
                    blit_alpha(screen,Shapes[i-1],((x+c)*scale,y*scale), 50)
                    pygame.draw.rect(screen,BLACK,((x+c)*scale,y*scale,scale,scale),1)
                else:
                    screen.blit(Shapes[i-1],((x+c)*scale,y*scale))
                    pygame.draw.rect(screen,BLACK,((x+c)*scale,y*scale,scale,scale),1)
            c+=1
        y+=1

# a function to draw text
def draw_text(surf, text, size, x, y, font, color=WHITE):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x,y)
    surf.blit(text_surface, text_rect)

# a function to merge the player's matrix with the game arena
def merge(arena,player):
    for y,row in enumerate(player.shape):
        for x,piece in enumerate(row):
            if piece != 0:
                arena[y+player.y][x+player.x] = piece
# a function to check for collision
def collide(arena, player):
    for y in range(len(player.shape)):
        for x in range(len(player.shape[y])):
            try:
                if (player.shape[y][x] != 0 and arena[y + player.y][x + player.x] != 0) or (player.shape[y][x] != 0 and (player.x+x > WIDTH//scale-RIGHT_offset-1 or player.x+x < LEFT_offset)):
                    return True
                    
            except:
                return True
    return False
# a function that draws the border of the game screen, as well as the next shape,
# the score, and the saved shape
def draw():
    screen.fill(DARK_NAVY)
    for piece in back_pieces:
        draw_shape(piece.shape,piece.x,piece.y,True)
    pygame.draw.line(screen,RED,(LEFT_offset*scale,0),(LEFT_offset*scale,HEIGHT))
    pygame.draw.line(screen,RED,(WIDTH - RIGHT_offset*scale,0),(WIDTH - RIGHT_offset*scale,HEIGHT))
    
    draw_shape(player.shape,player.x,player.y)

    # changing box
    pygame.draw.rect(screen,BLUE,(WIDTH-RIGHT_offset*20+20,20,100,len(player.nextShape)*20+40),2)
    draw_shape(player.nextShape,WIDTH//scale-RIGHT_offset+2, 2)
    draw_shape(Saved,scale//20,scale//5)
    draw_shape(game_arena,0,0)
    draw_text(screen, 'score: {}'.format(score), 14, scale/4, scale/2,font)
    if player.speed == 0:
        pygame.draw.rect(screen,ORANGE,(WIDTH//2-scale*2,HEIGHT//2-scale,scale*3,scale*3))
        pygame.draw.rect(screen,WHITE,(WIDTH//2-(scale*2-scale*3/5),HEIGHT//2-(scale*3/4),scale*3/5,scale*3*(5/6)))
        pygame.draw.rect(screen,WHITE,(WIDTH//2-(scale*2-scale*3/5)+2*(scale*3/5),HEIGHT//2-(scale*3/4),scale*3/5,scale*3*(5/6)))
# a function to move the pieces down
def Drop():
    global timer
    player.y+=1
    timer = 0
    if collide(game_arena,player):
        player.y-=1
        merge(game_arena,player)
        player.reset()

# a function to rotate the pieces' matrix
def rotate(array,degree):
    for x in range(degree):
        new_array = []
        sorted_array = []
        for i in range(len(array[0])):
            for m in range(len(array)-1,-1,-1):
                sorted_array.append(array[m][i])
            new_array.append(sorted_array)
            sorted_array = []
        array = new_array
    return new_array

#a function ot move the pieces right or left
def Move(direction):
    player.x+=direction
    if collide(game_arena, player):
        player.x-=direction
        
#a function that rotates the pieces and checks for collision     
def Rotate(matrix, direction):
    x = player.x
    player.shape = rotate(matrix,direction)
    offset = 1
    c = 1
    #FIX THIS COLLISION
    while collide(game_arena,player):
        player.x += offset
        offset = (abs(offset)+1) *((-1)**c)
        c += 1
        if abs(offset) > 4:
            player.shape = rotate(player.shape, 3)
            player.x = x
            break

#a function to remove a filled line
def lineRemove(arena,L_o,R_o):
    global score
    for row in range(len(arena)):
        if list(filter(lambda x: x != 0, arena[row][L_o:R_o*-1])) == arena[row][L_o:R_o*-1]:
            if row % 2 == 0:
                f = 0
                inc = 1
            else:
                f = -1
                inc = -1
            while True:
                clock.tick(FPS)
                arena[row][f] = 0
                f+=inc
                if f == len(arena[row]) or f == -len(arena[row]):
                    break
                draw()
                pygame.display.flip()

            arena.pop(row)
            arena.insert(0,[0 for x in range(len(arena[0]))])
            score+=len(arena[row][L_o:R_o*-1])

# a function that creates a button given a rectangle
def button(button,font_size,write=True):
    screen.blit(button[4],(button[0],button[1]))
    if write:
        draw_text(screen,button[6],font_size,button[0]+scale/4,button[1],font)
    mp = pygame.mouse.get_pos()
    if button[0]<=mp[0]<=button[0]+button[2] and button[1]<=mp[1]<=button[1]+button[3]:
        screen.blit(button[5],(button[0],button[1]))
        if write:
            draw_text(screen,button[6],font_size,button[0]+scale/4,button[1],font)
            
# a function to check for a click
def is_clicked(item):
    mp = pygame.mouse.get_pos()
    if item[0]<=mp[0]<=item[0]+item[2] and item[1]<=mp[1]<=item[1]+item[3] and pygame.mouse.get_pressed()[0]:
        click_sound.play()
        return True
    return False

# a function that draws the background of the game over screen
def Background(arena):
    for i in range(5): 
        y = random.randrange(0,HEIGHT//scale)
        x = random.randrange(0,WIDTH//scale)
        p = random.randrange(0,len(Shape_List))
        arena[y][x] = p
# a function that draws the death animation
def Death_Animation(arena):
    player.shape = createMatrix(3,3)
    run = True
    while run:
        clock.tick(FPS)
        for col in range(HEIGHT//scale-1,0,-1):
            clock.tick(30)
            for i in range(col,HEIGHT//scale-1):
                clock.tick(30)
                arena[i+1] = arena[i]
                arena[i] = [0 for x in range(len(arena[0]))]
                draw()
                pygame.display.flip()

            arena.pop(-1)
            arena.insert(0,[0 for x in range(len(arena[0]))])
            if arena == createMatrix(WIDTH//20,HEIGHT//20):
                run = False
                break
# the main screen
def Main_Screen():
    Start = [8*scale,4*scale,7*scale,2*scale,Start_Btn_B,Start_Btn_Y,'Start']
    Instructions = [4*scale,7*scale,15*scale,2*scale,Inst_Btn_B,Inst_Btn_Y,'Instructions']
    Scores = [4.5*scale,10*scale,14*scale,2*scale,Score_Btn_B,Score_Btn_Y,'High Scores']
    Quit = [9*scale,13*scale,5*scale,2*scale,Exit_Btn_B,Exit_Btn_Y,'Exit']
    
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'

        if is_clicked(Start):
            return 'play'
        elif is_clicked(Instructions):
            return 'controls'
        elif is_clicked(Quit):
            return 'quit'
        elif is_clicked(Scores):
            return 'scores'
        
        screen.fill(NAVY)
        draw_text(screen, 'TETRIS',45,WIDTH/2-scale*5, scale,font)
        button(Start,32)
        button(Instructions,32)
        button(Scores,33)
        button(Quit,33)
        
        pygame.display.flip()

# the game over screen
def GameOver_Screen():
    global game_arena
    global score
    global Saved
    global drop_rate
    global old_score
    
    score = 0
    PlayAgain = [6*scale,11*scale,scale*12,scale*2,Again_Btn_B,Again_Btn_Y,'Play Again']
    Scores = [5*scale,14*scale,scale*14,scale*2,Score_Btn_B,Score_Btn_Y,'High Scores']
    Quit = [9*scale,17*scale,5*scale,2*scale,Exit_Btn_B,Exit_Btn_Y,'Exit']
    
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
        if is_clicked(PlayAgain):
            player.reset()
            Saved = createMatrix(3,3)
            drop_rate = 0
            old_score = 0
            return 'play'
        if is_clicked(Scores):
            return 'scores'
        if is_clicked(Quit):
            return 'quit'

        screen.fill(NAVY)
        Background(grid)
        draw_shape(grid,0,0)
        draw_text(screen, 'Game Over',56,WIDTH//2-scale*10, HEIGHT//4,font,WHITE)
        button(PlayAgain,32)
        button(Quit,32)
        button(Scores,33)
        
        pygame.display.flip()

# the controls screen        
def Controls():
    Start = [0,scale*18,scale*2,scale*2,Red_Arrow,Yellow_Arrow]
    Goals = [scale*21,scale*18,scale*2,scale*2,Green_Arrow,Grey_Arrow]
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                mp = pygame.mouse.get_pos()
                if Start[0]<=mp[0]<=Start[0]+Start[2] and Start[1]<=mp[1]<=Start[1]+Start[3]:
                    click_sound.play()
                    return 'start'
        screen.fill(NAVY)

        draw_text(screen, 'Controls',56, 2*scale,0,font)
        
        screen.blit(Left_Arrow,(scale*2,scale*4))
        screen.blit(Down_Arrow,(scale*4,scale*4))
        screen.blit(Right_Arrow,(scale*6,scale*4))
        draw_text(screen, 'Arrows to move',24,scale*9,scale*4,font)
        
        screen.blit(Space_Key,(scale*2,scale*6))
        draw_text(screen, 'Space to rotate',24,scale*9,scale*7,font)
        
        screen.blit(Enter_Key,(scale*2, scale*10))
        draw_text(screen, 'Enter to hold',24,scale*9,scale*10,font)
        draw_text(screen, 'shape/ use held',24,scale*9,scale*11,font)
        draw_text(screen, 'shape',24,scale*9,scale*12,font)
        
        screen.blit(P_Key, (scale*2,scale*15))
        screen.blit(Esc_Key, (scale*6,scale*15))
        draw_text(screen, 'P or Esc to pause',22,scale*9,scale*15,font)
        
        draw_text(screen,'GOALS',24,scale*16,scale*18,font)
        
        draw_text(screen,'MAIN',24,scale*2.1,scale*18-scale/3,font)
        draw_text(screen,'MENU',24,scale*2.1,scale*19-scale/3,font)

        button(Start,12,False)
        button(Goals,12,False)

        if is_clicked(Goals):
            return 'goals'
        pygame.display.flip()

# the goals screen
def goals():
    controls = [0,scale*18,scale*2,scale*2,Red_Arrow,Yellow_Arrow]
    Start = [scale*21,scale*18,scale*2,scale*2,Green_Arrow,Grey_Arrow]
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                mp = pygame.mouse.get_pos()
                if Start[0]<=mp[0]<=Start[0]+Start[2] and Start[1]<=mp[1]<=Start[1]+Start[3]:
                    click_sound.play()
                    return 'start'

        screen.fill(NAVY)
        draw_text(screen, 'GOALS',56, 6*scale,0,font)
        draw_text(screen, 'Complete rows',20,scale,scale*3,font)
        draw_text(screen, 'to get points',20,scale,scale*4,font)
        draw_text(screen, "Don't let" ,20,scale*14,scale*3,font)
        draw_text(screen, 'them stacK',20,scale*14,scale*4,font)
        draw_text(screen, 'too high',20,scale*14,scale*5,font)
        draw_text(screen,'CONTROLS',24,scale*2.1,scale*18,font)
        draw_text(screen,'MAIN',24,scale*16.8,scale*18-scale/3,font)
        draw_text(screen,'MENU',24,scale*16.8,scale*19-scale/3,font)
        button(Start,12,False)
        button(controls,12,False)
        if is_clicked(controls):
            return 'controls'
        pygame.display.flip()
   
# the main game screen
def Game(score_list):
    global timer
    global score
    global Saved
    global ns_counter
    global grid
    global FPS
    global drop_rate
    global old_score
    global f
    delay = 0
    paused = False
    drop_rate = 0
    timer = 0
    score = 0
    running = True
    Saved = createMatrix(3,3)
    d = True
    grid = createMatrix(WIDTH//scale,HEIGHT//scale)
    old_score = 0
    player.reset()
    while True:
        clock.tick(FPS)
        timer +=1
        if timer == FPS-drop_rate:
            player.update()
            timer = 0
        keys = pygame.key.get_pressed()
        if not paused:
            if keys[pygame.K_DOWN]:
                delay+=1
                if delay == 6:
                    Drop()
                    delay = 0
            if keys[pygame.K_LEFT]:
                delay+=1
                if delay==6:
                    Move(-1)
                    delay=0
            if keys[pygame.K_RIGHT]:
                delay+=1
                if delay==6:
                    Move(1)
                    delay=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not paused:
                    s = player.shape
                    ns_counter += 1
                    if ns_counter < 3:
                        if d:
                            player.shape = player.nextShape
                            player.nextShape = random.choice(Shape_List)
                            d = False
                        else:
                            player.shape = Saved
                        Saved = s
                        player.y = 0
                        player.x = 9
                if event.key == pygame.K_SPACE and not paused:
                   Rotate(player.shape, 1)
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    if player.speed != 0:
                        paused = True
                        player.speed = 0
                    else:
                        paused = False
                        timer = FPS-1
                        player.speed = 1
        lineRemove(game_arena,LEFT_offset,RIGHT_offset)
        if score % 11 == 0 and score != 0 and score != old_score:
            if drop_rate < 57:
                drop_rate += 3
            old_score = score
            
        for piece in back_pieces:
            piece.update()

        if player.y <= 0 and collide(game_arena,player):
            merge(game_arena,player)
            Death_Animation(game_arena)
            for s in range(len(score_list)):
                if score >= int(score_list[s][1]):
                    score_list.insert(s,[Key_Module.ask(screen),str(score)])
                    score_list.pop()
                    f.close()
                    remove('Highscores.txt')
                    break
            f = open('Highscores.txt','w+')
            for v in score_list:
                f.write('{}-{}\n'.format(v[0],v[1]))
            return 'game_over'
        
        draw()
        pygame.display.flip()

# the highscores screen
def HighScores(scoreList):
    main = [0,scale*18,scale*2,scale*2,Red_Arrow,Yellow_Arrow]
    while True:
        screen.fill(NAVY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'

        if is_clicked(main):
            return 'start'
        
        for i in range(len(scoreList)):
            draw_text(screen,'{}'.format(scoreList[i][0]),30,scale*2,scale*3*i+scale,font_2)
            draw_text(screen,'{}'.format(scoreList[i][1]),30,scale*18,scale*3*i+scale,font)
        draw_text(screen,'MAIN',24,scale*2.1,scale*18-scale/3,font)
        draw_text(screen,'MENU',24,scale*2.1,scale*19-scale/3,font)
        button(main,12,False)
        pygame.display.flip()

 # sort the scores from a file and add them to a list       
score_list = []
for i in range(5):
    x = f.readline().strip('\n').split('-')
    if x != ['']:
        score_list.append(x)
score_list = sorted(score_list,key=lambda x: int(x[-1]),reverse=True)

# initate the back pieces
back_pieces = []
for i in range(6):
    back_pieces.append(Back())
    back_pieces[i].set_up()

# initiate the song as well as the arena
Theme_Song.set_volume(0.1)
game_arena = createMatrix(WIDTH//scale,HEIGHT//scale)
player = Player()
response = 'start'
InPlay = True

# main game loop
while InPlay:
    if response == 'quit':
        InPlay = False
    elif response == 'start':
        response = Main_Screen()
    elif response == 'play':
        Theme_Song.play(-1)
        response =  Game(score_list)
        Theme_Song.fadeout(2000)
    elif response == 'controls':
        response = Controls()
    elif response == 'goals':
        response = goals()
    elif response == 'scores':
        response = HighScores(score_list)
    elif response == 'game_over':
        response = GameOver_Screen()
f.close()
pygame.quit()
