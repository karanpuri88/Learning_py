#Local Scope#
def spam():
    eggs = 123
spam()
eggs = 321
print (eggs)

# Global & Local Scope#

def spam():
    eggs = 123
    bacon ()
    print (eggs)
def bacon ():
    ham = 101
    eggs = 1
spam()  
eggs = 411
print (eggs)

#To Convert Local scope variable to Global variable using global statement#
def spam():
    global eggs
    eggs = 10000
spam()
print (eggs)
