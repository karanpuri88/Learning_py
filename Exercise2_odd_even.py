#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
print ('Enter a number to know whether it is odd or even')
number = input()
output = int(number)%2
if output == 0:
    print ('it is even')
else :
    print ('it is odd')
