num = int(input('Enter a number: '))
fac = 1
if num == 0:
    print(f'The factorial of {num} is 1')
elif num < 0:
    print('Invalid')
else:
    for i in range(1, num+1):
        fac *= i
    print(f'The factorial of {num} is {fac}')