f=open('hi.txt','w+')

L=[]
for i in range(0,3):
    L.append(input())
f.writelines(L)
f.seek(0)
p=f.read()
print(p)
f.close()
