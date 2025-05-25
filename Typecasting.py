#explicit typecasting
#conversion is done by the developer
string1="14"
number= 4
string_number=int(string1)  #conversion of string1 from string data type to int. data type.
sum=number+ string_number
print("the sum is",sum)

#Implicit typecasting
#python automatically converts
#a to int
a=5
b=1.2
c=a+b
print(c)
print(type(a))
print(type(b))
print(type(c))