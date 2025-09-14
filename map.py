def cube(x):
    return x*x*x
print(cube(2))

l=[1,2,3,4,5]
newl = list(map(cube,l))
print(newl)