import random as r

f=open("hi.txt","w+")
print("file 1 open")


L=[]
for i in range(0,5):
    b=(str(r.randint(1,100)))
    L.append(b)
    f.write(b+'\n')
        

f.close()
print(L)
L.sort()
print(L)
p=open("sort.txt","w+")
for j in L:
    p.write(j+'\n')
print("done 2")
p.close()
