#Write a Python program to check if a given number is prime or not.
num = int(input("Enter the number to be checked: "))
flag = 0 #presume num is a prime number
if num > 1 :
    for i in range(2, int(num / 2)):
        if (num % i == 0):
            flag = 1 #num is a not prime number
            break #no need to check any further
if flag == 1:
    print(num , "is not a prime number")
else:
    print(num , "is a prime number")