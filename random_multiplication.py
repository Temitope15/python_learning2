from random import randint
for i in range(10):
    randomNum1 = randint(1, 10)
    randomNum2 = randint(1, 10)
    multiply = randomNum1 * randomNum2
    print("Question ", (i+1),":", randomNum1, " X ", randomNum2, " = ", sep='', end='')
    question = int(input())
    if question == multiply:
        print("Right!")
    else:
        print("Wrong. The answer is ", multiply, ".")
print("END OF GAME")