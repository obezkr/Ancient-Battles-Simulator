#v.004
# добавлены щитовики и эта инструкция/реклама внизу
#
#
# создавайте свои армии! левой кнопкой мыши вы создаете армию синих,
# щелчком же правой кнопкой мыши вы создаете армию красных.
# выстраивайте свои войска, и смотрите на их эпичнейшую битву!
# чтобы начать сражение, достаточно лишь нажать R - и пусть победит сильнейший!
# 
#

import pygame
import math

# здесь определяются константы, классы и функции
FPS = 30
WIDTH=1160
HEIGHT=800
Win=(WIDTH, HEIGHT)
razmer=10

WHP=80
RangeW=3
DamageW=15
ReloadW=3
costW=20

AHP=40
StepA=3
RangeA=70
DamageA=50
ReloadA=18
costA=30

SHHP=250
RangeSH=3
DamageSH=7
ReloadSH=5
costSH=30

goldB=1500
goldR=1500
RED=(255, 0, 0)
REDA=(241, 79, 79)
BLUE=(0, 0, 255)
BLUEA=(79, 125, 242)
BLUESH=(84, 0, 255)
REDSH=(239, 33, 112)
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
GOLD=(255, 215, 0)

BW=[]
BWMove=[]
BWHP=[]
BWReload=[]

RW=[]
RWMove=[]
RWHP=[]
RWReload=[]

BA=[]
BAMove=[]
BAHP=[]
BAReload=[]

RA=[]
RAMove=[]
RAHP=[]
RAReload=[]

BSH=[]
BSHMove=[]
BSHHP=[]
BSHReload=[]

RSH=[]
RSHMove=[]
RSHHP=[]
RSHReload=[]

start=False
gameover=False
fighter=0
def MoveBW():
    global xMove, yMove, BW, BA, RA, RW, BWMove, RWMove, RangeW
    #сначала ходят все синие, потом все красные 
    i=0
    while i<len(BW):
        x1=BW[i]
        y1=BW[i+1]
        # здесь идет функция, которая определяет самого ближнего врага
        j=0
        if len(RW)>0:
            x=RW[j]
            y=RW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RW'
        elif len(RA)>0:
            x=RA[j]
            y=RA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RA'
        elif len(RSH)>0:
            x=RSH[j]
            y=RSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RSH'
        j=0
        while j<len(RSH):
            x=RSH[j]
            y=RSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RSH'
            j=j+2
        j=0
        while j<len(RW):
            x=RW[j]
            y=RW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RW'
            j=j+2
        j=0
        while j<len(RA):
            x=RA[j]
            y=RA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RA'
            j=j+2
        
        if mas=='RW':
            x2=RW[jDistance]
            y2=RW[jDistance+1]
        if mas=='RA':
            x2=RA[jDistance]
            y2=RA[jDistance+1]
        if mas=='RSH':
            x2=RSH[jDistance]
            y2=RSH[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeW:
                c=RangeW
            if Distance<=RangeW:
                c=Distance
            a=(c/sinc)*sina
            b=(c/sinc)*sinb
            if x1<x2:
                xMove=x1+a
                yMove=y1+b
            if x1>x2:
                xMove=x1-a
                yMove=y1-b
        if (x2-x1)==0:
            xMove=x1
            if y2>y1:
                yMove=yMove+RangeW
            if y1>y2:
                yMove=yMove-RangeW
            if y1==y2:
                yMove=y1
        BWMove.append(xMove)
        BWMove.append(yMove)
        i=i+2
    BW=BWMove
def MoveRW():
    global xMove, yMove, BW, BA, RA, RW, BWMove, RWMove, RangeW
    i=0
    while i<len(RW):    # теперь ходят красные
        x1=RW[i]
        y1=RW[i+1]
        j=0
        if len(BW)>0:
            x=BW[j]
            y=BW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BW'
        elif len (BA)>0:
            x=BA[j]
            y=BA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BA'
        elif len (BSH)>0:
            x=BSH[j]
            y=BSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BSH'
        while j<len(BSH):
            x=BSH[j]
            y=BSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BSH'
            j=j+2
        j=0
        while j<len(BW):
            x=BW[j]
            y=BW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BW'
            j=j+2
        j=0
        while j<len(BA):
            x=BA[j]
            y=BA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BA'
            j=j+2
        
        if mas=='BW':
            x2=BW[jDistance]
            y2=BW[jDistance+1]
        if mas=='BA':
            x2=BA[jDistance]
            y2=BA[jDistance+1]
        if mas=='BSH':
            x2=BSH[jDistance]
            y2=BSH[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeW:
                c=RangeW
            if Distance<=RangeW:
                c=Distance
            a=(c/sinc)*sina
            b=(c/sinc)*sinb
            if x1<x2:
                xMove=x1+a
                yMove=y1+b
            if x1>x2:
                xMove=x1-a
                yMove=y1-b
        if (x2-x1)==0:
            xMove=x1
            if y2>y1:
                yMove=yMove+RangeW
            if y1>y2:
                yMove=yMove-RangeW
            if y1==y2:
                yMove=y1
        RWMove.append(xMove)
        RWMove.append(yMove)
        i=i+2
    RW=RWMove

    
def MoveBA():
    global xMove, yMove, BA, BW, RW, RA, BAMove, RAMove, RangeA, StepA
    #сначала ходят все синие, потом все красные 
    i=0
    while i<len(BA):
        x1=BA[i]
        y1=BA[i+1]
        # здесь идет функция, которая определяет самого ближнего врага
        j=0
        if len(RW)>0:
            x=RW[j]
            y=RW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RW'
        elif len(RA)>0:
            x=RA[j]
            y=RA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RA'
        elif len(RSH)>0:
            x=RSH[j]
            y=RSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RSH'
        while j<len(RSH):
            x=RSH[j]
            y=RSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RSH'
            j=j+2
        j=0
        while j<len(RW):
            x=RW[j]
            y=RW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RW'
            j=j+2
        j=0
        while j<len(RA):
            x=RA[j]
            y=RA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RA'
            j=j+2
        if mas=='RW':
            x2=RW[jDistance]
            y2=RW[jDistance+1]
        if mas=='RA':
            x2=RA[jDistance]
            y2=RA[jDistance+1]
        if mas=='RSH':
            x2=RSH[jDistance]
            y2=RSH[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeA:
                c=StepA
            if Distance-StepA<=RangeA:
                c=Distance-RangeA
            if Distance<=RangeA:
                c=0
            a=(c/sinc)*sina
            b=(c/sinc)*sinb
            if x1<x2:
                xMove=x1+a
                yMove=y1+b
            if x1>x2:
                xMove=x1-a
                yMove=y1-b
        if (x2-x1)==0:
            xMove=x1
            if y2>y1:
                yMove=yMove+StepA
            if y1>y2:
                yMove=yMove-StepA
            if y1==y2:
                yMove=y1
        BAMove.append(xMove)
        BAMove.append(yMove)
        i=i+2
    BA=BAMove    
   
def MoveRA():
    global xMove, yMove, BA, RA, BW, RW, BAMove, RAMove, RangeA, StepA
    i=0
    while i<len(RA):
        x1=RA[i]
        y1=RA[i+1]
        # здесь идет функция, которая определяет самого ближнего врага
        j=0
        if len(BW)>0:
            x=BW[j]
            y=BW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BW'
        elif len(BA)>0:
            x=BA[j]
            y=BA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BA'
        elif len(BSH)>0:
            x=BSH[j]
            y=BSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BSH'
        while j<len(BSH):
            x=BSH[j]
            y=BSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BSH'
            j=j+2
        j=0
        while j<len(BW):
            x=BW[j]
            y=BW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BW'
            j=j+2
        j=0
        while j<len(BA):
            x=BA[j]
            y=BA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BA'
            j=j+2
        if mas=='BW':
            x2=BW[jDistance]
            y2=BW[jDistance+1]
        if mas=='BA':
            x2=BA[jDistance]
            y2=BA[jDistance+1]
        if mas=='BSH':
            x2=BSH[jDistance]
            y2=BSH[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeA:
                c=StepA
            if Distance-StepA<=RangeA:
                c=Distance-RangeA
            if Distance<=RangeA:
                c=0
            a=(c/sinc)*sina
            b=(c/sinc)*sinb
            if x1<x2:
                xMove=x1+a
                yMove=y1+b
            if x1>x2:
                xMove=x1-a
                yMove=y1-b
        if (x2-x1)==0:
            xMove=x1
            if y2>y1:
                yMove=yMove+StepA
            if y1>y2:
                yMove=yMove-StepA
            if y1==y2:
                yMove=y1
        RAMove.append(xMove)
        RAMove.append(yMove)
        i=i+2
    RA=RAMove
    

def MoveBSH():
    global xMove, yMove, BW, BA, BSH, RA, RW, RSH, BSHMove, RSHMove, RangeSH
    #сначала ходят все синие, потом все красные 
    i=0
    while i<len(BSH):
        x1=BSH[i]
        y1=BSH[i+1]
        # здесь идет функция, которая определяет самого ближнего врага
        j=0
        if len(RSH)>0:
            x=RSH[j]
            y=RSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RSH'
        elif len(RW)>0:
            x=RW[j]
            y=RW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RW'
        elif len(RA)>0:
            x=RA[j]
            y=RA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RA'   
        while j<len(RSH):
            x=RSH[j]
            y=RSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RSH'
            j=j+2
        j=0    
        while j<len(RW):
            x=RW[j]
            y=RW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RW'
            j=j+2
        j=0
        while j<len(RA):
            x=RA[j]
            y=RA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RA'
            j=j+2
        if mas=='RSH':
            x2=RSH[jDistance]
            y2=RSH[jDistance+1]
        if mas=='RW':
            x2=RW[jDistance]
            y2=RW[jDistance+1]
        if mas=='RA':
            x2=RA[jDistance]
            y2=RA[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeSH:
                c=RangeSH
            if Distance<=RangeSH:
                c=Distance
            a=(c/sinc)*sina
            b=(c/sinc)*sinb
            if x1<x2:
                xMove=x1+a
                yMove=y1+b
            if x1>x2:
                xMove=x1-a
                yMove=y1-b
        if (x2-x1)==0:
            xMove=x1
            if y2>y1:
                yMove=yMove+RangeSH
            if y1>y2:
                yMove=yMove-RangeSH
            if y1==y2:
                yMove=y1
        BSHMove.append(xMove)
        BSHMove.append(yMove)
        i=i+2
    BSH=BSHMove

def MoveRSH():
    global xMove, yMove, BW, BA, BSH, RA, RW, RSH, BSHMove, RSHMove, RangeSH
    #сначала ходят все синие, потом все красные 
    i=0
    while i<len(RSH):
        x1=RSH[i]
        y1=RSH[i+1]
        # здесь идет функция, которая определяет самого ближнего врага
        j=0
        if len(BSH)>0:
            x=BSH[j]
            y=BSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BSH'
        elif len(BW)>0:
            x=BW[j]
            y=BW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BW'
        elif len(BA)>0:
            x=BA[j]
            y=BA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BA'
        j=0    
        while j<len(BSH):
            x=BSH[j]
            y=BSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BSH'
            j=j+2
        j=0   
        while j<len(BW):
            x=BW[j]
            y=BW[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BW'
            j=j+2
        j=0
        while j<len(BA):
            x=BA[j]
            y=BA[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BA'
            j=j+2
        if mas=='BSH':
            x2=BSH[jDistance]
            y2=BSH[jDistance+1]
        if mas=='BW':
            x2=BW[jDistance]
            y2=BW[jDistance+1]
        if mas=='BA':
            x2=BA[jDistance]
            y2=BA[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeSH:
                c=RangeSH
            if Distance<=RangeSH:
                c=Distance
            a=(c/sinc)*sina
            b=(c/sinc)*sinb
            if x1<x2:
                xMove=x1+a
                yMove=y1+b
            if x1>x2:
                xMove=x1-a
                yMove=y1-b
        if (x2-x1)==0:
            xMove=x1
            if y2>y1:
                yMove=yMove+RangeSH
            if y1>y2:
                yMove=yMove-RangeSH
            if y1==y2:
                yMove=y1
        RSHMove.append(xMove)
        RSHMove.append(yMove)
        i=i+2
    RSH=RSHMove


def AttackSH():
    global BSHHP, RSHHP, BSH, RSH
    i=0
    while i!=len(BSH): 
        j=0
        udar=0
        if BSHReload[int(i/2)]==ReloadSH:
            while j!=len(RSH):
                if BSH[i]==RSH[j] and BSH[i+1]==RSH[j+1]:
                    if RSHHP[int(j/2)]>0:
                        RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageSH
                        udar=1
                        break
                j=j+2
            if udar==0:
                j=0
                while j!=len(RA):
                    if BSH[i]==RA[j] and BSH[i+1]==RA[j+1]:
                        if RAHP[int(j/2)]>0:
                            RAHP[int(j/2)]=RAHP[int(j/2)]-DamageSH
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RW):
                    if BSH[i]==RW[j] and BSH[i+1]==RW[j+1]:
                        if RWHP[int(j/2)]>0:
                            RWHP[int(j/2)]=RWHP[int(j/2)]-DamageSH
                            udar=1
                            break
                    j=j+2
        if BSHReload[int(i/2)]!=ReloadSH:
            BSHReload[int(i/2)]=BSHReload[int(i/2)]+1
        if udar==1:
            BSHReload[int(i/2)]=0
        i=i+2
        
    i=0
    while i!=len(RSH): 
        j=0
        udar=0
        if RSHReload[int(i/2)]==ReloadSH:
            while j!=len(BSH):
                if RSH[i]==BSH[j] and RSH[i+1]==BSH[j+1]:
                    if BSHHP[int(j/2)]>0:
                        BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageSH
                        udar=1
                        break
                j=j+2
            if udar==0:
                j=0
                while j!=len(BA):
                    if RSH[i]==BA[j] and RSH[i+1]==BA[j+1]:
                        if BAHP[int(j/2)]>0:
                            BAHP[int(j/2)]=BAHP[int(j/2)]-DamageSH
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BW):
                    if RSH[i]==BW[j] and RSH[i+1]==BW[j+1]:
                        if BWHP[int(j/2)]>0:
                            BWHP[int(j/2)]=BWHP[int(j/2)]-DamageSH
                            udar=1
                            break
                    j=j+2
        if RSHReload[int(i/2)]!=ReloadSH:
            RSHReload[int(i/2)]=RSHReload[int(i/2)]+1
        if udar==1:
            RSHReload[int(i/2)]=0
        i=i+2


def AttackA():
    global BWHP, BAHP, RWHP, RAHP, BW, RW, BA, RA
    i=0
    while i!=len(BA):
        j=0
        udar=0
        x1=BA[i]
        y1=BA[i+1]
        if BAReload[int(i/2)]==ReloadA:
            while j!=len(RSH):
                x2=RSH[j]
                y2=RSH[j+1]
                if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                    if RSHHP[int(j/2)]>0:
                        RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageA
                        udar=1
                        break
                j=j+2
            if udar==0:
                j=0
                while j!=len(RW):
                    x2=RW[j]
                    y2=RW[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                        if RWHP[int(j/2)]>0:
                            RWHP[int(j/2)]=RWHP[int(j/2)]-DamageA
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RA):
                    x2=RA[j]
                    y2=RA[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                        if RAHP[int(j/2)]>0:
                            RAHP[int(j/2)]=RAHP[int(j/2)]-DamageA
                            udar=1
                            break
                    j=j+2
        if BAReload[int(i/2)]!=ReloadA:
            BAReload[int(i/2)]=BAReload[int(i/2)]+1
        if udar==1:
            BAReload[int(i/2)]=0
        i=i+2
    i=0
    while i!=len(RA):
        j=0
        udar=0
        x1=RA[i]
        y1=RA[i+1]
        if RAReload[int(i/2)]==ReloadA:
            while j!=len(BSH):
                x2=BSH[j]
                y2=BSH[j+1]
                if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                    if BSHHP[int(j/2)]>0:
                        BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageA
                        udar=1
                        break
                j=j+2
            if udar==0:
                j=0
                while j!=len(BW):
                    x2=BW[j]
                    y2=BW[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                        if BWHP[int(j/2)]>0:
                            BWHP[int(j/2)]=BWHP[int(j/2)]-DamageA
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BA):
                    x2=BA[j]
                    y2=BA[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                        if BAHP[int(j/2)]>0:
                            BAHP[int(j/2)]=BAHP[int(j/2)]-DamageA
                            udar=1
                            break
                    j=j+2
        if RAReload[int(i/2)]!=ReloadA:
            RAReload[int(i/2)]=RAReload[int(i/2)]+1
        if udar==1:
            RAReload[int(i/2)]=0
        i=i+2
        

def AttackW():
    global BWHP, RWHP, BW, RW
    i=0
    while i!=len(BW): #сначала атакуют все синие Warriors
        j=0
        udar=0
        if BWReload[int(i/2)]==ReloadW:
            while j!=len(RSH):
                if BW[i]==RSH[j] and BW[i+1]==RSH[j+1]:
                    if RSHHP[int(j/2)]>0:
                        Bonus=-0.05 #потому что он один раз учитывает себя
                        for o in range(0, len(BW), 2):
                            if BW[i]==BW[o] and BW[i+1]==BW[o+1]:
                                Bonus=Bonus+0.05 # бонус от союзников, которые тоже в этой точке
                        RSHHP[int(j/2)]=RSHHP[int(j/2)]-(DamageW+DamageW*Bonus)
                        udar=1
                        break
                j=j+2
            if udar==0:
                j=0
                while j!=len(RW):
                    if BW[i]==RW[j] and BW[i+1]==RW[j+1]:
                        if RWHP[int(j/2)]>0:
                            Bonus=-0.05 #потому что он один раз учитывает себя
                            for o in range(0, len(BW), 2):
                                if BW[i]==BW[o] and BW[i+1]==BW[o+1]:
                                    Bonus=Bonus+0.05 # бонус от союзников, которые тоже в этой точке
                            RWHP[int(j/2)]=RWHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RA):
                    if BW[i]==RA[j] and BW[i+1]==RA[j+1]:
                        if RAHP[int(j/2)]>0:
                            Bonus=-0.05 #потому что он один раз учитывает себя
                            for o in range(0, len(BW), 2):
                                if BW[i]==BW[o] and BW[i+1]==BW[o+1]:
                                    Bonus=Bonus+0.05 # бонус от союзников, которые тоже в этой точке
                            RAHP[int(j/2)]=RAHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
        if BWReload[int(i/2)]!=ReloadW:
            BWReload[int(i/2)]=BWReload[int(i/2)]+1
        if udar==1:
            BWReload[int(i/2)]=0
        i=i+2
    i=0
    while i!=len(RW): #теперь атакуют все красные
        j=0
        udar=0
        if RWReload[int(i/2)]==ReloadW:
            while j!=len(BSH):
                if RW[i]==BSH[j] and RW[i+1]==BSH[j+1]:
                    if BSHHP[int(j/2)]>0:
                        Bonus=-0.05 #потому что он один раз учитывает себя
                        for o in range(0, len(RW), 2):
                            if RW[i]==RW[o] and RW[i+1]==RW[o+1]:
                                Bonus=Bonus+0.05 # бонус от союзников, которые тоже в этой точке
                        BSHHP[int(j/2)]=BSHHP[int(j/2)]-(DamageW+DamageW*Bonus)
                        udar=1
                        break
                j=j+2
            if udar==0:
                j=0
                while j!=len(BW):
                    if RW[i]==BW[j] and RW[i+1]==BW[j+1]:
                        if BWHP[int(j/2)]>0:
                            Bonus=-0.05 #потому что он один раз учитывает себя
                            for o in range(0, len(RW), 2):
                                if RW[i]==RW[o] and RW[i+1]==RW[o+1]:
                                    Bonus=Bonus+0.05 # бонус от союзников, которые тоже в этой точке
                            BWHP[int(j/2)]=BWHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BA):
                    if RW[i]==BA[j] and RW[i+1]==BA[j+1]:
                        if BAHP[int(j/2)]>0:
                            Bonus=-0.05 #потому что он один раз учитывает себя
                            for o in range(0, len(RW), 2):
                                if RW[i]==RW[o] and RW[i+1]==RW[o+1]:
                                    Bonus=Bonus+0.05 # бонус от союзников, которые тоже в этой точке
                            BAHP[int(j/2)]=BAHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
        if RWReload[int(i/2)]!=ReloadW:
            RWReload[int(i/2)]=RWReload[int(i/2)]+1
        if udar==1:
            RWReload[int(i/2)]=0
        i=i+2
    # удаляем тех, кто погиб (и Warriors, и Archers)
    # в новой функции? да.
    
    
def CheckHP():
    global BW, RW, BWHP, RWHP
    i=0
    while i<len(BWHP):
        if BWHP[i]<=0:
            del BWHP[i]
            del BW[i*2]
            del BW[i*2]
            del BWReload[i]
            i=i-1
        i=i+1
    i=0
    while i<len(BAHP):
        if BAHP[i]<=0:
            del BAHP[i]
            del BA[i*2]
            del BA[i*2]
            del BAReload[i]
            i=i-1
        i=i+1
    i=0
    while i<len(BSHHP):
        if BSHHP[i]<=0:
            del BSHHP[i]
            del BSH[i*2]
            del BSH[i*2]
            del BSHReload[i]
            i=i-1
        i=i+1
    i=0
    while i<len(RWHP):
        if RWHP[i]<=0:
            del RWHP[i]
            del RW[i*2]
            del RW[i*2]
            del RWReload[i]
            i=i-1
        i=i+1
    i=0
    while i<len(RAHP):
        if RAHP[i]<=0:
            del RAHP[i]
            del RA[i*2]
            del RA[i*2]
            del RAReload[i]
            i=i-1
        i=i+1
    i=0
    while i<len(RSHHP):
        if RSHHP[i]<=0:
            del RSHHP[i]
            del RSH[i*2]
            del RSH[i*2]
            del RSHReload[i]
            i=i-1
        i=i+1
   
def CheckWinner():
    global BW, BA, BSH, RW, RA, RSH, gameover
    if len(RW)+len(RA)+len(RSH)==0 and len(BW)+len(BA)+len(BSH)==0:
        print ('tie!')
        gameover=True
    elif len(BW)+len(BA)+len(BSH)==0:
        print ('RED wins!')
        gameover=True
    elif len(RW)+len(RA)+len(RSH)==0:
        print ('BLUE wins!')
        gameover=True
    
        

# здесь происходит инициация, создание объектов и др.
pygame.init()
sc=pygame.display.set_mode(Win)
surf = pygame.Surface(Win)
surf.fill((0, 0, 0))
clock = pygame.time.Clock()
 
# если надо до цикла отобразить объекты на экране
pygame.display.update()


# главный цикл
while True:
    if gameover==True:
        exit()
    gameover=False
    # задержка
    clock.tick(FPS)
    if start==True:
        sc.blit(surf, (0, 0))
        MoveBW()
        MoveRW()
        MoveBA()
        MoveRA()
        MoveBSH()
        MoveRSH()
        AttackW()
        AttackA()
        AttackSH()
        CheckHP()
        CheckWinner()
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_ESCAPE:
                exit()
            if i.key == pygame.K_r:
                start=True
            
        if i.type == pygame.MOUSEBUTTONDOWN:
            x=i.pos[0]
            y=i.pos[1]
            pygame.draw.rect(sc, (BLACK), (900, 0, 260, 100))
            if y>100:
                if i.button == 1:
                    if fighter=='Warriors':
                        if goldB-costW>=0:
                            a=pygame.draw.rect(sc, (BLUE), (x-razmer/2, y-razmer/2, razmer, razmer))
                            BW.append(x-razmer/2)
                            BW.append(y-razmer/2)
                            BWHP.append(WHP)
                            BWReload.append(ReloadW)
                            goldB=goldB-costW
                    if fighter=='Archers':
                        if goldB-costA>=0:
                            a=pygame.draw.rect(sc, (BLUEA), (x-razmer/2, y-razmer/2, razmer, razmer))
                            BA.append(x-razmer/2)
                            BA.append(y-razmer/2)
                            BAHP.append(AHP)
                            BAReload.append(ReloadA)
                            goldB=goldB-costA
                    if fighter=='Shields':
                        if goldB-costSH>=0:
                            a=pygame.draw.rect(sc, (BLUESH), (x-razmer/2, y-razmer/2, razmer, razmer))
                            BSH.append(x-razmer/2)
                            BSH.append(y-razmer/2)
                            BSHHP.append(SHHP)
                            BSHReload.append(ReloadSH)
                            goldB=goldB-costSH
                if i.button == 3:
                    if fighter=='Warriors':
                        if goldR-costW>=0:
                            a=pygame.draw.rect(sc, (RED), (x-razmer/2, y-razmer/2, razmer, razmer))
                            RW.append(x-razmer/2)
                            RW.append(y-razmer/2)
                            RWHP.append(WHP)
                            RWReload.append(ReloadW)
                            goldR=goldR-costW
                    if fighter=='Archers':
                        if goldR-costA>=0:
                            a=pygame.draw.rect(sc, (REDA), (x-razmer/2, y-razmer/2, razmer, razmer))
                            RA.append(x-razmer/2)
                            RA.append(y-razmer/2)
                            RAHP.append(AHP)
                            RAReload.append(ReloadA)
                            goldR=goldR-costA
                    if fighter=='Shields':
                        if goldR-costSH>=0:
                            a=pygame.draw.rect(sc, (REDSH), (x-razmer/2, y-razmer/2, razmer, razmer))
                            RSH.append(x-razmer/2)
                            RSH.append(y-razmer/2)
                            RSHHP.append(SHHP)
                            RSHReload.append(ReloadSH)
                            goldR=goldR-costSH
            if 0<x<80 and 0<y<100:
                fighter='Warriors'
            if 80<x<160 and 0<y<100:
                fighter='Archers'
            if 160<x<240 and 0<y<100:
                fighter='Shields'
            
 
    # --------
    # изменение объектов и многое др.
    # --------
    pygame.draw.line(sc, WHITE, [0, 100], [WIDTH, 100], 3)
    pygame.draw.rect(sc, WHITE, (0, 0, 80, 100))
    
    pygame.draw.rect(sc, WHITE, (80, 0, 80, 100))
    pygame.draw.line(sc, BLACK, [80, 100], [80, 0], 2)
    
    pygame.draw.rect(sc, WHITE, (160, 0, 80, 100))
    pygame.draw.line(sc, BLACK, [160, 100], [160, 0], 2)
    
    lenBW=str(int(len(BW)/2)+int(len(BA)/2)+int(len(BSH)/2))
    lenRW=str(int(len(RW)/2)+int(len(RA)/2)+int(len(RSH)/2))
    f1 = pygame.font.Font(None, 34)
    text1 = f1.render('Blue:', 0, BLUE)
    text1b = f1.render(lenBW, 0, BLUE)
    text2 = f1.render("Red:", 0, RED)
    text2r = f1.render(lenRW, 0, RED)
    f3 = pygame.font.Font(None, 24)
    W = f3.render("Warriors", 0, BLACK)
    A = f3.render("Archers", 0, BLACK)
    SH = f3.render("Shields", 0, BLACK)
    text5 = f3.render(str(goldB), 0, GOLD)
    text6 = f3.render(str(goldR), 0, GOLD)
    
    
    sc.blit(text1, (800, 20))
    sc.blit(text2, (800, 60))
    sc.blit(text1b, (950, 20))
    sc.blit(text2r, (950, 60))
    sc.blit(W, (8, 40))
    sc.blit(A, (88, 40))
    sc.blit(SH, (168, 40))
    sc.blit(text5, (990, 23))
    sc.blit(text6, (990, 63))
        
    i=0
    while i<len(BWMove):
        pygame.draw.rect(sc, (BLUE), (BWMove[i]-razmer/2, BWMove[i+1]-razmer/2, razmer, razmer))
        i=i+2
    BWMove=[]
    i=0
    while i<len(RWMove):
        pygame.draw.rect(sc, (RED), (RWMove[i]-razmer/2, RWMove[i+1]-razmer/2, razmer, razmer))
        i=i+2
    RWMove=[]
    i=0
    while i<len(BAMove):
        pygame.draw.rect(sc, (BLUEA), (BAMove[i]-razmer/2, BAMove[i+1]-razmer/2, razmer, razmer))
        i=i+2
    BAMove=[]
    i=0
    while i<len(RAMove):
        pygame.draw.rect(sc, (REDA), (RAMove[i]-razmer/2, RAMove[i+1]-razmer/2, razmer, razmer))
        i=i+2
    RAMove=[]
    i=0
    while i<len(BSHMove):
        pygame.draw.rect(sc, (BLUESH), (BSHMove[i]-razmer/2, BSHMove[i+1]-razmer/2, razmer, razmer))
        i=i+2
    BSHMove=[]
    i=0
    while i<len(RSHMove):
        pygame.draw.rect(sc, (REDSH), (RSHMove[i]-razmer/2, RSHMove[i+1]-razmer/2, razmer, razmer))
        i=i+2
    RSHMove=[]
    # обновление экрана
    pygame.display.update()



