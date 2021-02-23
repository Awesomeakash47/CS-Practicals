a = int(input('enter a number'))
b = int(input('enter a number'))

aeven = aodd = beven = bodd = 0

for i in range(a):
    if i % 2:
        aodd += i
    else:
        aeven += i

for i in range(b) :
    if i % 2:
        bodd += i
    else:
        beven += i



print(aeven, aodd)
print(beven, bodd)
