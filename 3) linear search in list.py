ch = 'y'

while ch == 'y':
    l = eval(input(('enter a list')))
    s = input('enter the str to be checked')

    for i in l:
        if i == s:
            print('string is present in list')
            break
    
    ch = input('enter y to continue, n to stop').lower()
