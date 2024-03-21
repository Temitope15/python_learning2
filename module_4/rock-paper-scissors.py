from random import randint
userName = input("What is your name: ")
ruleTitle = "THIS IS THE RULE OF THE GAME"
print(ruleTitle)
print("*" * len(ruleTitle))
print("if you are picking rock, type 1, picking paper type 2, scissors type 3")
compScore, userScore = 0, 0

for i in range(5):
    compValue = randint(1, 3)
    userValue = int(input("USER:  "))
    print("computer:", compValue)

    if userValue < 1 or userValue > 3:
        print("invalid!")
    elif compValue == userValue:
        pass
    elif (compValue == 1 and userValue == 2) or \
         (compValue == 2 and userValue == 3) or \
         (compValue == 3 and userValue == 1):
        userScore += 1
    else:
        compScore += 1

print("END OF GAME!")
print(userName, "has", userScore, "points and the computer has", compScore, "points")
if userScore > compScore:
    print(userName, "YOU WON!")
elif userScore < compScore:
    print(userName, "YOU LOST!")
elif userScore == compScore:
    print("There is a tie!")
