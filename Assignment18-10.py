x={'C':92,'Java':66,'Python':85}
a=x.values()
a=sorted(a)
print(a)
print(a[0])
for i in x:
    if x[i]==a[0]:
        print(i)
