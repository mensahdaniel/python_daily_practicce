#!/usr/bin/python3
class person:
    def __init__(self,name,height = 15,birthday = 29):
        self.name = name
        self.height = height
        self.birthday = birthday

    def run(self):
        print("{} runs very fast" .format(self.name))
    
droid2 = person("daniel",15,"29")
droid2.height()

