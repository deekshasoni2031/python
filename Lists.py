lst1=[3,5,6]
print(lst1)
print(type(lst1))
print(lst1[0])
print(lst1[1])
print(lst1[2])

# list with combination of data types
marks=[3,5,6,"deeksha",True]
print(marks)

# Accessing list items
colors=["red","blue","green","yellow"]
print(colors[0])  #positive indexing 
print(colors[-1])  #negative indexing

# Check whether an item is present in list or not
colors2=["red","blue","green","yellow"]
if "red" in colors2:
    print("red is present in colours2")
else:
    print("red is not present in colours2")