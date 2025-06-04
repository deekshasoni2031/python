#list methods in python
#1 l.append()
l=[1,2,3,4]
l.append(7)
print(l)

#2 l.sort()
colors=["red","blue","green"]
colors.sort() #by-default sorting will be done in ascending order
print(colors)
colors.sort(reverse=True) #descending order

#3 reverse()
colors.reverse()
print(colors)

#4 index()
print(colors.index("green"))

#5 count()
l=[11,34,2,3,6,1,1]
print(l.count(1))
print(l)

#6 copy()
m=l.copy()
m[0]=0
print(l)

#7 insert()
colors.insert(1,"indigo")
print(colors)

#8 extend()
rainbow=["green","yellow","orange"]
colors.extend(rainbow)
print(colors)

#concatination of two lists
l1=["a","b","c"]
l2=[1,2,3]
print(l1+l2)
