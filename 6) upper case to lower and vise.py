s = input('enter a string: ')
output = ''

for i in range(len(s)):
    if s[i].islower():
        output += s[i].upper()
    elif s[i].isupper():
        output += s[i].lower()
    else:
        output += s[i]

print(output)     
