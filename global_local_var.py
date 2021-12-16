# Difference between Global & local Variables

# using global variable inside a function & using global keyword inside function

x = 5
def num():
    global y
    print(" x was define outside function , but value of x inside function is same because it global variable" , x)
    y = 10
num()
print ("value of x outside function", x )
print ("value of y cannot print outside without using global keyword, because it is local scope")
print ("Value of y can be print outside only when we use global keyword global keyword", y)