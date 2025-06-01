# function arguments in python 
# 1. default argument-
# example 1
def name(fname,mname="john",lname="whatson"):
    print("hello",fname,mname,lname)
    name("amy")

# example 2
'''def average(a=9,b=1):
    print("average is",(a+b)/2)

average(b=9)'''

# 2. keyword arguments-
# example 1
def sum(a=10,b=30):
    print("sum of a and b is:",a+b)

sum(a=10,b=20)

# 3. required arguments-
def average(a=9,b=1):
    print("average is:",(a+b)/2)
    average(5,6)
    

