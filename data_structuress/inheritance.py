#!/usr/bin/python3
# this is a function that defines a parent class that a base class inherits.
class boss:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("i am the boss and am called {}".format(self.name))


deboss = boss("bolga")
deboss.display()


class smallboy(boss):
    def seer(self):
        print("{} is my boss ".format(self.name))


akoa = smallboy("bolga")
akoa.seer()
