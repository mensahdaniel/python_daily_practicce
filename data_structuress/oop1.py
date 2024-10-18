#!/usr/bin/python3
class cow:
    def __init__(self,name="",height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
    
    def cry(self):
        print("{} the cow cries".format(self.name))
    def eat(self):
        print("{} the cow eats very well aswer".format(self.name))
p = cow('bark')
j = cow('eat')
j.eat()
