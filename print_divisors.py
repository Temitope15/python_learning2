multiple = int(input("Enter a number: "))
for i in range(1, multiple + 1):
    divisor = multiple % i
    if divisor != 0:
        continue
    print(i,", ", sep='', end='')
print("are factors of", multiple)