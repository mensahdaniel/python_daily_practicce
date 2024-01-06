#!/usr/bin/python3
# this is a function that converts a word into an accronym
#ask the user to enter word
word = input("please enter a word to convert ")
#convert the words into an upper case 
word = word.upper()
#convert words to list
list_of_words = word.split()
#cycle throgh the list of words
for i in list_of_words:
#print the words without a line
    print(i[0],end="")
#add a new line
print()
