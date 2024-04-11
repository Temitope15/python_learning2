count = 0
for i in range(1, 11):
    isSquare = int(i ** 0.5) ** 2 == i
    isCube = int(i ** (1 / 3)) ** 3 == i
    isFive = int(i ** (1 / 5)) ** 5 == i
    if not isSquare and not isCube and not isFive:
        count += 1
print(f" count = {count}")
