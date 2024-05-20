import random as r

L=[]
for i in range(0,10000):
    L.append(str(r.randint(1,1000)))

f=open("hi.txt","w+")
f.writelines(L)
print("done")

f.close()
L.sort()
p=open("sort.txt","w+")
p.writelines(L)
print("done 2")
p.close()
