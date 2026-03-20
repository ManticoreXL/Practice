import sys
s = []
summ = 0

for x in range(5):
    a = int(sys.stdin.readline())
    summ = summ + a
    s.append(a)
    
s.sort()

print(summ//5)
print(s[2])