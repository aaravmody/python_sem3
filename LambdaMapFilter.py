eg=lambda x:x+2; #Add 2
print(eg(4))

L=[1,3,5,7,9]
eg2=list(map(eg,L)) #Add 2 to all values of a list
print(eg2)

g5=lambda x:x>5
eg3=list(filter(g5,eg2)) #Filter >5 values from the new list
print(eg3)
