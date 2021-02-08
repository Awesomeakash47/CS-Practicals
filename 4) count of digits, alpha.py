s = input('enter a string: ')

print('''
    1 - count of digits
    2 - count of alphabets
    3 - count of space
    4 - count of lower case alphabet
''')

ch = int(input('enter your choice: '))
count = 0

for i in range(len(s)):
    if ch == 1:
        if s[i].isdigit():
            count += 1

    elif ch == 2:
        if s[i].isalpha():
            count += 1

    elif ch == 3:
        if s[i].isspace():
            count += 1

    elif ch == 4:
        if s[i].islower():
            count += 1

print(count)




    