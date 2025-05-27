#Built-in methods used to alter or modify string in python
# NOTE= these string methods do not make changes in orignal string rather they create a new string
# 1. upper()->converts a string in upper case
str1="scjednGBGFGsadn"
print(str1.upper())

# 2.lower()->converts a string in lower case
str2="bdhcgDERHNbds"
print(str2.lower())

# 3.strip()->removes any whitw space before or after string
str3="deeksha soni  " 
print(str3.strip())

# 4.rstrip()
str4="hello!!!"
print(str4.rstrip("!"))

# 5.replace()
str5="silver spoon"
print(str5.replace("sp","M"))

# 6.split()
str6="silver spoon"
print(str6.split(" "))

# 7.capitalize()
str7="hello"
print(str7.capitalize())

# 8.center()
str8="Welcome to the console!!"
print(str8.center(50,".")) #center alingement plus padding

# 9.count()
str9="Abrakadabra"
print(str9.count("a"))

#10.endswith()
str10="welcome to the console!!"
print(str10.endswith("!!"))
print(str10.endswith("to",4,10))

#11.find()
str11="his name is den.he is an honest man"
print(str11.find("name"))

#12.index()
str12="HE's name is dan.he is an honest man"
print(str12.index("dan"))

#13.isalnum()
str13="WelcomeToTheConsole"
print(str13.isalnum())

#14.isalpha()
str14="Welcome"
print(str14.isalpha())

#15.islower()
str15="hello world"
print(str15.islower())

#16.isprintable()
str16="we wish you a merry christmas"
print(str16.isprintable())

#17.isspace()
str17="           "
print(str17.isspace())

#18.istitle()
str18="World Health Organization"
print(str18.istitle())

#19.isupper()
str19="WORLD HEALTH"
print(str19.isupper())

#20.startswith()
str20="python is an iterpreted language"
print(str20.startswith("python"))

#21.swapcase()
str21="World Health"
print(str21.swapcase())

#22.title()
str22="His name is dan"
print(str22.title())