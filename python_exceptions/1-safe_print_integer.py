#!/usr/bin/python3
'''
while True:
    try:
        y = int(input("please enter a number "))
        break
    except ValueError:
        print("oops that was not a number please eneter a number ")
        break
'''
'''
user_input = input("please enter a number ")

try:
    number = int(user_input)
    print("you entered" ,number)
except ValueError:
    print("invalid input \n")

'''
# handling exceptions with index error 

try:
    my_list = [1,2,3]
    print(my_list[3])
except IndexError:
    print("sorry an unknown error occured ")

except:
    print("sorry that index does not exist")

finally:
    print("good job")
