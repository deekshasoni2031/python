# Do while loop in python
'''Python does not have a built-in do-while loop construct like some other programming languages.
However, its functionality can be emulated using a while loop with a break statement or 
by ensuring the loop body executes at least once before the condition is checked'''
# example 1 -
while True:
    number = int (input("enter a positive number: "))
    print(number)
    if not number > 0:
        break