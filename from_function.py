# import sqrt function from math module 
# import all function from random moudle

from math import sqrt
import random

x = input("Enter a number : ")
num = int(x)
# when function is imported from module , we do not need to preeced wih module name 
print ("Sqaure root of" , num, "is" , sqrt(num))

# when we load all function of module , when we need to use modulename.functionname

print ("Random value of " , num , "is",  random.randint(num,10))