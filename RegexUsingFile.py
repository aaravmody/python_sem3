#text in my file is Hi my name is Aarav and my phone number is 7977183376 and my email id is aaravmody@gmail.com and selmonbhoi@edu.com

import re
f=open("regex.txt","r")
s=f.read()
print(s)
f.seek(0)
pattern="([a-zA-z]\w+)@[a-zA-z]+\.com"
match1=re.findall(pattern,s)
print("email name is: ",match1) #matches email name so returns aaravmody and selmonbhoi

pattern2="\d{10}"
match2=re.findall(pattern2,s)
print("phone number is: ",match2)

