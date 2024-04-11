count_1, count_4, count_9 = 0,0,0
for i in range(1,101):
    if (i * i) % 10 == 1:
        count_1 += 1
    if (i * i) % 10 == 4:
        count_4 += 1
    if (i * i) % 10 == 9:
        count_9 += 1
print("There are", count_1,  "square of numbers between 1 and 100 that end with 1")
print("There are", count_4,  "square of numbers between 1 and 100 that end with 4")
print("There are", count_9,  "square of numbers between 1 amd 100 that end with 9")