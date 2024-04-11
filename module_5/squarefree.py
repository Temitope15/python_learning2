import math

num = int(input("Enter any integer: "))
square_free = True
for i in range(1, num + 1):
    if num % i == 0:
        if int(math.sqrt(i)) ** 2 == i and i != 1:
            square_free = False
            break

if square_free:
    print(f"{num} is square free")
else:
    print(f"{num} is not square free")



