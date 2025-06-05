#tuples in python 
tup=(1, )
print(type(tup),tup)

#accessing tuples items
tup2=("abhijeet",19,"eligible",True)
print(tup2[0])
print(tup2[1])
print(tup2[2])
print(tup2[3])
print(type(tup2))

#check for an item
tup3=(341,342,343,345)
if 342 in tup3:
    print("yes 342 is in the tuple")

#printing elements in a particular range
tup4=("red","blue","green","violet","yellow","pink","magenta","grey")
print(tup4[1:5]) #positive indexing
print(tup4[-7:-2]) #negative indexing

#printing alternate values
tup5=("a","b","c","d","e","f","g","h","i")
print(tup5[::2])
print(tup5[-8:-1:2])