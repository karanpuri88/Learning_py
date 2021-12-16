#print list using for loop
#finding the index value in a list

spam = ['dog','cat','elephant','rat']

for i in range (len(spam)):
    print('index ' + str(i) + ' is ' + spam[i])
    name = spam[i]
    print (str(spam[i]) + ' is ' + str(spam.index(name)))

#Append a new vlaue in a list
print ('Enter a new value to add in a list')
x= input ()
spam.append(x)
print ('print the appended value : ' + spam [-1])

#Insert & take the index & value input from user

print('enter the index value between 0 & ' + str(len(spam)) + ' to insert a new value in list')
k = input()
l = int(k)
print('enter the name')
nameA = input ()
spam.insert(l,nameA)
print ('the new index value : ' + str(l) + ' & name is : ' + str(nameA))
print (spam)

#Revision
#=========

# Add all the numbers taken from user input using for loop & while loop
print ('enter the first value : ')
a = input()
print ('enter the first value : ')
b = input()
for f in range (int(a),int(b)):
    value = 0 + f
print (value)
