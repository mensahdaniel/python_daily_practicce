#!/usr/bin/python3
while True:
    try:
        numerals = int(input("please enter a number: "))
        break
    except ValueError:
        print("you did not enter a number")
print("thankyou for enterng a number")
