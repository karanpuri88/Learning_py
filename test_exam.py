# word_without_vowels = ""

# # Prompt the user to enter a word
# # and assign it to the user_word variable.

# user_word = input ("Enter the word :")
# user_word = user_word.upper()
# for letter in user_word:
#     # Complete the body of the loop.
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     word_without_vowels = word_without_vowels + letter

# # Print the word assigned to word_without_vowels.
# print (word_without_vowels)



# c0 = int(input("Enter ny non-negative and non-zero integer number : "))
# count = 0
# while c0 > 1:
#        if c0 % 2 == 0:
#            new_c0 = c0//2
#            print (new_c0)
#            c0 = new_c0
#            count = count + 1
#        else :
#            new_c0 = 3*c0+1
#            print (new_c0)
#            c0 = new_c0
#            count = count + 1
            
# print ("Steps = ", count)



# list_2 = [0, 1, 2, 3, 6, 10, 11, 15]

# sorted = list_2.sort()

# print (type (sorted))



# # What they taught in school ... # bubble sort
# #=================================

# list_1 = [0, 1, 2, 3, 6, 10, 11, 15]
# swapped = True
# while swapped:
#     swapped = False
#     for i in range(len(list_1)-1):
#         if list_1[i] > list_1[i+1]:
#             swapped = True
#             list_1[i], list_1[i+1] = list_1[i+1], list_1[i]
# print (list_1)

# # what they do in real life
# #==========================

# list_2 = [0, 1, 2, 3, 6, 10, 11, 15]
# list_2.sort()
# print (list_2)

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2

# del list_1[0]
# del list_2[:]

# print(list_3)



t = [[3-i for i in range (3)] for j in range (3)]

print(t[3][0])

# s = 0
# for i in range (3):
#      s= s+ t[i][i]
# print(s)