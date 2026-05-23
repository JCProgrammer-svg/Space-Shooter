import pygame
pygame.init()

win = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Space shooter")
clock = pygame.time.Clock()


x1 =69.5738
x2 =49.1476
x3 =69.5738
x4 =171.705
y1=401.866
y2=350
y3=298.9345
y4=350

xb1 =1130.51
xb2 =1028.29
xb3 =1130.51
xb4 =1150.85
yb1 =401.866
yb2 =350
yb3 =298.9345
yb4 =350

rec1x =320
rec1y = 0
rec2x = 70
rec2y = 0
rec3x = 70
rec3y = 24
rec4x = 320
rec4y = 24

brec1x =1130
brec1y = 0
brec2x = 880
brec2y = 0
brec3x = 880
brec3y = 24
brec4x = 1130
brec4y = 24



vel = 10
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

run = True

def redrawGameWindow():
    for bullet in bullets1:
        bullet.draw(win)
    for bullet in bullets1R:
        bullet.draw(win)
    for bullet in bullets1C:
        bullet.draw(win)
    for bullet in bullets2:
        bullet.draw(win)
    for bullet in bullets2I:
        bullet.draw(win)
    for bullet in bullets2M:
        bullet.draw(win)
    pygame.display.update()

def boundaryleft(x):
    if x<0:
        return False
    return True
def boundaryright(x):
    if x>600:
        return False
    return True
def boundarydown(y):
    if y>700:
        return False
    return True
def boundaryup(y):
    if y<0:
        return False
    return True

def boundarybleft(x):
    if x<600:
        return False
    return True
def boundarybright(x):
    if x>1200:
        return False
    return True
def boundarybdown(y):
    if y>700:
        return False
    return True
def boundarybup(y):
    if y<0:
        return False
    return True

def bullet1collison(x,y,x1,y1,x2,y2,x3,y3):
    if x >= x1 and y == y1 :
        return True
    if x >= (x1 + x3)//2 and y >=(y1 + y2)//2 and y <= (y1 + y3)//2:
        return True
    if x >= x2 and y >= y2 and y <= y3:
        return True

def bullet2collison(x,y,x1,y1,x2,y2,x3,y3):
    if x <= x1 and y == y1 :
        return True
    if x <= (x1 + x3)//2 and y >=(y1 + y2)//2 and y <= (y1 + y3)//2:
        return True
    if x <= x2 and y >= y2 and y <= y3:
        return True

text_font1 = pygame.font.SysFont("franklingothicheavy", 55)
text_font2 = pygame.font.SysFont("microsoftyibaiti", 40)
text_font3 = pygame.font.SysFont("franklingothicheavy", 40)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    win.blit(img, (x, y))

def gameover(x1, x2,x3,x4,player):
    if x1 == x2:
        player = 1
    elif x3 == x4:
        player =2
    return player

player = 0

bullets1 = []
bullets1R = []
bullets1C = []
bullets2 = []
bullets2I = []
bullets2M = []

cooldown = 400

last_shot_1 = {"straight": 0, "diagonal_up": 0, "diagonal_down": 0}
last_shot_2 = {"straight": 0, "diagonal_up": 0, "diagonal_down": 0}


lastshot = pygame.time.get_ticks()

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets1:
        if bullet.x < 1200 and bullet.x > 0:
            bullet.x += bullet.vel  # Moves the bullet by its vel
        else:
            bullets1.pop(bullets1.index(bullet))
        if bullet1collison(bullet.x,bullet.y,xb2,yb2,xb3,yb3,xb1,yb1):
            bullets1.pop(bullets1.index(bullet))
            brec2x +=10
            brec3x +=10
    
    for bullet in bullets1R:
        if bullet.x < 1200 and bullet.x > 0:
            bullet.x += bullet.vel  # Moves the bullet by its vel
            bullet.y -= (bullet.vel * 0.1763)
        else:
            bullets1R.pop(bullets1R.index(bullet))
        if bullet1collison(bullet.x,bullet.y,xb2,yb2,xb3,yb3,xb1,yb1):
            bullets1R.pop(bullets1R.index(bullet))
            brec2x +=10
            brec3x +=10

    for bullet in bullets1C:
        if bullet.x < 1200 and bullet.x > 0:
            bullet.x += bullet.vel  # Moves the bullet by its vel
            bullet.y += (bullet.vel * 0.1763)
        else:
            bullets1C.pop(bullets1C.index(bullet))
        if bullet1collison(bullet.x,bullet.y,xb2,yb2,xb3,yb3,xb1,yb1):
            bullets1C.pop(bullets1C.index(bullet))
            brec2x +=10
            brec3x +=10

    for bullet in bullets2:
        if bullet.x < 1200 and bullet.x > 0:
            bullet.x += bullet.vel  # Moves the bullet by its vel
        else:
            bullets2.pop(bullets2.index(bullet))
        if bullet2collison(bullet.x,bullet.y,x4,y4,x3,y3,x1,y1):
            bullets2.pop(bullets2.index(bullet))
            rec1x -=10
            rec4x -=10

    for bullet in bullets2I:
        if bullet.x < 1200 and bullet.x > 0:
            bullet.x += bullet.vel  # Moves the bullet by its vel
            bullet.y += (bullet.vel * 0.1763)
        else:
            bullets2I.pop(bullets2I.index(bullet))
        if bullet2collison(bullet.x,bullet.y,x4,y4,x3,y3,x1,y1):
            bullets2I.pop(bullets2I.index(bullet))
            rec1x -=10
            rec4x -=10

    for bullet in bullets2M:
        if bullet.x < 1200 and bullet.x > 0:
            bullet.x += bullet.vel  # Moves the bullet by its vel
            bullet.y -= (bullet.vel * 0.1763)
        else:
            bullets2M.pop(bullets2M.index(bullet))
        if bullet2collison(bullet.x,bullet.y,x4,y4,x3,y3,x1,y1):
            bullets2M.pop(bullets2M.index(bullet))
            rec1x -=10
            rec4x -=10


    keys = pygame.key.get_pressed()
    
    timenow = pygame.time.get_ticks()

    if keys[pygame.K_f] and timenow - last_shot_1["straight"] > cooldown:
        bullets1.append(projectile(x4, y4, 6, (150, 150, 150), 1))
        last_shot_1["straight"] = timenow
    if keys[pygame.K_r] and timenow - last_shot_1["diagonal_up"] > cooldown:
        bullets1R.append(projectile(x4, y4, 6, (150, 150, 150), 1))
        last_shot_1["diagonal_up"] = timenow
    if keys[pygame.K_c] and timenow - last_shot_1["diagonal_down"] > cooldown:
        bullets1C.append(projectile(x4, y4, 6, (150, 150, 150), 1))
        last_shot_1["diagonal_down"] = timenow

# Handle shooting for Player 2
    if keys[pygame.K_j] and timenow - last_shot_2["straight"] > cooldown:
        bullets2.append(projectile(xb2, yb2, 6, (150, 150, 150), -1))
        last_shot_2["straight"] = timenow
    if keys[pygame.K_i] and timenow - last_shot_2["diagonal_up"] > cooldown:
        bullets2I.append(projectile(xb2, yb2, 6, (150, 150, 150), -1))
        last_shot_2["diagonal_up"] = timenow
    if keys[pygame.K_m] and timenow - last_shot_2["diagonal_down"] > cooldown:
        bullets2M.append(projectile(xb2, yb2, 6, (150, 150, 150), -1))
        last_shot_2["diagonal_down"] = timenow

    if (keys[pygame.K_a] and boundaryleft(x2)):
        x1 -= vel
        x2 -= vel
        x3 -= vel
        x4 -= vel
    
    if (keys[pygame.K_d] and boundaryright(x4)):
        x1 += vel
        x2 += vel
        x3 += vel
        x4 += vel

    if (keys[pygame.K_w] and boundaryup(y3)):
        y1 -= vel
        y2 -= vel
        y3 -= vel
        y4 -= vel

    if (keys[pygame.K_s] and boundarydown(y1)):
        y1 += vel
        y2 += vel
        y3 += vel
        y4 += vel
    
    if (keys[pygame.K_LEFT] and boundarybleft(xb2)):
        xb1 -= vel
        xb2 -= vel
        xb3 -= vel
        xb4 -= vel
    
    if (keys[pygame.K_RIGHT] and boundarybright(xb4)):
        xb1 += vel
        xb2 += vel
        xb3 += vel
        xb4 += vel

    if (keys[pygame.K_UP] and boundarybup(yb3)):
        yb1 -= vel
        yb2 -= vel
        yb3 -= vel
        yb4 -= vel

    if (keys[pygame.K_DOWN] and boundarybdown(yb1)):
        yb1 += vel
        yb2 += vel
        yb3 += vel
        yb4 += vel

    player = gameover(brec1x,brec2x,rec1x,rec2x,player)
    if  player > 0:
        run = False
    

    recpoint1 = (rec1x,rec1y)
    recpoint2 = (rec2x,rec2y)
    recpoint3 = (rec3x,rec3y)
    recpoint4 = (rec4x,rec4y)

    brecpoint1 = (brec1x,brec1y)
    brecpoint2 = (brec2x,brec2y)
    brecpoint3 = (brec3x,brec3y)
    brecpoint4 = (brec4x,brec4y)

    point1 = (x1, y1)
    point2 = (x2,y2)
    point3 = (x3, y3)
    point4 = (x4, y4)

    pointb1 = (xb1, yb1)
    pointb2 = (xb2,yb2)
    pointb3 = (xb3, yb3)
    pointb4 = (xb4, yb4)

    
    
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.polygon(win, (90,36,232), [point1, point2, point3, point4])  #This takes: window/surface, color, rect 
    pygame.draw.polygon(win, (19,196,196), [pointb1, pointb2, pointb3, pointb4])  #This takes: window/surface, color, rect 
    pygame.draw.polygon(win, (255,0,0), [recpoint1,recpoint2,recpoint3,recpoint4])  #This takes: window/surface, color, rect
    pygame.draw.polygon(win, (255,0,0), [brecpoint1,brecpoint2,brecpoint3,brecpoint4])  #This takes: window/surface, color, rect
    pygame.draw.polygon(win,(255,255,255),[(600,0),(600,700)],width=3)
    draw_text("P1",text_font3,(85,125,185),10,0)
    draw_text("P2",text_font3,(19,196,196),1140,0)
    pygame.display.update() # This updates the screen so we can see our rectangle
    redrawGameWindow()


if player > 0:
    draw_text("GAME OVER",text_font1,(85,125,185),440,250)
    if player ==1:
        draw_text("player  1 won",text_font2,(90,36,232),500,300)
    elif player == 2:
        draw_text("player  2 won",text_font2,(19,196,196),500,300)
    pygame.display.update()
    pygame.time.delay(3000)
