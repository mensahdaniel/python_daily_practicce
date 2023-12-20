#!/usr/bin/python3
if __name__ == "__main__":
    import random
numbers = []
for i in range(5):
    numbers.append(random.randrange(1, 9))
for i in numbers:
    print(i,end = "")
