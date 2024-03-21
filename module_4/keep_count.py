countTen = 0
countZero = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num > 10:
        countTen += 1
    if num == 0:
        countZero += 1
print(countTen, "numbers are greater than 10 and", countZero, "numbers are equal to zero")