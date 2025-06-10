# dictionaries in python
dic = {"deeksha":"human being","spoon":"object"}
print(dic)
print(dic["deeksha"])

dic2 = {344:"h",345:"w",346:"r"}
print(dic2[344])

# accessing dictionary items
# accessing single items
info = {"name":"deeksha","age":18,"eligible":True}
print(info["name"])
print(info.get("eligible"))

# accessing multiple values
print(info.values())
print(info.keys())

for key in info.keys():
    print(info[key])
for key in info.keys(): #using f string
    print(f"the value corresponding to the key {key} is {info[key]}")

# accessing key value pairs
print(info.items())

for key,value in info.items():
    print(f"the value corresponding to the key {key} is {info[key]}")

# Dictionary methods in python
#update()
info.update({"age":20})
print(info)
info.update({"DOB":2001}) #addind an element
print(info)
dic.update(dic2) #adding a dictionary
print(dic)

#clear
'''ep1.cleaar()
print(ep1)'''

#pop()
dic2.pop(346)
print(dic2)

#popitem()
info.popitem()
print(info)

#del()
del info["age"]
print(info)
del info
print(info)