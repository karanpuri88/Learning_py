#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print ('Enter a number to know all its divisor')
num = input()

for i in range (1,int(num)):
    x = int(num)%(i)
    if x == 0 :
        print ('divisors of ' + num + ' are : ' + str(i))
