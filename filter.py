
l=[1,2,3,4,5]
def filter_function(a):
    return a>4

n_newl=(filter(filter_function,l))
print(n_newl)