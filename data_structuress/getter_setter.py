#!/usr/bin/python3
class square:
    def __init__(self,height ="0",width ="0"):
        self.heigth = height
        self.width = width

    @property
    def height(self):
        print("initializing the height")

        return self.__height
    @height.setter
    def height(self,value):

        if value.isdigit():
            self.__height = value
        
        else:
            print("please please please")

    @property
    def width(self):
        print("initializing the height")

        return self.__width
    @height.setter
    def width(self,value):

        if value.isdigit():
            self.__width = value

        else:
            print("wmt wati")
    def get_area(self):
        return int(self.__height) * int(self.__width)
asquare = square()
height = input("please enter height :")
width  = input('please enter width :')

asquare.height = height
asquare.width = width

print("the heigth is",asquare.height)
print("the width is",asquare.width)

print("The area is",asquare.get_area())


