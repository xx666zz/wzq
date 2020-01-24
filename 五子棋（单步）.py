import pygame, sys
from pygame.locals import *
from math import pi
from ai_wzq import ai
import re
from easygui import msgbox
GREEN = ( 0, 255, 0)
WHITE = (255, 255, 255)
def qpsc():#棋盘生成
    global qp,screen,yydd,sy,ys
    qp=[]
    sy=0#输赢
    yydd=[]
    ys = 1#颜色
    for x in range(20):
        for y in range(14):
            qp.append([x,y,0])
    pygame.init()# 初始化pygame
    screen = pygame.display.set_mode((800,600))# 设置窗口的大小，单位为像素
    pygame.display.set_caption('game')# 设置窗口标题
    e = 0
    f = 0
    a = 1
    b = 25
    c =800
    d = 25
    while e < 15:
        pygame.draw.aaline(screen, GREEN, [a, b],[c, d],True)
        e+=1
        b+=40
        d+=40
    a = 25
    b = 1
    c = 25
    d = 600
    while f < 20:
        pygame.draw.aaline(screen, GREEN, [a, b],[c, d],True)
        a+= 40
        c+=40
        f+=1
#################################################
def pdzb(x,y):#判断（圆心)坐标
    global yydd#已有的点
    global qp,ys,sy
    ymy=False#有没有
    e = 0
    f = 0
    b = 25
    while e < 15:
        if y >= b -20 and y < b +20:
            yxy=b
            break
        e+=1
        b+=40
    a = 25
    while f < 20:
        if x >= a -20 and x < a +20:
            yxx=a#圆心x
            break
        a+= 40
        f+=1
    ydzb=(yxx,yxy)#圆的坐标
    for i in yydd:
        if i == ydzb:
            ymy=True#有没有
            break
    if ymy != True:
        djg = ((yxx-25)/40+1)+((yxy-25)/40*20+1)-1
        x=(yxx-25)/40
        y=(yxy-25)/40
        for i in range(len(qp)):
            if qp[i][0]==x and qp[i][1]==y:
                if ys%2==1:
                    qp[i][2]=1
                else:
                    qp[i][2]=2
        yydd.append(ydzb)
        j1,j2=0,0
        if ys%2==1:
            s=1
        else:
            s=2
        j3,j4=0,0
        for z in range(-5,5):
            for i in range(len(qp)):            
                if qp[i][0]>=x-4 and qp[i][0]<=x+4 and qp[i][1]==y:#横向
                    if qp[i][2]==s:
                        j1+=1
                        if j1>=5:
                            sy=1
                    else:
                        j1=0
                if qp[i][1]>=y-4 and qp[i][1]<=y+4 and qp[i][0]==x:#纵向
                    if qp[i][2]==s:
                        j2+=1
                        if j2>=5:
                            sy=1
                    else:
                        j2=0
                if qp[i][0]==x+z and qp[i][1]==y-z:#斜向（左下右上）
                    if qp[i][2]==s:
                        j3+=1
                        if j3>=5:
                            sy=1
                    else:
                        j3=0
                if qp[i][0]==x+z and qp[i][1]==y+z:#斜向（左上右下）
                    if qp[i][2]==s:
                        j4+=1
                        if j4>=5:
                            sy=1
                    
                    else:
                        j4=0
        return(yxx,yxy,x,y)
    else:
        return(0,0,0,0)
####################################

##################################
qpsc()
while True:
    for event in pygame.event.get():# 获取事件
        if event.type ==MOUSEBUTTONDOWN:
            坐标 = event.pos
            zb1,zb2 = str(坐标).split(',')
            zb1 = int(re.sub('[(]', '', zb1))
            zb2 = int(re.sub('[)]', '', zb2))
            yxx,yxy,x,y=pdzb(zb1,zb2)
            if yxx == 0:
                pass
            else:
                if ys %2 == 1:
                    pygame.draw.circle(screen, WHITE, [yxx, yxy], 15)
                    pygame.display.update()
                    if sy==1:
                        qpsc()
                        msgbox('白棋赢了！','五子棋')
                #else:
                    #pygame.draw.circle(screen,GREEN, [yxx, yxy], 15)
                    ys+=1
                    x,y,p=ai(qp,x,y)
                    print(p)
                    yxx,yxy,x,y=pdzb(40*x+25,40*y+25)
                    pygame.draw.circle(screen,GREEN, [yxx, yxy], 15)
                    pygame.display.update()
                    if sy==1:
                        qpsc()
                        msgbox('绿棋赢了！','五子棋')
                    ys+=1
            #x,y,f=ai(qp)
            #print(x,y,f)
        if event.type == QUIT:# 判断事件是否为退出事件
            pygame.quit()  # 退出pygame       
            sys.exit()# 退出系统
    pygame.display.update()# 绘制屏幕内容
