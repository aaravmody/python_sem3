#Count no of lower,upper,spaces in a sentence

strinput=input("Enter your string")
low=0
cap=0
sp=0
for i in strinput:
    if i.islower():
        low+=1
    elif i.isupper():
        cap+=1
    elif i==" ":
        sp+=1

print(f"Number of low is {low} \n Cap is {cap} \n Spaces are {sp}")
