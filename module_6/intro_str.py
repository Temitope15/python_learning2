string = input("Enter a string: ")
print(len(string))
for i in range(10):
    print(string)
print(f'The first letter of {string} is {string[0]}')
print(f'The first 3 letters of {string} is {string[:3]}')
print(f'The last 3 letters of {string} is {string[-3:]}')
print(f'{string} written backwards is {string[::-1]}')
if len(string) > 7:
    print(f" the 7th character of {string} is {string[6]}")
else:
    print('the string is not long enough to print the 7th character')
print(f"the string without the first and last characters is {string[1:len(string) - 1]}")
print(f'{string.upper()}')
print(f"{string.replace('o', 'e')}")
spacedStr = ''
for c in string:
    spacedStr = spacedStr + c + ' '
print(spacedStr)
