#Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,0] and write a program that prints out all the elements of the list that are less than 5.

spam = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 0, 4]
for i in range (len(spam)):
    if spam[i] < 5:
        print (spam [i])
