def test():
    eggs = 42
    test1()
    print(eggs)

#test()
#print(eggs) #this will give error as there is no assignment in global variable

def test1():
    eggs = 101
    print(eggs)

test()

def new():
    print(karan) # local variable can get value from global variable & but not vice versa
karan = 100
new()

def new1():
    global puri
    puri = 1000
    print(puri) 
puri = 500
new1()
print(puri) # as puri is defined as global , hence it will print 1000 NOT 500
