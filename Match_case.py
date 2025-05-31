# Match-case statements in python 
x = int(input("enter the value of x: "))
# x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
    case 4:
        print("if x is 4")
    case _ if x != 90:   # Default case 
        print(x,"is not 90")