n = int(input())

s = []
s.append(0)
s.append(1)

for x in range(2, n+1):
    s.append(s[x-1]+s[x-2])
        
print(s[n])