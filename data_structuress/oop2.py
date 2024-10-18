#!/usr/bin/python3
class square:
    def __init__(hight='0',width='0'):
        self.height = height
        self.width = width

        @property
        def height(self):
            print('retrieving the height')

            return self.__height
        @height.setter
        def height(self,value):
            if value.isdigit():
                self.__height = value
            else:
                ("please enter a number what you entered isnt a number")

        @property
        def width (self):
            print('retrieving the height')

            return self.__width
        @height.setter
        def height(self,value):
            if value.isdigit():
                self.__width = value
            else:
                ("please enter a number what you entered isnt a number")
        def getarea(self):
            return int(self.__width) * int(self.__height)

def main():
    asquare = square()
    height = input('please enter a height ')
    width = input ('please enter width')
    asquare.height = height
    asquare.width = width
    print('height', asquare.width)
    print('height',asquare.height)
    print("area is ",asquare.getarea)
main()
