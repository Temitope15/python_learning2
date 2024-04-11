"""
Program that finds all the perfect numbers less than 10000
A perfect number - A number is called a perfect number if it is equal to the sum of all of its divisors, not including
the number itself
For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6
and 6 = 1 + 2 + 3.
"""
for i in range(2,10000):
    total = 0
    for j in range(1,i):
        if i % j == 0:
            total += j
    if total == i:
        print(total)