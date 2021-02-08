print('enter 1 - armstrong, 2 - factorial, 3 - sum of n numbers')
ch = int(input('enter your choice: '))

if ch == 1:
    n = input('enter a number')
    a = 0
    for i in range(len(str(n))):
        a += int(n[i]) ** 3

    if int(n) == a:
        print('its armstrong')
    else:
        print("bruh")

elif ch == 2:
    n = int(input('print factorial of: '))
    out = 1
    for i in range(1, n+1):
        out *= i
    print(out)

elif ch == 3:
    n = int(input('enter a number: '))
    out = 0
    for i in range(n+1):
        out += i
    print(out)

else:
    print('error 404: command not found')