# string formatting in python
txt="for only {price:.2f} dollars!" # .2 means upto 2 decimal places
print(txt.format(price=49))

vote="all the memembers whose age is {age:.1f} are elegible for voting"
print(vote.format(age=18))