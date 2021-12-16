#Plus all numbers between first & last input

print ('enter first value :')
first = input()
print ('enter last value :')
last = input()
total = 0
for i in range(int(first),int(int(last)+1)):
        total = total+i
print(total)

