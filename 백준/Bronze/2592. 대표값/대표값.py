import statistics

s = []
nsum = 0

for _ in range(10):
    a = int(input())
    s.append(a)
    nsum = nsum + a
    
print(nsum//10)
print(statistics.mode(s))