#def double(x):
    #return x*2


cube= lambda x:x*x*x
double = lambda x:x*2
print(double(5))
print(cube(2))


def apple(fix,value):
    return 6+fix(value)

print(apple(lambda x:x*x*x,2))