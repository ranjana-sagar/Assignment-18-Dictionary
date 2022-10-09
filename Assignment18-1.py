b={}
b=b.fromkeys((1,2,3,4,5))
x=input("Enter your name,age,mobilno,gender,height:")
x=x.split(',')
i=0
for k in b:
    b[k]=eval(x[i])
    i+=1
print(b)    
