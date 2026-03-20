n, x = map(int, input().split())
s = list(input().split())
a = []

for i in range(0, n):
    if int(s[i]) < x:
        a.append(s[i])
        
print(" ".join(a))
        
