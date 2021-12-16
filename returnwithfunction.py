import random

def getanswer(answernumber):
    if answernumber == 1:
        return 'hello 1'
    
    elif answernumber == 2:
        return 'hello 2'
    
    elif answernumber == 3:
          return 'hello 3'
   
    elif answernumber == 4:
         return 'hello 4'
    
    elif answernumber == 5:
         return 'hello 5'
    

x=random.randint(1,5)

y=getanswer(x)

print(y)

