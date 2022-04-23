import sys, pygame, random, os, math
pygame.init()
pygame.mixer.init()
size = width, height = 1366, 700
screen = pygame.display.set_mode(size)

def knopki():
    global toplivo
    global a
    global b
    if toplivo > 0:
        global koeff
        c = None
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and keystate[pygame.K_RIGHT] == False:
            b = b + koeff
            c = 0
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_LEFT] == False:
            b = b - koeff
            c = 0
        if keystate[pygame.K_UP] and keystate[pygame.K_DOWN] == False:
            a = a + koeff
            c = 0
        if keystate[pygame.K_DOWN] and keystate[pygame.K_UP] == False:
            a = a - koeff
            c = 0
    
   
        if keystate[pygame.K_UP] and keystate[pygame.K_LEFT]:
            a = a + koeff*0.7
            b = b + koeff*0.7
            c = 1
        if keystate[pygame.K_UP] and keystate[pygame.K_RIGHT]:
            a = a + koeff*0.7
            b = b - koeff*0.7
            c = 1
        if keystate[pygame.K_DOWN] and keystate[pygame.K_LEFT]:
            a = a - koeff*0.7
            b = b + koeff*0.7
            c = 1
        if keystate[pygame.K_DOWN] and keystate[pygame.K_RIGHT]:
            a = a - koeff*0.7
            b = b - koeff*0.7
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

def pirat():
    knopki()
    loc[0] = loc[0] + b
    loc[1] = loc[1] + a
    pygame.draw.circle(screen, [191, 191, 191], [int((loc[0]+50)), int((loc[1]+50))], 25, 0)
    pygame.draw.circle(screen, [127,31,31], [int((loc[0]+50)), int((loc[1]+50))], 12, 0)
    global razgovor
    global pirat_time
    if razgovor == 1:
        x_razg = 733
        chislo = "Zdravstvuj, putnik! Ja znaju, zachem ty prishyol."
        score_surf = score_font.render(chislo, 1, (223, 223, 223))
        screen.blit(score_surf, [x_razg, 0])
        if pirat_time > 2:
            chislo = "Ty prishyol za beskonechnoj Vselennoj. Ty v nej!" 
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 30])
        if pirat_time > 4:
            chislo = "Izvini, ne predstavilsya, Ja stalker Pirat."
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 60])
        if pirat_time > 6:
            chislo = "Ja tut stolknulsya s mestnym pravitelstvom,"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 90])
        if pirat_time > 8:
            chislo = "posle chego menya navechno zaperli zdes. U tebya"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 120])
        if pirat_time > 10:
            chislo = "mnogo voprosov. Ja otvechu na vse. Pochemu tam" 
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 150])
        if pirat_time > 12:
            chislo = "gde tsena 42, tam portal? Takuju tsenu naznachil"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 180])
        if pirat_time > 14:
            chislo = "prezident torgovoj federatsii, kak nopominanie,"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 210])
        if pirat_time > 16:
            chislo = "chto imenno stolko raz mestnoe pravitelsvo"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 240])
        if pirat_time > 18:
            chislo = "proigralo v vojnah s torgovoy federatsiej."
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 270])
        if pirat_time > 20:
            chislo = "No nastojatshya beskonechnaja Vselennaja " 
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 300])
        if pirat_time > 22:
            chislo = "ohranyatsa mestnym pravitelstvom. On, bukvalno"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 330])
        if pirat_time > 24:
            chislo = "nahoditsya vnutri ih planety. Oni dadut tebe"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 360])
        if pirat_time > 26:
            chislo = "spidometr i vosmozhnost vernutsya tuda, otkuda"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 390])
        if pirat_time > 28:
            chislo = "prishyol, i vsyo... Da, ty zdes uskoryaeshsya i" 
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 420])
        if pirat_time > 30:
            chislo = "zamedlyaeshsya, potomu chto zdes nastoyatshi"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 450])
        if pirat_time > 32:
            chislo = "vakuum, a ne zhidkij, kak v vashih mirah. Esli"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 480])
        if pirat_time > 34:
            chislo = "ty chitaesh etu zapis, znachi ja davno uzhe umer."
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 510])
        if pirat_time > 36:
            chislo = "Parapampam! Sledi za toplivom, druzhitshe! Poka!"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 540])
        if pirat_time > 42:
            razgovor = 0
            pirat_time = 0

def Changa():
    loc[0] = loc[0] + b
    loc[1] = loc[1] + a
    pygame.draw.circle(screen, [0,255,0], [int((loc[0]-933)), int((loc[1]+50))], 325, 1)
    pygame.draw.circle(screen, [255,0,0], [int((loc[0]-933)), int((loc[1]+50))], 150, 1)
    pygame.draw.circle(screen, [0,0,200], [int((loc[0]-933)), int((loc[1]+50))], 125, 0)
    pygame.draw.circle(screen, [0, 60, 240], [int((loc[0]-933)), int((loc[1]+50))], 100, 0)
    global changa_time
    global running
    global raz
    x_razg = 10
    rasst = ( (int(location[0])+25-(loc[0]-933))**2 + (int(location[1])+25-(loc[1]+50))**2)**0.5
    if rasst < 500:
        chislo = "Ne priblizhaytes k krasnoj linii! Inache Vy budete"
        score_surf = score_font.render(chislo, 1, (223, 63, 63))
        screen.blit(score_surf, [x_razg, 160])
        
        chislo = "unichtozheny. Podletite za zelyonuju liniyu" 
        score_surf = score_font.render(chislo, 1, (223, 63, 63))
        screen.blit(score_surf, [x_razg, 190])

    if rasst < 325 and raz == 1:
        chislo = "Zdravstvuj, putnik! Vas privetstvuet pravitelstvo"
        score_surf = score_font.render(chislo, 1, (223, 223, 223))
        screen.blit(score_surf, [x_razg, 220])
        if changa_time > 6:
            chislo = "Changa. Navernoe, Vam stalker Pirat uzhe mnogoe"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 250])
        if changa_time > 8:
            chislo = "objasnil. My ochen seryozno otnositsya k svoej"
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 280])
        if changa_time > 10:
            chislo = "bezopasnoste. My postavim na vash korabl" 
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 310])
        if changa_time > 12:
            chislo = "spidometr. On budet dejstvovat, esli Vy v" 
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 340])
        if changa_time > 14:
            chislo = "sledujutshej raz pribudete v nashu Vselennuju." 
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 370])
        if changa_time > 16:
            chislo = "A teper nazhmite 5,chtoby popast domoj." 
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 400])
        if changa_time > 18:
            chislo = "Do svidanija, putnik!" 
            score_surf = score_font.render(chislo, 1, (223, 223, 223))
            screen.blit(score_surf, [x_razg, 430])
        changa_time = changa_time + 0.02
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_KP5]:
            raz = raz + 1
            running = False
            
    elif ( (int(location[0])+25-(loc[0]-833))**2 + (int(location[1])+25-(loc[1]+50))**2)**0.5 > 400:
        changa_time = 0
        
    if rasst < 125:
        Vse_Game_Name = []
        f = open('Vse_Game_Name.txt', 'r')
        Vse_Game_Name = (eval(f.readlines()[0]))
        f.close()

        index =  Vse_Game_Name[0].index(str(Game_Name))
        del Vse_Game_Name[1][index]
        del Vse_Game_Name[2][index]
        del Vse_Game_Name[3][index]
        del Vse_Game_Name[4][index]
        del Vse_Game_Name[5][index]
        del Vse_Game_Name[6][index]
        del Vse_Game_Name[7][index]
        del Vse_Game_Name[8][index]
        del Vse_Game_Name[9][index]
        del Vse_Game_Name[10][index]
        del Vse_Game_Name[11][index]
        del Vse_Game_Name[12][index]
        Vse_Game_Name[0].remove(Game_Name)

        f = open('Vse_Game_Name.txt', 'w')
        f.write(str(Vse_Game_Name) + '\n')
        f.close()
        
        running = False

        global Game_Over
        Game_Over = True
                
stars_x = []
stars_y = []

for i in range(4000):
        x = random.randint(0, width)
        y = random.randint(0, height)
        stars_x.append(x)
        stars_y.append(y)
def CenterStars():
    knopki()
    loc_CenterStars[0] = loc_CenterStars[0] + b
    loc_CenterStars[1] = loc_CenterStars[1] + a
    pygame.draw.circle(screen, [0,60,240], [int(loc_CenterStars[0]), int(loc_CenterStars[1])], 1, 1)
def Stars():  
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
            
pygame.mixer.music.load("music\\resurection.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(-1)
score = 0

Vse_Game_Name = []
f = open('Vse_Game_Name.txt', 'r')
Vse_Game_Name = eval(f.readlines(0)[0])
f.close()

f = open('game_name_vselennaya.txt', 'r')
Game_Name = f.readline()
f.close()
loc = []

try:
    index1 =  Vse_Game_Name[0].index(str(Game_Name))
except:
    sys.exit()
toplivo = float(Vse_Game_Name[1][index1])
tovar = float(Vse_Game_Name[2][index1])
money = float(Vse_Game_Name[3][index1])
raz = int(Vse_Game_Name[4][index1])
a = float(Vse_Game_Name[9][index1])
b = float(Vse_Game_Name[10][index1])
loc.append(float(Vse_Game_Name[11][index1]))
loc.append(float(Vse_Game_Name[12][index1]))
score_font = pygame.font.Font(None, 36)
score_pos = [10, 10]
score_pos_record = [400, 10]
    
loc_CenterStars = [0, 0]
loc_CenterStars[0] = loc[0] + 50
loc_CenterStars[1] = loc[1] + 50

img_file = "image\platforma.png"
balls = []
speed = [0, 0]
location = [658, 325]
platforma = MyPlatformaClass(img_file, location, speed)
balls.append(platforma)

myachi = pygame.sprite.Group()
myachi.add(platforma)
end_time = 0
pirat_time = 0
changa_time = 0
razgovor = 0
time = 0
koeff = 0.02
t = None
clock = pygame.time.Clock()
paused = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0, 0, 0])
    Stars()
    CenterStars()
    if time > 0.4:
                    
        Back()
    
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
                chislo = "Edinstvennoe, cto vam" 
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [1000, 30])
            if end_time > 1.6:
                chislo = "ostalos, tak eto vecho"
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [1000, 60])
            if end_time > 2.4:
                chislo = "letat mezh zvyozd..."
                score_surf = score_font.render(chislo, 1, (223, 223, 223))
                screen.blit(score_surf, [1000, 90])
            end_time = end_time + 0.02

        if ( (int(location[0])+25-(loc[0]+50))**2 + (int(location[1])+25-(loc[1]+50))**2)**0.5 < 50:
            razgovor = 1
        if razgovor == 1:
            pirat_time = pirat_time + 0.02
        pirat()
        Changa()
        
        for ball in balls:
            platforma.move()
            screen.blit(ball.image, ball.rect)
            
    time = time + 0.02
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
if "Game_Over" not in locals():
    index =  Vse_Game_Name[0].index(str(Game_Name))
    Vse_Game_Name[1][index] = str(toplivo)
    Vse_Game_Name[2][index] = str(tovar)
    Vse_Game_Name[3][index] = str(money)
    Vse_Game_Name[4][index] = str(raz)
    Vse_Game_Name[9][index] = str(a)
    Vse_Game_Name[10][index] = str(b)
    Vse_Game_Name[11][index] = str(loc[0])
    Vse_Game_Name[12][index] = str(loc[1])
    f = open('Vse_Game_Name.txt', 'w')
    f.write(str(Vse_Game_Name) + '\n')
    f.close()
if raz%2 == 0:
    os.system("kosmos.py kosmos")
if "restart" in locals():
    if restart == True:
        os.system("kosmos.py")

