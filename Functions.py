# Functions in python
# 1. Built-in functions = min(),len(),max(),sum(),type(),range(),dict(),list(),tuple(),
# set(),print()
# 2. User-define functions = these functions are created by the user as per their needs

#example 1
def calculatemean(a,b): #function name 
    mean = (int(a*b)/int(a+b)) #function body
    print(int(mean))

a=2
b=2
c=34
d=56
calculatemean(a,b) #function call

#example 2
def isgreater(a,b):
    if (a>b):
        print("a is a greater number.")
    elif (b>a):
        print("b is a greater number.")
    else:
        print("not a valid expression.")

isgreater(a,b)
isgreater(c,d)
