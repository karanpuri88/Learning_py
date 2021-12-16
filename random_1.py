import random
def test (number):
    if number == 1:
        return 'number 1'
    elif number == 2:
        return 'return 2'
    elif number == 3:
        return 'number 3'
number = random.randint(1,3)
r = test(number) # test function is being called & with passed parameter of number & return value stored in r variable #
print (r) #print Return value#
