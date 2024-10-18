#!/usr/bin/python3
class person:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def display(self):
        print("your user id is: {}".format(self.ID))
        return self.ID
emp = person("mensah",22341) #an object of a person
emp.display()
