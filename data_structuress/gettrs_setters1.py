#!/bin/python3
class Daniel:
    def __init__(self,color,height):
        self.name = name
        self.height = height
        self.color = color
    @property
    def height(self):
        print("initialising the height")

        return self.__height
    
    @height.setter
    def height(self,value):

        if value.isdigit():
            self.__height = height
        else:print("please enter a value for height")

