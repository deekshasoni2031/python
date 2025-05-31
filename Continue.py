# Continue statement in python
# example 1
for i in range(12):
    if(i==10): # this will skip the iteration for 10 in the output
        print("skip the iteration")
        continue
    print("5x",i,"=",5*i)

# example 2
for i in[2,3,4,6,8,0]:
    if(i%2!=0):
        continue
    print(i)