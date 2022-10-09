x={1:{1:'k'},2:{8:'p'}}
x2={11:{5:'o'},12:{8:"90"}}
x3={45:{6:"hi"},56:{8:'vina'}}
d1=x.fromkeys((1,2,3))
for i in d1:
    if i==1:
        d1[i]=x
    elif i==2:
        d1[i]=x2
    elif i==3:
        d1[i]=x3
print(d1)        
