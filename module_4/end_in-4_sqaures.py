count = 0
for i in range(1,101):
    if (i ** 2) % 10 == 4:
        count += 1
print(count, "numbers from 1 to 100 end with 4")
