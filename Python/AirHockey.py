import pygame,sys
import random
from pygame.locals import *
from sys import exit

pygame.init()

size=[500,700]
screen=pygame.display.set_mode(size)

#Initialising the screen and fonts
screen1=pygame.display.set_mode(size)
pygame.display.set_caption("Air Hockey")
font1=pygame.font.SysFont("calibri",25)
font2=pygame.font.SysFont("calibri",40)
font3=pygame.font.SysFont("calibri",30)
font4=pygame.font.SysFont("calibri",50)

#Defining colors
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red =(255,0,0)
blue=(0,0,255)
yellow=(255,255,0)
aqua=(0,255,255)
silver=(192,192,192)
dgreen=(0,65,0)
fushia=(128,0,128)


#File to store scores
def create_score(c,p):
    scorefile=open('Scores.dat','ab')
    pickle.dump([c,p],scorefile)
    scorefile.close()
    scorefile=open('Scores.dat','rb+')
    print "\nCOMPUTER","\t"*3,"PLAYER"
    while True:
        try:        
            score=pickle.load(scorefile)
            print score[0],"\t"*4,score[1]
        except EOFError:            
            scorefile.close()
            break

#Home screen
def intro():
    pygame.draw.rect(screen1,white,(25,25,450,650),0)
    screen1.fill(fushia)
    pygame.draw.rect(screen1, green,(175,500,150,50),0)


#Designing the layout    
def table():
    pygame.draw.rect(screen, black,(25,25,450,650),0)
    pygame.draw.circle(screen, yellow, [250,350],50,5)
    pygame.draw.circle(screen, yellow, [250,350],10)
    pygame.draw.line(screen, yellow, [25,350],[475,350],5)
    pygame.draw.rect(screen, black,(25,25,450,650),5)
    pygame.draw.rect(screen,silver ,(200,10,100,20),0)
    pygame.draw.rect(screen,silver ,(200,670,100,20),0)

#Updating home screen
def homescreen(c,p):
    if c >=5:
        cpuwin=font4.render("YOU LOSE",True,white)
        screen.blit(cpuwin,(150,250))
        pygame.display.flip()
    if p >=5:
        cpuwin=font4.render("YOU WIN",True,white)
        screen.blit(cpuwin,(150,250))
        pygame.display.flip()
    playerScore=0
    cpuScore=0
            
    begin=False
    while begin==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit ()
                sys.exit()
            intro()
            msg=font2.render("WELCOME TO AIR HOCKEY!!!",True,aqua)
            rules=list()
            rules =['RULES:','1. Use the mouse to control the lower',
               'mallet to score.',
           '2. Press r to restart the game.','3. Press space to pause/play.',
           'Score 5 goals to win the game']
            n=len(rules)
            x=0
            for i in range(n):
                printmsg=font3.render(rules [i],True,aqua)
                screen1.blit(printmsg,(25,150+x))
                x+=50                  
            bmsg=font2.render("PLAY!",True,red)
            screen1.blit(bmsg,(210,510))
            screen1.blit(msg,(25,50))
            loc=pygame.mouse.get_pos()
            if loc[0]>150 and loc[0]<300 and loc[1]>500 and loc[1]<550:
                pygame.draw.rect(screen1, dgreen,(175,500,150,50),0)
                screen1.blit(bmsg,(210,510))
                click=pygame.mouse.get_pressed()
                if click[0]==1:
                    begin=True
                    break
            pygame.display.update()
            clock.tick(30)


cpuScore=0
playerScore=0
pStart_x=250
pStart_y=350

#Creating the puck
class Puck(object):
    def __init__(self,x,y,dx=0,dy=0):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.pStart_x=self.x
        self.pStart_y=self.y
    def update_Puck(self):
        if self.x<=40:
            self.x=42
            self.dx*=-1
        elif self.x>=460:
            self.x =458
            self.dx*=-1
        if self.y<=30:
            self.y=32
            self.dy*=-1 
        elif self.y>=670:
            self.y=668
            self.dy*=-1
        self.x+=self.dx
        self.y+=self.dy
    def fric_Puck(self):
        if self.dx>1:
            self.dx-=1
        elif self.dx<-1:
            self.dx+=1
        if self.dy>1:
            self.dy-=1
        elif self.dy<-1:
            self.dy+=1
    def draw_Puck(self):
        pygame.draw.circle(screen,red, [self.x,self.y],15,0)
    def limitPuckSpeed(self):
        if self.dx>10:
            self.dx=10
        if self.dx<-10:
            self.dx=-10
        if self.dy>10:
            self.dy=10
        if self.dy<-10:
            self.dy=10
    def reset(self):
        self.x=self.pStart_x
        self.y=self.pStart_y
        self.dx=0
        self.dy=0
puck1 = Puck(pStart_x,pStart_y)



#Creating the mallet
class Mallet(object):
    def __init__(self,malletType,x,y,uLim=50,bLim=650,lLim=50,rLim=450,dx=0,dy=0):
        self.x=x
        self.y=y
        self.last_x=self.x
        self.last_y=self.y
        
        self.malletType = malletType
        
        self.uLim=uLim
        self.bLim=bLim
        self.lLim=lLim
        self.rLim=rLim
                
        self.dx=dx
        self.dy=dy
        
        self.malletStart_x=self.x
        self.malletStart_y=self.y
        
    def update_Mallet(self):
        if self.malletType!="MP":
            self.x+=self.dx
            self.y+=self.dy
        if self.x<self.lLim:
            self.x=self.lLim
        elif self.x>self.rLim:
            self.x=self.rLim
        if self.y<self.uLim:
            self.y=self.uLim
        elif self.y>self.bLim:
            self.y=self.bLim
        
    def draw_Mallet(self):
        pygame.draw.circle(screen, white, [self.x,self.y],20,0)
        pygame.draw.circle(screen, green, [self.x,self.y],20,1)
        pygame.draw.circle(screen, green, [self.x,self.y],5,0)
        
    def reset_Mallet(self):
        self.x = self.malletStart_x
        self.y = self.malletStart_y
    
upperMallet=Mallet("AI",250,100,50,330)
lowerMallet=Mallet("MP",250,600,370,650)

def malletAI(upperMallet):
    if puck1.x < upperMallet.x:
        if puck1.x < upperMallet.lLim:
            upperMallet.dx=1
        else:
            upperMallet.dx=-2
    if puck1.x > upperMallet.x:
        if  puck1.x > upperMallet.rLim:
            upperMallet.dx=-1


        else:
            upperMallet.dx=2
    if puck1.y < upperMallet.y:
        if puck1.y < upperMallet.uLim:
            upperMallet.dy=1
        else:
            upperMallet.dy=-6
    if puck1.y > upperMallet.y:
        if puck1.y<=360: 
            upperMallet.dy=6
        else:
            if upperMallet.y>200:
                upperMallet.dy=-2
            else:
                upperMallet.dy=0
        if abs(puck1.y-upperMallet.y)<20 and abs(puck1.x-upperMallet.x)<20:
            puck1.dy +=2
#Goal
class Goal(object):
    def __init__(self,x,y,w=100,h=20):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
        self.centre_x=self.x+self.w/2
        self.centre_y=self.y+self.w/2
       
upperGoal=Goal(200,10)
lowerGoal=Goal(200,670)

ticksToFriction=60
ticksToAI=10
c=p=0
cpuScore=0
playerScore=0

pause=False
clock=pygame.time.Clock()
homescreen(c,p)

#Pausing
while pause==False:
  
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            pygame.quit ()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print "Game reset..."
                cpuScore=0
                playerScore=0
                puck1.reset()
                upperMallet.reset_Mallet()
            if event.key == pygame.K_SPACE:
                pause=True
                while pause==True:
                    for event in pygame.event.get():
                        if event.type==pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                pause=False               
    

    pos=pygame.mouse.get_pos()
    lowerMallet.x=pos[0]
    lowerMallet.y=pos[1]
    lowerMallet.update_Mallet()
    
    lowerMallet.dx=lowerMallet.x-lowerMallet.last_x
    lowerMallet.dy=lowerMallet.y-lowerMallet.last_y
    while ticksToAI==0:
        malletAI(upperMallet)
        ticksToAI=10    
            
    if (abs(upperMallet.x-puck1.x)<=35 and abs(upperMallet.y-puck1.y)<=35):
        puck1.dx=-1*puck1.dx+upperMallet.dx
        puck1.dy=-1*puck1.dy+upperMallet.dy
    
    if (abs(lowerMallet.x-puck1.x)<=35 and abs(lowerMallet.y-puck1.y)<=35):
        puck1.dx=-1*puck1.dx+lowerMallet.dx
        puck1.dy=-1*puck1.dy+lowerMallet.dy
    
    puck1.limitPuckSpeed()        

    #Scoring a goal           
    if (abs(lowerGoal.centre_y-puck1.y)<=50 and abs(lowerGoal.centre_x-puck1.x)<=50):
        print "Computer Scores!"
        cpuScore+=1
        print "User:", playerScore,"Computer:",cpuScore
        
        if cpuScore==5:
            c=cpuScore
            p=playerScore
            playerScore=0
            cpuScore=0
            print "\nComputer Wins!"
                        
            homescreen(c,p)
        puck1.reset()
        upperMallet.reset_Mallet()
                
    if (abs(upperGoal.centre_y-puck1.y)<=5 and abs(upperGoal.centre_x-puck1.x)<=40):
        print "User Scores!"
        playerScore += 1
        print "User:", playerScore,"Computer:", cpuScore
              
        if playerScore==5:           
            print "\nYou Win!"
            c=cpuScore
            p=playerScore
            playerScore=0
            cpuScore=0           
            homescreen(c,p)
        puck1.reset()
        upperMallet.reset_Mallet()            

    screen.fill(blue)
    table()
    
    puck1.draw_Puck()
    
    upperMallet.draw_Mallet()
    lowerMallet.draw_Mallet()
    
    AIScore=font1.render(str(cpuScore), True,aqua)
    MPScore=font1.render(str(playerScore), True,aqua)
    screen.blit(AIScore,(30,50))                
    screen.blit(MPScore,(30,650))
    
    pygame.display.flip()    #Updating the screen
        
    puck1.update_Puck()
    while ticksToFriction==0:
        puck1.fric_Puck()
        ticksToFriction=60
    upperMallet.update_Mallet()
    
    lowerMallet.last_x=lowerMallet.x
    lowerMallet.last_y=lowerMallet.y

    ticksToFriction-=1
    ticksToAI-=1
    clock.tick(100)    #Change this to control speed


