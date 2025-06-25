#!/usr/bin/python3
def divide(x,y):
    try:
        answer = x / y
    except ZeroDivisionError:
        print ("can't do that ")
    else:
        print("the result is".format(answer))
