from random import randint
right = 0
wrong = 0
for i in range(10):
    randomNum1 = randint(1, 10)
    randomNum2 = randint(1, 10)
    multiply = randomNum1 * randomNum2
    question = int(input(f"Question {i+1}: {randomNum1} X {randomNum2} = "))
    if question == multiply:
        right += 1
        print("Right!")
    else:
        wrong += 1
        print(f"Wrong. The answer is {multiply}.")

print("END OF GAME")
print(f'You got {right} questions right and {wrong} question(s) wrong')
