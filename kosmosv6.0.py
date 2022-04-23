# -*- coding: utf-8 -*-
import sys, pygame, random, os, math
pygame.init()
pygame.mixer.init()
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("window.ui")[0]

class MyWindowClass(QtGui.QMainWindow, QtGui.QWidget, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        chislo_Vse_Game_Name = len(Vse_Game_Name[0])
        for i in range(chislo_Vse_Game_Name):
            button_Vse_Game_Name = QtGui.QPushButton(str(Vse_Game_Name[0][i]), self)
            button_Vse_Game_Name.setGeometry(100, (270+i*50), 100, 35)
            massiv_button_Vse_Game_Name.append(button_Vse_Game_Name)

            delete_Vse_Game_Name = QtGui.QPushButton(str(Vse_Game_Name[0][i]), self)
            delete_Vse_Game_Name.setGeometry(450, (270+i*50), 100, 35)
            delete_Vse_Game_Name.setStyleSheet("background: red")
            massiv_delete_Vse_Game_Name.append(delete_Vse_Game_Name)
        for i in range(chislo_Vse_Game_Name):
            label = QtGui.QLabel("Money " + str(Vse_Game_Name[3][i]), self)
            label.move(220, (270+i*50))
            label.setFixedSize(150, 30)
            massiv_label.append(label)
        for i in range(len(Vse_Game_Name[0])):
            massiv_button_Vse_Game_Name[i].clicked.connect(self.button_clicked1)
            massiv_delete_Vse_Game_Name[i].clicked.connect(self.button_clicked2)
            massiv_delete_Vse_Game_Name[i].clicked.connect(massiv_button_Vse_Game_Name[i].deleteLater)
            massiv_delete_Vse_Game_Name[i].clicked.connect(massiv_delete_Vse_Game_Name[i].deleteLater)
            massiv_delete_Vse_Game_Name[i].clicked.connect(massiv_label[i].deleteLater)
        self.game.clicked.connect(self.button_clicked0)
        if len(Vse_Game_Name[0]) < 4:
            hight_QWidget = 480
        else:
            hight_QWidget = (300+len(Vse_Game_Name[0])*50)
        QtGui.QWidget.setFixedSize(self, 640, hight_QWidget)
    def button_clicked0(self):
        global Game_Name
        if self.name.text() == "":
            Game_Name = "ANONIM"
        else:
            Game_Name = self.name.text()
        if Game_Name not in Vse_Game_Name[0]:
            Vse_Game_Name[0].append(str(Game_Name))
            Vse_Game_Name[1].append('10000')
            Vse_Game_Name[2].append('0')
            Vse_Game_Name[3].append('1000')
        f = open('Vse_Game_Name.txt', 'w')
        f.write(str(Vse_Game_Name) + '\n')
        f.close()
        myQExampleScrollArea.close()
        
    def button_clicked1(self):
        sender = self.sender()
        global Game_Name
        Game_Name = sender.text()
        myQExampleScrollArea.close()
        
    def button_clicked2(self):
        sender = self.sender()
        i = sender.text()
        index =  Vse_Game_Name[0].index(str(i))
        del Vse_Game_Name[1][index]
        del Vse_Game_Name[2][index]
        del Vse_Game_Name[3][index]
        Vse_Game_Name[0].remove(i)
        

        f = open('Vse_Game_Name.txt', 'w')
        f.write(str(Vse_Game_Name) + '\n')
        f.close()
        
class QExampleScrollArea (QtGui.QScrollArea, QtGui.QWidget ):
    def __init__ (self, parentQWidget = None):
        super(QtGui.QScrollArea, self).__init__(parentQWidget)
        QtGui.QWidget.setFixedSize(self, 660, 480)
        self.myAnnotator = MyWindowClass(self)
        self.setWidget(self.myAnnotator)

    def mousePressEvent (self, eventQMouseEvent):
        QtGui.QScrollArea.mousePressEvent(self, eventQMouseEvent)
        self.myAnnotator.mousePressEvent(eventQMouseEvent)

    def mouseReleaseEvent (self, eventQMouseEvent):
        QtGui.QScrollArea.mouseReleaseEvent(self, eventQMouseEvent)
        self.myAnnotator.mouseReleaseEvent(eventQMouseEvent)

    def mouseMoveEvent (self, eventQMouseEvent):
        QtGui.QScrollArea.mouseMoveEvent(self, eventQMouseEvent)
        self.myAnnotator.mouseMoveEvent(eventQMouseEvent)

    def wheelEvent (self, eventQWheelEvent):
        self.myAnnotator.wheelEvent(eventQWheelEvent)
massiv_label = []
massiv_delete_Vse_Game_Name = []
massiv_button_Vse_Game_Name = []

Vse_Game_Name = []
f = open('Vse_Game_Name.txt', 'r')
Vse_Game_Name = (eval(f.readlines()[0]))

app = QtGui.QApplication(sys.argv)
myQExampleScrollArea = QExampleScrollArea()
myQExampleScrollArea.show()

app.exec_()
   
size = width, height = 1366, 700
screen = pygame.display.set_mode(size)

toplivo = 100

def knopki():
    global toplivo
    global a
    global b
    a = 0
    b = 0
    if toplivo > 0:
        global koeff
        c = None
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and keystate[pygame.K_RIGHT] == False:
            b = koeff
            c = 0
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_LEFT] == False:
            b = -koeff
            c = 0
        if keystate[pygame.K_UP] and keystate[pygame.K_DOWN] == False:
            a = koeff
            c = 0
        if keystate[pygame.K_DOWN] and keystate[pygame.K_UP] == False:
            a = -koeff
            c = 0
    
   
        if keystate[pygame.K_UP] and keystate[pygame.K_LEFT]:
            a = koeff*0.7
            b = koeff*0.7
            c = 1
        if keystate[pygame.K_UP] and keystate[pygame.K_RIGHT]:
            a = koeff*0.7
            b = -koeff*0.7
            c = 1
        if keystate[pygame.K_DOWN] and keystate[pygame.K_LEFT]:
            a = -koeff*0.7
            b = koeff*0.7
            c = 1
        if keystate[pygame.K_DOWN] and keystate[pygame.K_RIGHT]:
            a = -koeff*0.7
            b = -koeff*0.7
            c = 1
        
        if c == 0:
            toplivo = toplivo - (math.fabs(a)+math.fabs(b))/10
        if c == 1:
            toplivo = toplivo - (math.fabs(a)+math.fabs(b))/14
        
class MyPlatformaClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left = location[0]
        self.rect.top = location[1]
    def move(self):
        global raketa
        raketa =  pygame.draw.circle(screen, [0,60,240], [int(location[0])+25, int(location[1])+25], 1, 1)
        
stars_x = []
stars_y = []

for i in range(4000):
        x = random.randint(0, width)
        y = random.randint(0, height)
        stars_x.append(x)
        stars_y.append(y)
loc_CenterStars = [683, 350]
def CenterStars():
    knopki()
    loc_CenterStars[0] = loc_CenterStars[0] + b
    if loc_CenterStars[0] > 2*width:
        loc_CenterStars[0] = loc_CenterStars[0]  - 2*width
    if loc_CenterStars[0] < 0:
         loc_CenterStars[0] =  loc_CenterStars[0] + 2*width
    loc_CenterStars[1] = loc_CenterStars[1] + a
    if loc_CenterStars[1] < 0:
        loc_CenterStars[1] = loc_CenterStars[1] + 2*height
    if loc_CenterStars[1] > 2*height:
        loc_CenterStars[1] = loc_CenterStars[1] - 2*height
    pygame.draw.circle(screen, [0,60,240], [int(loc_CenterStars[0]), int(loc_CenterStars[1])], 1, 1)
def Stars():
    knopki()
    
    for i in range(4000):
        stars_x[i] = stars_x[i] + b
        if stars_x[i] > width:
            stars_x[i] = stars_x[i] - width
        if stars_x[i] < 0:
            stars_x[i] = stars_x[i] + width
        stars_y[i] = stars_y[i] + a
        if stars_y[i] < 0:
            stars_y[i] = stars_y[i] + height
        if stars_y[i] > height:
            stars_y[i] = stars_y[i] - height
        pygame.draw.circle(screen, [0,60,240], [int(stars_x[i]), int(stars_y[i])], 1, 1)
class ZemljaClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("planet\zemlja.png")
        self.rect = self.image.get_rect()
        knopki()
        self.rect.left = loc[0]
        self.rect.top = loc[1]

    def move(self):
        loc[0] = loc[0] + b
        if loc[0] > 2*width-100:
            loc[0] = loc[0]  - 2*width
        if loc[0] < 0-100:
            loc[0] =  loc[0] + 2*width
        loc[1] = loc[1] + a
        if loc[1] < 0-100:
            loc[1] = loc[1] + 2*height
        if loc[1] > 2*height-100:
            loc[1] = loc[1] - 2*height
        self.rect.left = loc[0]
        self.rect.top = loc[1]

mir_x = 0
mir_y = 0
def Mir():
    global mir_x
    global mir_y
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_KP4]:
        mir_x = mir_x - 0.1
    if keystate[pygame.K_KP6]:
        mir_x = mir_x + 0.1
    if keystate[pygame.K_KP8]:
        mir_y = mir_y + 0.1
    if keystate[pygame.K_KP2]:
        mir_y = mir_y - 0.1
planets_x = 0
planets_y = 0
group_planets = pygame.sprite.Group()
def Planets():
    knopki()
    random.seed(int(mir_x))
    random.seed( int(mir_y)* int(random.random()*2*width) )
    global x_p
    x_p = 2*width * random.random()
    blue = random.random()
    red = int(255 * random.random())
    
    random.seed(int(mir_y))
    random.seed( int(mir_x)* int(random.random()*2*height) )
    global y_p
    y_p = 2*height * random.random()
    green = int(255 * random.random())
    blue = int(255*blue*random.random())
    color = [red,green,blue]

    global planets_x
    global planets_y
    planets_x = planets_x + b
    planets_y = planets_y + a
    x_p = x_p + planets_x
    if x_p > 2*width-100:
        planets_x = planets_x  - 2*width
    if x_p < 0-100:
        planets_x = planets_x + 2*width
    y_p = y_p + planets_y
    if y_p < 0-100:
        planets_y = planets_y + 2*height
    if y_p > 2*height-100:
        planets_y = planets_y - 2*height
    pygame.draw.circle(screen, color, [int(x_p), int(y_p)], 50, 0)
def Vvod():
    global kol
    kol = []
    def get_key():
        while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key
            else:
                pass

    def display_box(screen, message):
        fontobject = pygame.font.Font(None,18)
        pygame.draw.rect(screen, (0,0,0),
                        ((screen.get_width() / 2) - 100,
                        (screen.get_height() / 2) - 10,
                        200,20), 0)
        pygame.draw.rect(screen, (255,255,255),
                        ((screen.get_width() / 2) - 102,
                        (screen.get_height() / 2) - 12,
                        204,24), 1)
        if len(message) != 0:
            screen.blit(fontobject.render(message, 1, (255,255,255)),
                        ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
        pygame.display.flip()
    def ask(screen, question):
        pygame.font.init()
        global current_string
        current_string = []
        display_box(screen, question + ": " + string.join(current_string,""))
        while 1:
            inkey = get_key()
            if inkey == K_BACKSPACE:
                current_string = current_string[0:-1]
            elif inkey == K_RETURN:
                break
            elif inkey >= 48 and inkey <= 57:
                current_string.append(chr(inkey))
            display_box(screen, question + ": " + string.join(current_string,""))
        return string.join(current_string,"")

    if __name__ == '__main__': kol.append(ask(screen, "Scolko: "))
torg = 0
def Torgovlya():
    random.seed(int(mir_x))
    random.seed( int(mir_y)* int(random.random()*2*width) )
    tsena_tovar = int(1/random.random())

    random.seed(int(mir_y))
    random.seed( int(mir_x)* int(random.random()*2*height) )
    tsena_toplivo = int(1/random.random())

    global score_font
    if random.random() > 0.5:
        chislo = "Mne prodat "
    else:
        chislo = "Mne kupit "
    score_surf = score_font.render(chislo, 1, (223, 223, 223))
    screen.blit(score_surf, [10, 220])
    
    chislo = "Tsena tovara: " + str(tsena_tovar)
    score_surf = score_font.render(chislo, 1, (223, 223, 223))
    screen.blit(score_surf, [10, 250])

    chislo = "Tsena toplivo: " + str(tsena_toplivo)
    score_surf = score_font.render(chislo, 1, (223, 223, 223))
    screen.blit(score_surf, [10, 280])

    chislo = "Nazhmite 1 na klaviature sprava, chtoby"
    score_surf = score_font.render(chislo, 1, (223, 223, 223))
    screen.blit(score_surf, [10, 310])

    chislo = "vybrat pervyj tovar, ili 3, chtoby - vtoroj"
    score_surf = score_font.render(chislo, 1, (223, 223, 223))
    screen.blit(score_surf, [10, 340])
    global t
    if t != None:
        Vvod()
    global kol
    global money
    global tovar
    global toplivo
    if "kol" in globals() and kol == ['']:
        print kol
        kol = 0
    if random.random() > 0.5 and "kol" in globals():
        kol[0] = int(kol[0])
        kol[0] = -kol[0]
    if t == "tov" and type(kol) == list:
        
        tovar = tovar + int(kol[0])
        money = money - tsena_tovar*int(kol[0])
        if money < 0:
            tovar = tovar - int(kol[0])
            money = money + tsena_tovar*int(kol[0])
        
    if t == "top":
        toplivo = toplivo + int(kol[0])
        money = money - tsena_toplivo*int(kol[0])
        if money < 0:
            toplivo = toplivo - int(kol[0])
            money = money + tsena_toplivo*int(kol[0])
    t = None
def Back():
    pygame.draw.rect(screen, [223, 223, 223], [5, 35, 75, 35], 1)
    back_text = "Back"
    back_surf = score_font.render(back_text, 1, (223, 223, 223))
    screen.blit(back_surf, [10, 40])
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.pos[0] > 5 and event.pos[0] < 80:
            if event.pos[1] > 35 and event.pos[1] < 70:
                global restart
                global running
                restart = True
                running = False
                
size = width, height = 1366, 700
screen = pygame.display.set_mode(size)


pygame.mixer.music.load("music\\resurection.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(-1)
score = 0
if "Game_Name" in locals():
    index1 =  Vse_Game_Name[0].index(str(Game_Name))
    toplivo = int(Vse_Game_Name[1][index1])
    tovar = int(Vse_Game_Name[2][index1])
    money = int(Vse_Game_Name[3][index1])
    score_font = pygame.font.Font(None, 36)
    score_pos = [10, 10]
    score_pos_record = [400, 10]
loc = [633, 300]
massiv_zemlja = []
zemlja = ZemljaClass()
massiv_zemlja.append(zemlja)
img_file = "image\platforma.jpg"
balls = []
speed = [0, 0]
location = [658, 325]
platforma = MyPlatformaClass(img_file, location, speed)
balls.append(platforma)

myachi = pygame.sprite.Group()
myachi.add(platforma)

time = 0
koeff = 10
"""money = 1000
tovar = 0"""
t = None
clock = pygame.time.Clock()
paused = False
running = True
if "Game_Name" not in locals():
        running = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0, 0, 0])
    Stars()
    CenterStars()
    if time > 0.4:
        Mir()
        if int(mir_x) == 0 and int(mir_y) == 0:
            for i in massiv_zemlja:
                zemlja.move()
                screen.blit(zemlja.image, zemlja.rect)
        else:
            Planets()
            if ( (int(location[0])+25-(x_p))**2 + (int(location[1])+25-(y_p))**2)**0.5 < 62.5:
                chislo = "Nazhmite 7 na klaviature sprava, chtoby"
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [10, 160])

                chislo = "pristupit k torgovle, i 9, chtoby okonchit"
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [10, 190])

                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_KP7]:
                    torg = 1
                if keystate[pygame.K_KP9]:
                    torg = 0
                if torg == 1:
                    Torgovlya()
                    keystate = pygame.key.get_pressed()
                    if keystate[pygame.K_KP1]:
                        t = "tov"
                    if keystate[pygame.K_KP3]:
                        t = "top"
                    
        Back()
    
        chislo = "Mir: x "+ str(mir_x) + " y " + str(mir_y)
        score_surf = score_font.render(chislo, 1, (223, 223, 223))
        screen.blit(score_surf, score_pos_record)
    
        chislo = "Location: x " + str(loc_CenterStars[0]) + " y " + str(loc_CenterStars[1])
        score_surf = score_font.render(chislo, 1, (223, 223, 223))
        screen.blit(score_surf, score_pos)

        chislo = "Toplivo: " + str(toplivo)
        score_surf = score_font.render(chislo, 1, (223, 223, 223))
        screen.blit(score_surf, [10, 70])

        chislo = "Tovar: " + str(tovar)
        score_surf = score_font.render(chislo, 1, (223, 223, 223))
        screen.blit(score_surf, [10, 100])

        chislo = "Money: " + str(money)
        score_surf = score_font.render(chislo, 1, (223, 223, 223))
        screen.blit(score_surf, [10, 130])
        
        if toplivo > 0:
            end_time = 0
        if toplivo <= 0:
            chislo = "Toplivo konchilos :("
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [1000, 0])
            if end_time > 0.8:
                chislo = "No vy vsyo etchyo mozhete" 
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [1000, 30])
            if end_time > 1.6:
                chislo = "dvigatsya mezhdu mirami,"
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [1000, 60])
            if end_time > 2.4:
                chislo = "tak chto est veroztnost,"
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [1000, 90])
            if end_time > 3.2:
                chislo = "chto vy popadyote na planety,"
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [1000, 120])
            if end_time > 4:
                chislo = "gde smozhete kupit toplivo."
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [1000, 150])
            if end_time > 4.8:
                chislo = "Udachi!"
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [1000, 180])
            end_time = end_time + 0.02
        
        for ball in balls:
            platforma.move()
            screen.blit(ball.image, ball.rect)
    time = time + 0.02
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
index =  Vse_Game_Name[0].index(str(Game_Name))
Vse_Game_Name[1][index] = str(int(toplivo))
Vse_Game_Name[2][index] = str(int(tovar))
Vse_Game_Name[3][index] = str(int(money))
f = open('Vse_Game_Name.txt', 'w')
f.write(str(Vse_Game_Name) + '\n')
f.close()
if "restart" in locals():
    if restart == True:
        os.system("kosmosv6.0.py")
