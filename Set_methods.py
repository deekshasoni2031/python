#set methods in python
#1.update
s1={1,2,3,4}
s2={5,6,7,8}
s1.update(s2)

#2.union
print(s1.union(s2))

#3.intersection and intersection_update
s3={"A","B","C","D","E"}
s4={"A","C","D","R","F"}
s=s3.intersection(s4)
print(s)

s3.intersection_update(s4)