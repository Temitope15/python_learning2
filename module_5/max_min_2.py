highest_num = None
lowest_num = None
for i in range(10):
    score = int(input(f'enter score {i + 1}: '))
    if highest_num is None:
        highest_num = score
    if lowest_num is None:
        lowest_num = score
    if score > highest_num:
        highest_num= score
    if score < lowest_num:
        lowest_num = score
print(f"The highest score is: {highest_num}")
print(f"The lowest score is: {lowest_num}")