#manipulating tuples
tup1=("spain","italy","india","norway","qatar")
temp=list(tup1)
temp.append("russia") #add item
temp.pop(3) #delete item
temp[2]="finland" #chande item
tup1=tuple(temp)
print(tup1)

#concatenate two tuples= Simply by changing them into list
countries1=("a","b","c","d") #list 1
countries2=("e","f","g","h") #list 2
south_east_asia=countries1+countries2
print(south_east_asia)

# to count no. of elements
tup2=(1,2,3,4,3,5,6,2,2,2)
res=tup2.count(3)
print("count of 3 in tuple is: ",res)

# index()method
res1=tup2.index(2)
print("first occurence of 3 is",res1)
print=tup2.index(3,4,8)

#NOTE
'''ONCE WE HAVE CONVERTED A TUPLE INTO A LIST THEN WE CAN USE ALL THE METHODS OF LIST ON THEM 
& THEN AGAIN CONVERT IT BACK TO TUPLE '''