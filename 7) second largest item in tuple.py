ch = 'y'

while ch == 'y':
    t = eval(input('Enter a tuple: '))
    print(sorted(t)[-2])
    ch = input("y'wanna continue, then press y: ").lower()