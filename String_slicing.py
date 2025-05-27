pie="apple pie"
print(pie[ :5]) #here the space is automaticallly assumed as 0
print(pie[6])
print(pie[:])  #here it will apply len function
print(pie[0:-3])
print(pie[0:len(pie)-3])
print(pie[-1:len(pie)-3])
print(pie[-3:-1])

#Finding length of string using len() function
name="deeksha soni"
print(len(name))