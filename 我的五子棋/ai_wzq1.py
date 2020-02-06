def ai(qp1,x11,y11):
    import itertools as its
    sd=3  #深度
    X=2 #当前局面得分最高的前几个棋子继续算分
    word=''
    for i in range(X):
        word+=str(i)
    l2=999
    xyb={}
    f999=['22223','22232','22322','23222','32222']
    f330=['311112','211113','2113110','2131110','0111312','0113112','0131112']
    f100=['032220','023220','022320','022230','031110','011130','011310','013110']
    f40=['03220','02320','02230','032020','023020','022030','030220','020320','020230','132220','123220','122320','122230','032221','023221','022321','022231','01130','03110','01310','0311120','0211130']
    f5=['0320','03020','0230','02030']
    f9991=['11113','11131','11311','13111','31111']
    f3301=['322221','122223','1223220','1232220','0222321','0223221','0232221']
    f1001=['031110','013110','011310','011130','032220','022230','022320','023220','0322210','0122230']
    f401=['03110','01310','01130','031010','013010','011030','030110','010310','010130','231110','213110','211310','211130','031112','013112','011312','011132','02230','03220','02320']
    f51=['0310','03010','0130','01030']
    qpp=qp1
    pp={'':0}
    for i3 in range(sd):
        r=its.product(word,repeat=i3)
        for i4 in r:
            q=''.join(i4)
            for i5 in range(1,i3):
                for i6 in range(len(qpp)):
                    if qpp[i6][0]==xyb[q[0:i5]][0] and qpp[i6][1]==xyb[q[0:i5]][1]:
                        if i5%2==1:
                            qpp[i6][2]=2
                        else:
                            qpp[i6][2]=1
            fs,zb=[],[]
            for i in range(len(qp1)):
                    if qpp[i][2]==0:
                        f=0
                        qpp[i][2]=3
                        x,y=qpp[i][0],qpp[i][1]
                        h=z=zx=yx=''
                        lb=[]
                        qw=0
                        for z1 in range(-7,8):
                            for i1 in range(len(qpp)):
                                if qpp[i1][0]>=x-5 and qpp[i1][0]<=x+5 and qpp[i1][1]==y and qw==0:#横向
                                    h+=str(qpp[i1][2])
                                if qpp[i1][1]>=y-5 and qpp[i1][1]<=y+5 and qpp[i1][0]==x and qw==0:#纵向
                                    z+=str(qpp[i1][2])
                                if qpp[i1][0]==x+z1 and qpp[i1][1]==y-z1:#斜向（左下右上）
                                    zx+=str(qpp[i1][2])
                                if qpp[i1][0]==x+z1 and qpp[i1][1]==y+z1:#斜向（左上右下）
                                    yx+=str(qpp[i1][2])
                            qw=1
                        lb.append(h)
                        lb.append(z)
                        lb.append(zx)
                        lb.append(yx)
                        if i3%2==0:
                            for i2 in lb:
                                for z in f999:
                                    if z in i2:
                                        f+=999
                                for z in f330:
                                    if z in i2:
                                        f+=330
                                for z in f100:
                                    if z in i2:
                                        f+=100
                                for z in f40:
                                    if z in i2:
                                        f+=40
                                for z in f5:
                                    if z in i2:
                                        f+=5
                        else:
                            for i2 in lb:
                                for z in f999:
                                    if z in i2:
                                        f+=999
                                for z in f330:
                                    if z in i2:
                                        f+=330
                                for z in f100:
                                    if z in i2:
                                        f+=100
                                for z in f40:
                                    if z in i2:
                                        f+=40
                                for z in f5:
                                    if z in i2:
                                        f+=5
                        fs.append(f)
                        zb.append([x,y])
                        qpp[i][2]=0
            
            p=0
            p1,p2=999,999
            for ii in range(X):
                l=0
                p=0
                p1=999              
                for i in range(len(fs)):
                    if fs[i]==p and abs(zb[i][0]-x11)+abs(zb[i][1]-y11)<=p1 or fs[i]>p:
                        fs[l]=p
                        p=fs[i]
                        p1=abs(zb[i][0]-x11)+abs(zb[i][1]-y11)
                        l=i
                xyb[q+str(ii)]=[zb[l][0],zb[l][1]]
                if i3%2==0:
                    pp[q+str(ii)]=pp[q]+p
                else:
                    pp[q+str(ii)]=pp[q]-p
                del fs[l]
                del zb[l]
        r=its.product(word,repeat=i3)
        for i4 in r:
            q=''.join(i4)
            for i5 in range(1,i3):
                for i6 in range(len(qpp)):
                    if qpp[i6][0]==xyb[q[0:i5]][0] and qpp[i6][1]==xyb[q[0:i5]][1]:
                        qpp[i6][2]=0
                        
    
    l,d=[],[]
    for i2 in range(sd):
        z=sd-i2-1
        r1=its.product(word,repeat=z)
        for i3 in r1:
            q=''.join(i3)
            p=0
            for i4 in range(X):
                if z%2==1:
                    if pp[q+str(i4)]>=p:
                        p=pp[q+str(i4)]
                        pp[q]=pp[q+str(i4)]
                else:
                    if pp[q+str(i4)]<=p:
                        p=pp[q+str(i4)]
                        pp[q]=pp[q+str(i4)]
    p=0
    l=0
    for i in range(X):
        if pp[str(i)]>=p:
            p=pp[str(i)]
            l=i
    x,y=xyb[str(l)][0],xyb[str(l)][1]
    return x,y,p   
