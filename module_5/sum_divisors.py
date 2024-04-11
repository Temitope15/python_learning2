num = int(input("Enter a number: "))
total = 0
for j in range(1, num + 1):
    if num % j == 0:
        total += j
print("The sum of the divisors of", num, "is", total)
