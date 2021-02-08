ch = int(input('1 or 2: '))

if ch == 1:
    s = input('enter a str: ')
    s1 = input('enter str to be found in the above str')

    if s.find(s1) > -1:
        print('its present')
    else:
        print('bruh')
    
elif ch == 2:
    s = input('enter a str: ')
    out = ''
    for i in range(len(s)):
        '''if s[i].isspace:

            out += '@'
        else:
            out += s[i]'''

    print(out)