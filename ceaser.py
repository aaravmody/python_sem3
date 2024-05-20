stri="This is not encrypted"
print(stri)
new=""
for i in stri:
    if(i==" "):
        new+=i
    else:
        i=chr(ord(i)+2)
        new+=i
print(new)
