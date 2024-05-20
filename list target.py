L=[10,20,40,60,80]
tar=int(input("Enter target"))
s=set()

for i in L:
    for j in L:
        if i+j==tar:
            s.add(tuple((i,j)))
        for k in L:
            if i+j+k==tar:
                s.add(tuple((i,j,k)))

print(list(set(s)))
            
