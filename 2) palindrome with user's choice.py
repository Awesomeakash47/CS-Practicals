ch = 'y'

while ch == 'y'.lower():
    n = int(input('enter a number: '))
    a = n
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n//10

    if a == int(rev):
        print('The number is palindrome')
    else:
        print('The numba is not palindrome')

    ch = input('enter y to continue, n to stop')