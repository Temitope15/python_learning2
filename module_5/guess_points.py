from random import randint

points = 0
for i in range(5):
    randomNum = randint(1, 10)
    guess = int(input('Enter a number from 1 to 10: '))
    if guess == randomNum:
        points += 10
    else:
        points -= 1
if points <= 0:
    print('You lose!')
else:
    print(f'You have {points} points')
