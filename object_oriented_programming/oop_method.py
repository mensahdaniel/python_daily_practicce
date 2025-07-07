#!/usr/bin/python3

# creating a method oop
'''
class person:
    def great(self):
        print("hellon good morning my friend ")

p = person

p().great()

'''

class student:
    def _init_(self,name,age,level):
        self.name = name
        self.age = age
        self.level = level


    def introduce(self):
        print(f"my name is {self.name}. I am {self.age} years old an im in level{self.level}")

# creating the student object

student1 = student( "daniel", 25, "level 400")
student2 = student("richard", 27, "senior high school")

#calling the method

student1.introduce()
