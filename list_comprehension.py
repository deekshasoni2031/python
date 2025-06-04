# accepts items with small letter "o" in the new list
names=["milo","sarah","bruno","anastasia","rose"]
nameswith_o=[item for item in names if "o" not in item] #in place of not in in can also be used
print(nameswith_o)
nameswith_i=[item for item in names if "i"  in item] 
print(nameswith_i)