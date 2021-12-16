#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
print ('Enter your name :')
name = input ()
print ('Enter your age:')
age = input()
calculate = 2020 + 100 - int(age)
print ('Hello ' + name + ' will be 100 years on ' + str(calculate))
