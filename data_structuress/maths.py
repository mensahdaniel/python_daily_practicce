#!/usr/bin/python3
original = input("enter the words: ")
#convert the string into an upper case
original = original.upper()
#now split those words
list_of_words = original.split()
#cycle through the list of words
for words  in list_of_words:
    print(words[0],end="")
print()
