#v.008
# редактор кампаний - здесь можно создавать свои уровни
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
costW=25

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

PHP=50
StepP=3
RangeP=60
HealthP=15
ReloadP=6
costP=20

razmerC=15
CHP=50
StepC=2
RangeC=100
RangeCE=20
DamageC=80
ReloadC=50
costC=300

goldB=1500
goldR=2500

RED=(255, 0, 0)
REDA=(241, 79, 79)
REDSH=(196, 1, 105)
REDP=(247, 133, 76)
REDC=(178, 59, 0)
BLUE=(0, 0, 255)
BLUEA=(79, 125, 242)
BLUESH=(84, 0, 255)
BLUEP=(47, 179, 249)
BLUEC=(0, 95, 178)
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

BP=[]
BPMove=[]
BPHP=[]
BPReload=[]

RP=[]
RPMove=[]
RPHP=[]
RPReload=[]

BC=[]
BCMove=[]
BCHP=[]
BCReload=[]

RC=[]
RCMove=[]
RCHP=[]
RCReload=[]

mes=0
spl=0
start=False
gameover=False
fighter=0
admin=[]
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
        elif len(RP)>0:
            x=RP[j]
            y=RP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RP'
        elif len(RSH)>0:
            x=RSH[j]
            y=RSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RSH'
        elif len(RC)>0:
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RC'
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
        j=0
        while j<len(RP):
            x=RP[j]
            y=RP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RP'
            j=j+2
        j=0
        while j<len(RC):
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RC'
            j=j+2
        
        if mas=='RW':
            x2=RW[jDistance]
            y2=RW[jDistance+1]
        if mas=='RA':
            x2=RA[jDistance]
            y2=RA[jDistance+1]
        if mas=='RP':
            x2=RP[jDistance]
            y2=RP[jDistance+1]
        if mas=='RSH':
            x2=RSH[jDistance]
            y2=RSH[jDistance+1]
        if mas=='RC':
            x2=RC[jDistance]
            y2=RC[jDistance+1]
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
            if Distance>RangeW:
                c=RangeW
            if Distance<=RangeW:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
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
        elif len (BP)>0:
            x=BP[j]
            y=BP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BP'
        elif len (BSH)>0:
            x=BSH[j]
            y=BSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BSH'
        elif len (BC)>0:
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BC'
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
        j=0
        while j<len(BP):
            x=BP[j]
            y=BP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BP'
            j=j+2
        j=0
        while j<len(BC):
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BC'
            j=j+2
        
        if mas=='BW':
            x2=BW[jDistance]
            y2=BW[jDistance+1]
        if mas=='BA':
            x2=BA[jDistance]
            y2=BA[jDistance+1]
        if mas=='BP':
            x2=BP[jDistance]
            y2=BP[jDistance+1]
        if mas=='BSH':
            x2=BSH[jDistance]
            y2=BSH[jDistance+1]
        if mas=='BC':
            x2=BC[jDistance]
            y2=BC[jDistance+1]
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
            if Distance>RangeW:
                c=RangeW
            if Distance<=RangeW:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
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
        elif len(RP)>0:
            x=RP[j]
            y=RP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RP'
        elif len(RSH)>0:
            x=RSH[j]
            y=RSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RSH'
        elif len(RC)>0:
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RC'
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
        j=0
        while j<len(RP):
            x=RP[j]
            y=RP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RP'
            j=j+2
        j=0
        while j<len(RC):
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RC'
            j=j+2
        if mas=='RW':
            x2=RW[jDistance]
            y2=RW[jDistance+1]
        if mas=='RA':
            x2=RA[jDistance]
            y2=RA[jDistance+1]
        if mas=='RP':
            x2=RP[jDistance]
            y2=RP[jDistance+1]
        if mas=='RSH':
            x2=RSH[jDistance]
            y2=RSH[jDistance+1]
        if mas=='RC':
            x2=RC[jDistance]
            y2=RC[jDistance+1]
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
            if Distance>RangeA:
                c=StepA
            if Distance<=RangeA:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
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
        elif len(BP)>0:
            x=BP[j]
            y=BP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BP'
        elif len(BSH)>0:
            x=BSH[j]
            y=BSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BSH'
        elif len(BC)>0:
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BC'
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
        j=0
        while j<len(BP):
            x=BP[j]
            y=BP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BP'
            j=j+2
        j=0
        while j<len(BC):
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BC'
            j=j+2
        if mas=='BW':
            x2=BW[jDistance]
            y2=BW[jDistance+1]
        if mas=='BA':
            x2=BA[jDistance]
            y2=BA[jDistance+1]
        if mas=='BP':
            x2=BP[jDistance]
            y2=BP[jDistance+1]
        if mas=='BSH':
            x2=BSH[jDistance]
            y2=BSH[jDistance+1]
        if mas=='BC':
            x2=BC[jDistance]
            y2=BC[jDistance+1]
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
            if Distance>RangeA:
                c=StepA
            if Distance<=RangeA:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
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
        elif len(RP)>0:
            x=RP[j]
            y=RP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RP'
        elif len(RC)>0:
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RC'
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
        j=0
        while j<len(RP):
            x=RP[j]
            y=RP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RP'
            j=j+2
        j=0
        while j<len(RC):
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RC'
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
        if mas=='RP':
            x2=RP[jDistance]
            y2=RP[jDistance+1]
        if mas=='RC':
            x2=RC[jDistance]
            y2=RC[jDistance+1]
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
            if Distance>RangeSH:
                c=RangeW
            if Distance<=RangeSH:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
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
        elif len(BP)>0:
            x=BP[j]
            y=BP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BP'
        elif len(BC)>0:
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BC'
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
        j=0
        while j<len(BP):
            x=BP[j]
            y=BP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BP'
            j=j+2
        j=0
        while j<len(BC):
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BC'
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
        if mas=='BP':
            x2=BP[jDistance]
            y2=BP[jDistance+1]
        if mas=='BC':
            x2=BC[jDistance]
            y2=BC[jDistance+1]
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
            if Distance>RangeSH:
                c=RangeW
            if Distance<=RangeSH:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
            if y1==y2:
                yMove=y1
        RSHMove.append(xMove)
        RSHMove.append(yMove)
        i=i+2
    RSH=RSHMove


def MoveBP():
    global xMove, yMove, BA, BW, RW, RA, BP, RP, BSH, RSH, BPMove, RPMove, RangeP, StepP
    #сначала ходят все синие, потом все красные 
    i=0
    while i<len(BP):
        if len(BW)+len(BA)+len(BSH)+len(BC)==0:
            BPMove=BP
            break
        x1=BP[i]
        y1=BP[i+1]
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
        elif len(BC)>0:
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BC'
        elif len(BP)>0:
            x=BP[j]
            y=BP[j+1]
            if x1!=x and y1!=y:
                Sa=((x1-x)**2+(y1-y)**2)**0.5
                Distance=Sa
                jDistance=j
                mas='BP'
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
        j=0
        while j<len(BC):
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BC'
            j=j+2
        j=0
        if mas!='BW' and mas!='BA' and mas!='BSH' and mas!='BC':
            while j<len(BP):
                x=BP[j]
                y=BP[j+1]
                if x1!=x and y1!=y:
                    Sa=((x1-x)**2+(y1-y)**2)**0.5
                    if Sa<Distance:
                        Distance=Sa
                        jDistance=j
                        mas='BP'
                j=j+2
        if mas=='BW':
            x2=BW[jDistance]
            y2=BW[jDistance+1]
        if mas=='BA':
            x2=BA[jDistance]
            y2=BA[jDistance+1]
        if mas=='BP':
            x2=BP[jDistance]
            y2=BP[jDistance+1]
        if mas=='BSH':
            x2=BSH[jDistance]
            y2=BSH[jDistance+1]
        if mas=='BC':
            x2=BC[jDistance]
            y2=BC[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeP-StepP:
                c=StepP
            if Distance<=RangeP-StepP:
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
            if Distance>RangeP:
                c=StepA
            if Distance<=RangeP:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
            if y1==y2:
                yMove=y1
        BPMove.append(xMove)
        BPMove.append(yMove)
        i=i+2
    BP=BPMove
    
   
def MoveRP():
    global xMove, yMove, BA, RA, BW, RW, BSH, RSH, BP, RP, BPMove, RPMove, RangeP, StepP
    i=0
    while i<len(RP):
        if len(RW)+len(RA)+len(RSH)+len(RC)==0:
            RPMove=RP
            break
        x1=RP[i]
        y1=RP[i+1]
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
        elif len(RC)>0:
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RC'
        elif len(RP)>0:
            x=RP[j]
            y=RP[j+1]
            if x1!=x and y1!=y:
                Sa=((x1-x)**2+(y1-y)**2)**0.5
                Distance=Sa
                jDistance=j
                mas='RP'
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
        j=0
        while j<len(RC):
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RC'
            j=j+2
        j=0
        if mas!='RW' and mas!='RA' and mas!='RSH' and mas!='RC':
            while j<len(RP):
                x=RP[j]
                y=RP[j+1]
                if x1!=x and y1!=y:
                    Sa=((x1-x)**2+(y1-y)**2)**0.5
                    if Sa<Distance:
                        Distance=Sa
                        jDistance=j
                        mas='RP'
                j=j+2
        if mas=='RW':
            x2=RW[jDistance]
            y2=RW[jDistance+1]
        if mas=='RA':
            x2=RA[jDistance]
            y2=RA[jDistance+1]
        if mas=='RP':
            x2=RP[jDistance]
            y2=RP[jDistance+1]
        if mas=='RSH':
            x2=RSH[jDistance]
            y2=RSH[jDistance+1]
        if mas=='RC':
            x2=RC[jDistance]
            y2=RC[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeP-StepP:
                c=StepP
            if Distance<=RangeP-StepP:
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
            if Distance>RangeP:
                c=StepA
            if Distance<=RangeP:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
            if y1==y2:
                yMove=y1
        RPMove.append(xMove)
        RPMove.append(yMove)
        i=i+2
    RP=RPMove


###################################################################################
    

def MoveBC():
    global xMove, yMove, BC, BW, RW, RC, BCMove, RCMove, RangeC, StepC
    #сначала ходят все синие, потом все красные 
    i=0
    while i<len(BC):
        x1=BC[i]
        y1=BC[i+1]
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
        elif len(RP)>0:
            x=RP[j]
            y=RP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RP'
        elif len(RSH)>0:
            x=RSH[j]
            y=RSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RSH'
        elif len(RC)>0:
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='RC'
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
        j=0
        while j<len(RP):
            x=RP[j]
            y=RP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RP'
            j=j+2
        j=0
        while j<len(RC):
            x=RC[j]
            y=RC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='RC'
            j=j+2
        if mas=='RW':
            x2=RW[jDistance]
            y2=RW[jDistance+1]
        if mas=='RA':
            x2=RA[jDistance]
            y2=RA[jDistance+1]
        if mas=='RP':
            x2=RP[jDistance]
            y2=RP[jDistance+1]
        if mas=='RSH':
            x2=RSH[jDistance]
            y2=RSH[jDistance+1]
        if mas=='RC':
            x2=RC[jDistance]
            y2=RC[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeC:
                c=StepC
            if Distance-StepC<=RangeC:
                c=Distance-RangeC
            if Distance<=RangeC:
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
            if Distance>RangeC:
                c=StepC
            if Distance<=RangeC:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
            if y1==y2:
                yMove=y1
        BCMove.append(xMove)
        BCMove.append(yMove)
        i=i+2
    BC=BCMove    
   
def MoveRC():
    global xMove, yMove, BC, RC, BW, RW, BCMove, RCMove, RangeC, StepC
    i=0
    while i<len(RC):
        x1=RC[i]
        y1=RC[i+1]
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
        elif len(BP)>0:
            x=BP[j]
            y=BP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BP'
        elif len(BSH)>0:
            x=BSH[j]
            y=BSH[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BSH'
        elif len(BC)>0:
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            Distance=Sa
            jDistance=j
            mas='BC'
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
        j=0
        while j<len(BP):
            x=BP[j]
            y=BP[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BP'
            j=j+2
        j=0
        while j<len(BC):
            x=BC[j]
            y=BC[j+1]
            Sa=((x1-x)**2+(y1-y)**2)**0.5
            if Sa<Distance:
                Distance=Sa
                jDistance=j
                mas='BC'
            j=j+2
        if mas=='BW':
            x2=BW[jDistance]
            y2=BW[jDistance+1]
        if mas=='BA':
            x2=BA[jDistance]
            y2=BA[jDistance+1]
        if mas=='BP':
            x2=BP[jDistance]
            y2=BP[jDistance+1]
        if mas=='BSH':
            x2=BSH[jDistance]
            y2=BSH[jDistance+1]
        if mas=='BC':
            x2=BC[jDistance]
            y2=BC[jDistance+1]
        if (x2-x1)!=0:
            k=(y2-y1)/(x2-x1)
            k=math.atan(k)
            sina=math.radians(90-(math.degrees(k)))
            sina=math.sin(sina)
            sinb=math.sin(k)
            sinc=math.radians(90)
            sinc=math.sin(sinc)
            if Distance>RangeC:
                c=StepC
            if Distance-StepC<=RangeC:
                c=Distance-RangeC
            if Distance<=RangeC:
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
            if Distance>RangeC:
                c=StepC
            if Distance<=RangeC:
                c=Distance
            if y2>y1:
                yMove=y1+c
            if y1>y2:
                yMove=y1-c
            if y1==y2:
                yMove=y1
        RCMove.append(xMove)
        RCMove.append(yMove)
        i=i+2
    RC=RCMove


def AttackC():
    global BWHP, BCHP, RWHP, RCHP, BW, RW, BC, RC, BP, RP, RangeCE
    i=0
    while i!=len(BC):
        jj=0
        udar=0
        x1=BC[i]
        y1=BC[i+1]
        if BCReload[int(i/2)]==ReloadC:
            while jj!=len(RSH):
                x2=RSH[jj]
                y2=RSH[jj+1]
                if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                    if RSHHP[int(jj/2)]>0:
                        udar=1
                        # все в радиусе от цели получают урон
                        j=0
                        while j<len(RSH):
                            x=RSH[j]
                            y=RSH[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(RW):
                            x=RW[j]
                            y=RW[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(RA):
                            x=RA[j]
                            y=RA[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(RP):
                            x=RP[j]
                            y=RP[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(RC):
                            x=RC[j]
                            y=RC[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                            j=j+2
                        break
                jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(RW):
                    x2=RW[jj]
                    y2=RW[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if RWHP[int(jj/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(RSH):
                                x=RSH[j]
                                y=RSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RW):
                                x=RW[j]
                                y=RW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RA):
                                x=RA[j]
                                y=RA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RP):
                                x=RP[j]
                                y=RP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RC):
                                x=RC[j]
                                y=RC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2 
            if udar==0:
                jj=0
                while jj!=len(RA):
                    x2=RA[jj]
                    y2=RA[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if RAHP[int(jj/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(RSH):
                                x=RSH[j]
                                y=RSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RW):
                                x=RW[j]
                                y=RW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RA):
                                x=RA[j]
                                y=RA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RP):
                                x=RP[j]
                                y=RP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RC):
                                x=RC[j]
                                y=RC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(RP):
                    x2=RP[jj]
                    y2=RP[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if RPHP[int(jj/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(RSH):
                                x=RSH[j]
                                y=RSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RW):
                                x=RW[j]
                                y=RW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RA):
                                x=RA[j]
                                y=RA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RP):
                                x=RP[j]
                                y=RP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RC):
                                x=RC[j]
                                y=RC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(RC):
                    x2=RC[jj]
                    y2=RC[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if RCHP[int(jj/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(RSH):
                                x=RSH[j]
                                y=RSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RSHHP[int(j/2)]=RSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RW):
                                x=RW[j]
                                y=RW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RWHP[int(j/2)]=RWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RA):
                                x=RA[j]
                                y=RA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RAHP[int(j/2)]=RAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RP):
                                x=RP[j]
                                y=RP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RPHP[int(j/2)]=RPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(RC):
                                x=RC[j]
                                y=RC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    RCHP[int(j/2)]=RCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
        if BCReload[int(i/2)]!=ReloadC:
            BCReload[int(i/2)]=BCReload[int(i/2)]+1
        if udar==1:
            BCReload[int(i/2)]=0
        i=i+2
    i=0
    while i!=len(RC):
        jj=0
        udar=0
        x1=RC[i]
        y1=RC[i+1]
        if RCReload[int(i/2)]==ReloadC:
            while jj!=len(BSH):
                x2=BSH[jj]
                y2=BSH[jj+1]
                if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                    if BSHHP[int(jj/2)]>0:
                        udar=1
                        # все в радиусе от цели получают урон
                        j=0
                        while j<len(BSH):
                            x=BSH[j]
                            y=BSH[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(BW):
                            x=BW[j]
                            y=BW[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(BA):
                            x=BA[j]
                            y=BA[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(BP):
                            x=BP[j]
                            y=BP[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                            j=j+2
                        j=0
                        while j<len(BC):
                            x=BC[j]
                            y=BC[j+1]
                            Sa=((x2-x)**2+(y2-y)**2)**0.5
                            if Sa<=RangeCE+1:
                                BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                            j=j+2
                        break
                jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(BW):
                    x2=BW[jj]
                    y2=BW[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if BWHP[int(jj/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(BSH):
                                x=BSH[j]
                                y=BSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BW):
                                x=BW[j]
                                y=BW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BA):
                                x=BA[j]
                                y=BA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BP):
                                x=BP[j]
                                y=BP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BC):
                                x=BC[j]
                                y=BC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2 
            if udar==0:
                jj=0
                while jj!=len(BA):
                    x2=BA[jj]
                    y2=BA[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if BAHP[int(jj/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(BSH):
                                x=BSH[j]
                                y=BSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BW):
                                x=BW[j]
                                y=BW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BA):
                                x=BA[j]
                                y=BA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BP):
                                x=BP[j]
                                y=BP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BC):
                                x=BC[j]
                                y=BC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(BP):
                    x2=BP[jj]
                    y2=BP[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if BPHP[int(jj/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(BSH):
                                x=BSH[j]
                                y=BSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BW):
                                x=BW[j]
                                y=BW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BA):
                                x=BA[j]
                                y=BA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BP):
                                x=BP[j]
                                y=BP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BC):
                                x=BC[j]
                                y=BC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
            if udar==0:
                jj=0
                while jj!=len(BC):
                    x2=BC[jj]
                    y2=BC[jj+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeC**2+1:
                        if BCHP[int(jj/2)]>0:
                            udar=1
                            # все в радиусе от цели получают урон
                            j=0
                            while j<len(BSH):
                                x=BSH[j]
                                y=BSH[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BSHHP[int(j/2)]=BSHHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BW):
                                x=BW[j]
                                y=BW[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BWHP[int(j/2)]=BWHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BA):
                                x=BA[j]
                                y=BA[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BAHP[int(j/2)]=BAHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BP):
                                x=BP[j]
                                y=BP[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BPHP[int(j/2)]=BPHP[int(j/2)]-DamageC
                                j=j+2
                            j=0
                            while j<len(BC):
                                x=BC[j]
                                y=BC[j+1]
                                Sa=((x2-x)**2+(y2-y)**2)**0.5
                                if Sa<=RangeCE+1:
                                    BCHP[int(j/2)]=BCHP[int(j/2)]-DamageC
                                j=j+2
                            break
                    jj=jj+2
        if RCReload[int(i/2)]!=ReloadC:
            RCReload[int(i/2)]=RCReload[int(i/2)]+1
        if udar==1:
            RCReload[int(i/2)]=0
        i=i+2

    
###################################################################################

def HealP():
    global BWHP, BAHP, RWHP, RAHP, BW, RW, BA, RA, BP, RP, PHP, BPHP, RPHP
    i=0
    while i!=len(BP):
        j=0
        udar=0
        x1=BP[i]
        y1=BP[i+1]
        if BPReload[int(i/2)]==ReloadP:
            while j!=len(BSH):
                x2=BSH[j]
                y2=BSH[j+1]
                if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                    if BSHHP[int(j/2)]<SHHP:
                        BSHHP[int(j/2)]=BSHHP[int(j/2)]+HealthP
                        udar=1
                        break
                j=j+2
            if udar==0:
                j=0
                while j!=len(BW):
                    x2=BW[j]
                    y2=BW[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                        if BWHP[int(j/2)]<WHP:
                            BWHP[int(j/2)]=BWHP[int(j/2)]+HealthP
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BA):
                    x2=BA[j]
                    y2=BA[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                        if BAHP[int(j/2)]<AHP:
                            BAHP[int(j/2)]=BAHP[int(j/2)]+HealthP
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BP):
                    x2=BP[j]
                    y2=BP[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                        if BPHP[int(j/2)]<PHP:
                            BPHP[int(j/2)]=BPHP[int(j/2)]+HealthP
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BC):
                    x2=BC[j]
                    y2=BC[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                        if BCHP[int(j/2)]<CHP:
                            BCHP[int(j/2)]=BCHP[int(j/2)]+HealthP
                            udar=1
                            break
                    j=j+2
        if BPReload[int(i/2)]!=ReloadP:
            BPReload[int(i/2)]=BPReload[int(i/2)]+1
        if udar==1:
            BPReload[int(i/2)]=0
        i=i+2
    i=0
    while i!=len(RP):
        j=0
        udar=0
        x1=RP[i]
        y1=RP[i+1]
        if RPReload[int(i/2)]==ReloadP:
            while j!=len(RSH):
                x2=RSH[j]
                y2=RSH[j+1]
                if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                    if RSHHP[int(j/2)]<SHHP:
                        RSHHP[int(j/2)]=RSHHP[int(j/2)]+HealthP
                        udar=1
                        break
                j=j+2
            if udar==0:
                j=0
                while j!=len(RW):
                    x2=RW[j]
                    y2=RW[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                        if RWHP[int(j/2)]<WHP:
                            RWHP[int(j/2)]=RWHP[int(j/2)]+HealthP
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RA):
                    x2=RA[j]
                    y2=RA[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                        if RAHP[int(j/2)]<AHP:
                            RAHP[int(j/2)]=RAHP[int(j/2)]+HealthP
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RP):
                    x2=RP[j]
                    y2=RP[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                        if RPHP[int(j/2)]<PHP:
                            RPHP[int(j/2)]=RPHP[int(j/2)]+HealthP
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RC):
                    x2=RC[j]
                    y2=RC[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeP**2+1:
                        if RCHP[int(j/2)]<CHP:
                            RCHP[int(j/2)]=RCHP[int(j/2)]+HealthP
                            udar=1
                            break
                    j=j+2
        if RPReload[int(i/2)]!=ReloadP:
            RPReload[int(i/2)]=RPReload[int(i/2)]+1
        if udar==1:
            RPReload[int(i/2)]=0
        i=i+2


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
            if udar==0:
                j=0
                while j!=len(RP):
                    if BSH[i]==RP[j] and BSH[i+1]==RP[j+1]:
                        if RPHP[int(j/2)]>0:
                            RPHP[int(j/2)]=RPHP[int(j/2)]-DamageSH
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RC):
                    if BSH[i]==RC[j] and BSH[i+1]==RC[j+1]:
                        if RCHP[int(j/2)]>0:
                            RCHP[int(j/2)]=RCHP[int(j/2)]-DamageSH
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
            if udar==0:
                j=0
                while j!=len(BP):
                    if RSH[i]==BP[j] and RSH[i+1]==BP[j+1]:
                        if BPHP[int(j/2)]>0:
                            BPHP[int(j/2)]=BPHP[int(j/2)]-DamageSH
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BC):
                    if RSH[i]==BC[j] and RSH[i+1]==BC[j+1]:
                        if BCHP[int(j/2)]>0:
                            BCHP[int(j/2)]=BCHP[int(j/2)]-DamageSH
                            udar=1
                            break
                    j=j+2
        if RSHReload[int(i/2)]!=ReloadSH:
            RSHReload[int(i/2)]=RSHReload[int(i/2)]+1
        if udar==1:
            RSHReload[int(i/2)]=0
        i=i+2


def AttackA():
    global BWHP, BAHP, RWHP, RAHP, BW, RW, BA, RA, BP, RP
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
            if udar==0:
                j=0
                while j!=len(RP):
                    x2=RP[j]
                    y2=RP[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                        if RPHP[int(j/2)]>0:
                            RPHP[int(j/2)]=RPHP[int(j/2)]-DamageA
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RC):
                    x2=RC[j]
                    y2=RC[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                        if RCHP[int(j/2)]>0:
                            RCHP[int(j/2)]=RCHP[int(j/2)]-DamageA
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
            if udar==0:
                j=0
                while j!=len(BP):
                    x2=BP[j]
                    y2=BP[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                        if BPHP[int(j/2)]>0:
                            BPHP[int(j/2)]=BPHP[int(j/2)]-DamageA
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BC):
                    x2=BC[j]
                    y2=BC[j+1]
                    if (x2-x1)**2+(y2-y1)**2<=RangeA**2+1:
                        if BCHP[int(j/2)]>0:
                            BCHP[int(j/2)]=BCHP[int(j/2)]-DamageA
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
                            Bonus=-0.05 
                            for o in range(0, len(BW), 2):
                                if BW[i]==BW[o] and BW[i+1]==BW[o+1]:
                                    Bonus=Bonus+0.05 
                            RWHP[int(j/2)]=RWHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RA):
                    if BW[i]==RA[j] and BW[i+1]==RA[j+1]:
                        if RAHP[int(j/2)]>0:
                            Bonus=-0.05 
                            for o in range(0, len(BW), 2):
                                if BW[i]==BW[o] and BW[i+1]==BW[o+1]:
                                    Bonus=Bonus+0.05 
                            RAHP[int(j/2)]=RAHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RP):
                    if BW[i]==RP[j] and BW[i+1]==RP[j+1]:
                        if RPHP[int(j/2)]>0:
                            Bonus=-0.05 
                            for o in range(0, len(BW), 2):
                                if BW[i]==BW[o] and BW[i+1]==BW[o+1]:
                                    Bonus=Bonus+0.05 
                            RPHP[int(j/2)]=RPHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(RC):
                    if BW[i]==RC[j] and BW[i+1]==RC[j+1]:
                        if RCHP[int(j/2)]>0:
                            Bonus=-0.05 
                            for o in range(0, len(BW), 2):
                                if BW[i]==BW[o] and BW[i+1]==BW[o+1]:
                                    Bonus=Bonus+0.05 
                            RCHP[int(j/2)]=RCHP[int(j/2)]-(DamageW+DamageW*Bonus)
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
                            Bonus=-0.05 
                            for o in range(0, len(RW), 2):
                                if RW[i]==RW[o] and RW[i+1]==RW[o+1]:
                                    Bonus=Bonus+0.05 
                            BWHP[int(j/2)]=BWHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BA):
                    if RW[i]==BA[j] and RW[i+1]==BA[j+1]:
                        if BAHP[int(j/2)]>0:
                            Bonus=-0.05 
                            for o in range(0, len(RW), 2):
                                if RW[i]==RW[o] and RW[i+1]==RW[o+1]:
                                    Bonus=Bonus+0.05 
                            BAHP[int(j/2)]=BAHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BP):
                    if RW[i]==BP[j] and RW[i+1]==BP[j+1]:
                        if BPHP[int(j/2)]>0:
                            Bonus=-0.05 
                            for o in range(0, len(RW), 2):
                                if RW[i]==RW[o] and RW[i+1]==RW[o+1]:
                                    Bonus=Bonus+0.05 
                            BPHP[int(j/2)]=BPHP[int(j/2)]-(DamageW+DamageW*Bonus)
                            udar=1
                            break
                    j=j+2
            if udar==0:
                j=0
                while j!=len(BC):
                    if RW[i]==BC[j] and RW[i+1]==BC[j+1]:
                        if BCHP[int(j/2)]>0:
                            Bonus=-0.05 
                            for o in range(0, len(RW), 2):
                                if RW[i]==RW[o] and RW[i+1]==RW[o+1]:
                                    Bonus=Bonus+0.05 
                            BCHP[int(j/2)]=BCHP[int(j/2)]-(DamageW+DamageW*Bonus)
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
    while i<len(BPHP):
        if BPHP[i]<=0:
            del BPHP[i]
            del BP[i*2]
            del BP[i*2]
            del BPReload[i]
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
    while i<len(BCHP):
        if BCHP[i]<=0:
            del BCHP[i]
            del BC[i*2]
            del BC[i*2]
            del BCReload[i]
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
    while i<len(RPHP):
        if RPHP[i]<=0:
            del RPHP[i]
            del RP[i*2]
            del RP[i*2]
            del RPReload[i]
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
    i=0
    while i<len(RCHP):
        if RCHP[i]<=0:
            del RCHP[i]
            del RC[i*2]
            del RC[i*2]
            del RCReload[i]
            i=i-1
        i=i+1
   
def CheckWinner():
    global BW, BA, BSH, BA, RW, RA, RSH, RP, gameover, mes, clr
    if len(RW)+len(RA)+len(RSH)+len(RP)+len(RC)==0 and len(BW)+len(BA)+len(BSH)+len(BP)+len(BC)==0:
        mes=('tie!')
        clr=(100, 100, 100)
        gameover=True
    elif len(BW)+len(BA)+len(BSH)+len(BP)+len(BC)==0:
        mes=('RED wins!')
        clr=RED
        sound5.play()
        gameover=True
    elif len(RW)+len(RA)+len(RSH)+len(RP)+len(RC)==0:
        mes=('BLUE wins!')
        clr=BLUE
        sound3.play()
        gameover=True
    elif len(BW)+len(BA)+len(BSH)+len(BC)==0 and len(RW)+len(RA)+len(RSH)+len(RC)==0:
        if len(BP)>len(RP):
            mes=('BLUE wins!')
            clr=BLUE
            sound3.play()
            gameover=True
        if len(RP)>len(BP):
            mes=('RED wins!')
            clr=RED
            sound5.play()
            gameover=True
        if len(RP)==len(BP):
            mes=('tie!')
            clr=(100, 100, 100)
            gameover=True

# здесь происходит инициация, создание объектов и др.
pygame.init()
pygame.display.set_caption('Ancient Battles Simulator')
pygame.mixer.pre_init(44100, 16, 2, 4096)
img = pygame.image.load('images\icon8.ico')
pygame.display.set_icon(img)
sc=pygame.display.set_mode(Win)
surf = pygame.Surface(Win)
surf.fill((0, 0, 0))
clock = pygame.time.Clock()
sound1=pygame.mixer.Sound('music\horn.ogg')
sound2=pygame.mixer.Sound('music\swordsbattle.ogg')
sound3=pygame.mixer.Sound('music\ForWinner.ogg')
sound4=pygame.mixer.Sound('music\screams in battle.ogg')
sound5=pygame.mixer.Sound('music\ForLooser.ogg')
pygame.mixer.music.load('music\General Theme.ogg')
pygame.mixer.music.play()
# если надо до цикла отобразить объекты на экране
pygame.display.update()


# главный цикл
while True:
    if gameover==True:
        sound2.stop()
        sound4.stop()
        pygame.quit()
        exit()
        final=pygame.font.Font(None, 72)
        text7 = final.render(mes, 1, clr)
        sc.blit(text7, (430, HEIGHT/2))  
    if gameover==False:
        gameover=False
    # задержка
    clock.tick(FPS)
    if start==False:
        u=pygame.mixer.music.get_busy()
        if u==False:
            pygame.mixer.music.load('music\General Theme.ogg')
            pygame.mixer.music.play()
    if start==True:
        pygame.mixer.music.stop()
        if gameover==False:
            sc.blit(surf, (0, 0))
            MoveBW()
            MoveRW()
            MoveBA()
            MoveRA()
            MoveBSH()
            MoveRSH()
            MoveBC()
            MoveRC()
            MoveBP()
            MoveRP()
            if spl==0:# spl - sound_play
                spl=1
                sound2.play()
                sound4.play()
            AttackW()
            AttackA()
            AttackSH()
            AttackC()
            HealP()
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
                for i in range(len(RW)):
                    RW[i]=int(RW[i])
                for i in range(len(RA)):
                    RA[i]=int(RA[i])
                for i in range(len(RSH)):
                    RSH[i]=int(RSH[i])
                for i in range(len(RP)):
                    RP[i]=int(RP[i])
                for i in range(len(RC)):
                    RC[i]=int(RC[i])
                print(RW)
                print(RA)
                print(RSH)
                print(RP)
                print(RC)
                gameover=True
                break
                sound1.play()
                start=True
            if i.key == pygame.K_a:
                admin=[]
                admin.append('a')
            if i.key == pygame.K_d:
                admin.append('d')
            if i.key == pygame.K_m:
                admin.append('m')
            if i.key == pygame.K_i:
                admin.append('i')
            if i.key == pygame.K_n:
                admin.append('n')
                if admin==['a', 'd', 'm', 'i', 'n']:
                    goldB=goldB+10000
        if gameover==False:    
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
                        if fighter=='Priests':
                            if goldB-costP>=0:
                                a=pygame.draw.rect(sc, (BLUEP), (x-razmer/2, y-razmer/2, razmer, razmer))
                                BP.append(x-razmer/2)
                                BP.append(y-razmer/2)
                                BPHP.append(PHP)
                                BPReload.append(ReloadP)
                                goldB=goldB-costP
                        if fighter=='Catapults':
                            if goldB-costC>=0:
                                a=pygame.draw.rect(sc, (BLUEC), (x-razmerC/2, y-razmerC/2, razmerC, razmerC))
                                BC.append(x-razmerC/2)
                                BC.append(y-razmerC/2)
                                BCHP.append(CHP)
                                BCReload.append(ReloadC)
                                goldB=goldB-costC
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
                        if fighter=='Priests':
                            if goldR-costP>=0:
                                a=pygame.draw.rect(sc, (REDP), (x-razmer/2, y-razmer/2, razmer, razmer))
                                RP.append(x-razmer/2)
                                RP.append(y-razmer/2)
                                RPHP.append(PHP)
                                RPReload.append(ReloadP)
                                goldR=goldR-costP
                        if fighter=='Catapults':
                            if goldR-costC>=0:
                                a=pygame.draw.rect(sc, (REDC), (x-razmerC/2, y-razmerC/2, razmerC, razmerC))
                                RC.append(x-razmerC/2)
                                RC.append(y-razmerC/2)
                                RCHP.append(CHP)
                                RCReload.append(ReloadC)
                                goldR=goldR-costC
                            
                if 0<x<80 and 0<y<100:
                    fighter='Warriors'
                if 80<x<160 and 0<y<100:
                    fighter='Archers'
                if 160<x<240 and 0<y<100:
                    fighter='Shields'
                if 240<x<320 and 0<y<100:
                    fighter='Priests'
                if 320<x<400 and 0<y<100:
                    fighter='Catapults'
                
 
    # --------
    # изменение объектов и многое др.
    # --------
    pygame.draw.line(sc, WHITE, [0, 100], [WIDTH, 100], 3)
    pygame.draw.rect(sc, WHITE, (0, 0, 80, 100))
    
    pygame.draw.rect(sc, WHITE, (80, 0, 80, 100))
    pygame.draw.line(sc, BLACK, [80, 100], [80, 0], 2)
    
    pygame.draw.rect(sc, WHITE, (160, 0, 80, 100))
    pygame.draw.line(sc, BLACK, [160, 100], [160, 0], 2)
    
    pygame.draw.rect(sc, WHITE, (240, 0, 80, 100))
    pygame.draw.line(sc, BLACK, [240, 100], [240, 0], 2)
    
    pygame.draw.rect(sc, WHITE, (320, 0, 80, 100))
    pygame.draw.line(sc, BLACK, [320, 100], [320, 0], 2)
    
    lenBW=str(int(len(BW)/2)+int(len(BA)/2)+int(len(BSH)/2)+int(len(BP)/2)+int(len(BC)/2))
    lenRW=str(int(len(RW)/2)+int(len(RA)/2)+int(len(RSH)/2)+int(len(RP)/2)+int(len(RC)/2))
    f1 = pygame.font.Font(None, 34)
    text1 = f1.render('Blue:', 0, BLUE)
    text1b = f1.render(lenBW, 0, BLUE)
    text2 = f1.render("Red:", 0, RED)
    text2r = f1.render(lenRW, 0, RED)
    f3 = pygame.font.Font(None, 24)
    W = f3.render("Warriors", 0, BLACK)
    A = f3.render("Archers", 0, BLACK)
    SH = f3.render("Shields", 0, BLACK)
    P = f3.render("Priests", 0, BLACK)
    C = f3.render("Catapults", 0, BLACK)
    text5 = f3.render(str(goldB), 0, GOLD)
    text6 = f3.render(str(goldR), 0, GOLD)
    
    
    sc.blit(text1, (800, 20))
    sc.blit(text2, (800, 60))
    sc.blit(text1b, (950, 20))
    sc.blit(text2r, (950, 60))
    sc.blit(W, (8, 40))
    sc.blit(A, (88, 40))
    sc.blit(SH, (169, 40))
    sc.blit(P, (252, 40))
    sc.blit(C, (321, 40))
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
    i=0
    while i<len(BPMove):
        pygame.draw.rect(sc, (BLUEP), (BPMove[i]-razmer/2, BPMove[i+1]-razmer/2, razmer, razmer))
        i=i+2
    BPMove=[]
    i=0
    while i<len(RPMove):
        pygame.draw.rect(sc, (REDP), (RPMove[i]-razmer/2, RPMove[i+1]-razmer/2, razmer, razmer))
        i=i+2
    RPMove=[]
    i=0
    while i<len(BCMove):
        pygame.draw.rect(sc, (BLUEC), (BCMove[i]-razmerC/2, BCMove[i+1]-razmerC/2, razmerC, razmerC))
        i=i+2
    BCMove=[]
    i=0
    while i<len(RCMove):
        pygame.draw.rect(sc, (REDC), (RCMove[i]-razmerC/2, RCMove[i+1]-razmerC/2, razmerC, razmerC))
        i=i+2
    RCMove=[]
    # обновление экрана
    pygame.display.update()






