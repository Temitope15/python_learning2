from math import log
num = int(input("Enter a whole number: "))
total = 1
for i in range(2,num+1):
    total = total + (1/i)
print(total - log(num))
