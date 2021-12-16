#palindrom string

print ('enter a string to know wether it is palindrom or not')
name = input()
reverse = name[::-1] # Strings are list & ::-1 reverses the order
if name == reverse:
    print('It is palindrom')
else :
    print('it is not palindrom')
