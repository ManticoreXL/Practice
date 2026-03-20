n = int(input())

s = []

for x in range(n):
    a = int(input())
    s.append(a)
    
s.sort()

for x in range(n):
    print(s[x])