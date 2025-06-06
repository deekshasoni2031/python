# doc strings in python
def square(n):
    "takes in a number n, returns the square of n" # doc string
    print(n**2)
square(5)
print(square.__doc__)   # used to display doc string 