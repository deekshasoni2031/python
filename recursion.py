# Recursiopn in python
# factorial 
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)  # here a function is called under itself

print(factorial(3))
print(factorial(4))
print(factorial(5))