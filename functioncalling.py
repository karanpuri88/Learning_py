# Calling function , define function first & call later 

def hello():
    print("Hello")
hello()
try :
    hello()
except NameError:
    print("Not defined")