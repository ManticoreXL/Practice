a, b = map(int, input().split())
s = []

for x in range(1, a+1):
    if a%x==0:
        s.append(x)
        
if b>len(s):
    print(0)
else:
    print(s[b-1])