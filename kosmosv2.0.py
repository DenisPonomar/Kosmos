# -*- coding: utf-8 -*-
import sys, pygame, random, os
pygame.init()
pygame.mixer.init()
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
            label = QtGui.QLabel("score: " + str(Vse_Game_Name[1][i]), self)
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
            Vse_Game_Name[1].append('0')
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
   

class MyPlatformaClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left = location[0]
        self.rect.top = location[1]
    def move(self):
        x = 1
def knopki():
    global a
    global b
    a = 0
    b = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT] and keystate[pygame.K_RIGHT] == False:
        b = koeff
    elif keystate[pygame.K_RIGHT] and keystate[pygame.K_LEFT] == False:
        b = -koeff
        
    if keystate[pygame.K_UP] and keystate[pygame.K_DOWN] == False:
        a = koeff
    elif keystate[pygame.K_DOWN] and keystate[pygame.K_UP] == False:
        a = -koeff

    if keystate[pygame.K_UP] and keystate[pygame.K_LEFT]:
        a = koeff*0.7
        b = koeff*0.7
    if keystate[pygame.K_UP] and keystate[pygame.K_RIGHT]:
        a = koeff*0.7
        b = -koeff*0.7
        
    if keystate[pygame.K_DOWN] and keystate[pygame.K_LEFT]:
        a = -koeff*0.7
        b = koeff*0.7
    if keystate[pygame.K_DOWN] and keystate[pygame.K_RIGHT]:
        a = -koeff*0.7
        b = -koeff*0.7
width = 1366
height = 700    
stars_x = []
stars_y = []

for i in range(4000):
        x = random.randint(0, width)
        y = random.randint(0, height)
        stars_x.append(x)
        stars_y.append(y)

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
        x = stars_x[i]
        y = stars_y[i]
        pygame.draw.circle(screen, [0,60,240], [int(x), int(y)], 1, 1)
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
        loc[1] = loc[1] + a
        self.rect.left = loc[0]
        self.rect.top = loc[1]
        
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
koeff = 1000
score = 0
if "Game_Name" in locals():
    index1 =  Vse_Game_Name[0].index(str(Game_Name))
    record = int(Vse_Game_Name[1][index1])
    score_font = pygame.font.Font(None, 36)
    score_pos = [10, 10]
    score_pos_record = [400, 10]
loc = [583, 250]
massiv_planets = []
zemlja = ZemljaClass()
massiv_planets.append(zemlja)
img_file = "image\platforma.jpg"
balls = []
speed = [0, 0]
location = [633, 300]
platforma = MyPlatformaClass(img_file, location, speed)
balls.append(platforma)

myachi = pygame.sprite.Group()
myachi.add(platforma)

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
    for i in massiv_planets:
        zemlja.move()
        screen.blit(zemlja.image, zemlja.rect)
    Back()
    
    if score == 0:
        """speedy[0] = speedy[0]/koeff
        speedy[1] = speedy[1]/koeff"""
        koeff = 10

    if record <= score and paused == False:
        record = record + (0.01)
    ochki_record = "Record: "+ str(int(record)) + str(loc)
    score_surf_record = score_font.render(ochki_record, 1, (223, 223, 223))
    screen.blit(score_surf_record, score_pos_record)
    
    if paused == False:
        score = score + (0.01)
    ochki = "Score: " + str(int(score))
    score_surf = score_font.render(ochki, 1, (223, 223, 223))
    screen.blit(score_surf, score_pos)
    for ball in balls:
        platforma.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
if "restart" in locals():
    if restart == True:
        os.system("kosmosv1.0.py")
