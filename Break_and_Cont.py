#example 1
for i in range(1,101,1):
    print(i,end=" ")
    if(i==50):
        break
    else:
        print("abra ka dabra")
print("thankyou")

# example 2- printing table of 5
for i in range(12):
    if(i==10):
        break
    print("5 x",i+1,"=",5*(i+1))
print("loop se bahar nikal gaya")