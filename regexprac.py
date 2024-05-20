import re
f=open('regex.txt','w+')
text="Hi my name is Aarav and my phone number is 7977183376 and my email id is aaravmody@gmail.com"
f.write(text)
f.seek(0)
r=f.readlines()
print(r)
pattern="\d{10}"
match=re.findall(pattern,text)
print(match)
f.close()
