import statistics

print("1) to find the mean of a list")
print('2) to replace the first item on a list with last')
print('3) max elemnt with its index ')


ch  = int(input('enter your choice 1, 2, 3: '))

if ch == 1:
    l = eval(input('enter a list:'))
    print(statistics.mean(l))

elif ch == 2:
    l = eval(input('enter a list:'))
    x = l.pop(0)
    l.append(x)
    print(l)

elif ch == 3:
    l = eval(input('enter a list:'))
    largest = max(l)
    index = l.index(largest)
    print(largest, index)