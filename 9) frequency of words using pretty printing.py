import json

s = input('Enter a string: ')
d = {}
for i in s:
    d[i] = s.count(i)
    
print(json.dumps(d, indent=5))
