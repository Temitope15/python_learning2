"""
Program to print 1000 random numbers from 1 to 100
"""
from random import randint
count = 0
for i in range(10000):
    randomNum = randint(1,100)
    if randomNum % 12 == 0:
        count+=1
print("Between 1 and 1000 we have", count, "multiples of 12")