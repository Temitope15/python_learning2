t = ''

for i in range(5):
    l = input('Enter a letter: ')
    if l in 'aeiou':
        t = t + l
print(f'{t} is the vowel build up')
