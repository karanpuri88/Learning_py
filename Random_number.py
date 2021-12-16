#Secret number Game

import random
print ('Enter your name : ' )
name = input()
print ('Well, ' + name + ' I am thinking of a number between 1 and 20' )
secret = random.randint(1,20)

for i in range (1,7):
    print ('Take a guess')
    guess = int(input ())
    if guess > secret :
        print ('your guess is high')
    elif guess < secret :
        print ('your guess is low')
    else :
        break

if guess == secret:
    print ('Good job ' + name + ' you guessed my number in ' + str(i) + ' guesses')
else :
    print('Nope, The number I was thinking of was  '+ str(secret))
