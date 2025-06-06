# f-strings in python
letter="hey my name is {1} and i am from {0} and my city is {2}"
country="india"
name="deeksha"
city="jabalpur"
print(letter.format(country,name,city)) # country={0}  and name={1}

#using f string
print(f"he my name is {name} and i am from {country}")

price=49.09999
txt=f"for only {price:.2f} dollars!"
print(txt)

print(f"{2*30}")
print(type(f"{2*30}"))

# we can use {{}} to display the string as it is and not it's populated values
print(f"my name is {{name}} and i am from {{country}}")