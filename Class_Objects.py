class Person:  # person iis a class
    name = "harry"
    occupation = "SE"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()  # a is an object of class person
print(a.name)

a.name = "deeksha" 
a. occupation = "data analyst"
a.networth = 20
print(a.name,a.occupation)
print(a.info())
