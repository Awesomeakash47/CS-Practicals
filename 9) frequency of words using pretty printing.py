import json

s = input('Enter a string: ').split()
d = {}
for i in s:
    d[i] = s.count(i)
    
print(json.dumps(d, indent=5))