import string
f=open('hi.txt','w+')
r=open('bye.txt','w+')
L=[]
for i in range(0,3):
    L.append(input())
f.writelines(L)
L.sort()
r.writelines(L)
f.seek(0)
print(f.read())
r.seek(0)
print(r.read())
f.close()
