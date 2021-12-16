def divide(number):
    try:
        return 42/number
    except ZeroDivisionError: #this error you get when you divide a number by 0
        print (' you cannot divide number by 0')
print(divide(2))
print(divide(1))
print(divide(0))
print(divide(42))
