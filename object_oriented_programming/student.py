#!/usr/bin/python3
'''
class Student:
    def __init__(self, name, level, score):
        self.name = name
        self.level = level
        self.score = score

    def introduce(self):
        print(f"I'm {self.name}, in {self.level} with score {self.score}")

    def update_score(self, new_score):
        self.score = new_score
        print(f"{self.name}'s score is now {self.score}")

    def promote(self):
        self.level = "University"
        if self.score > 90:
            print(f"{self.name} has been promoted to {self.level}")
        else:
            print(f"sorry {self.name} is not legible for promotion")

# Test it
student1 = Student("Ama", "SHS", 100)

student1.introduce()
student1.promote()
student1.introduce()

'''

class patients:
    def __init__(self,name, age, gender,ward,condition):
        self.name = name
        self.age = age
        self.gender = gender
        self.ward = ward
        self.condition = condition
    def info(self):
        user_input = input ("please enter patients name")

        if user_input == "daniel":
            print("hello")
        else:
            print("hi")
patient1 = patients("daniel",24,"male","wardK","malaria")

patient1.info()
