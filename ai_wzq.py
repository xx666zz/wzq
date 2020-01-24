def ai(qp1,x11,y11):
    f999=['22223','22232','22322','23222','32222']
    f330=['311112','211113','2111310','2113110','2131110','0111312','0113112','0131112','311112']
    f100=['032220','023220','022320','022230','031110','011130','011310','013110']
    f40=['03220','02320','02230','032020','023020','022030','030220','020320','020230','132220','123220','122320','122230','032221','023221','022321','022231','01130','03110','01310','031112','211130']
    f5=['0320','03020','0230','02030']
    zb=[]
    fs=[]
    for i in range(len(qp1)):
        if qp1[i][2]==0:
            qpp=qp1
            f=0
            qpp[i][2]=3
            x,y=qpp[i][0],qpp[i][1]
            h=z=zx=yx=''
            lb=[]
            for z1 in range(-7,8):
                for i1 in range(len(qpp)):
                    if qpp[i1][0]>=x-5 and qpp[i1][0]<=x+5 and qpp[i1][1]==y:#横向
                        h+=str(qpp[i1][2])
                    if qpp[i1][1]>=y-5 and qpp[i1][1]<=y+5 and qpp[i1][0]==x:#纵向
                        z+=str(qpp[i1][2])
                    if qpp[i1][0]==x+z1 and qpp[i1][1]==y-z1:#斜向（左下右上）
                        zx+=str(qpp[i1][2])
                    if qpp[i1][0]==x+z1 and qpp[i1][1]==y+z1:#斜向（左上右下）
                        yx+=str(qpp[i1][2])
            lb.append(h)
            lb.append(z)
            lb.append(zx)
            lb.append(yx)
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
    for i in range(len(fs)):
        if fs[i]==p and abs(zb[i][0]-x11)<=p1 and abs(zb[i][1]-y11)<=p2 or fs[i]>p:
            p=fs[i]
            p1=abs(zb[i][0]-x11)
            p2= abs(zb[i][1]-y11)
            l=i
    x,y=zb[l][0],zb[l][1]
    return x,y,p      
