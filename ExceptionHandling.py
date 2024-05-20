a=int(input("A: "))
b=int(input("B: "))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("cant divide by 0")

L=[1,2,3]
try:
    print(L[5])
except IndexError:
    print("Index out of bounds")

try:
    f=open("oye.txt","r")
except FileNotFoundError:
    print("File nai mila")

try:
    'r'+23
except TypeError:
    print("yeh add nai ho sakte");


#User defined exceptions

class ageError(Exception):
    def _init_(self,message):
        self.message=message

try:
    num=int(input("Enter age: "))
    if num<0:
        raise ageError()
except ageError:
    print("Enter valid age")
    
