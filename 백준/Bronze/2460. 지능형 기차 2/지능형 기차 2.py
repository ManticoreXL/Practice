pit = 0
maxp = 0

for _ in range(10):
    m, p = map(int, input().split())
    pit = pit - m
    pit = pit + p
    if maxp == 0:
        maxp = pit
    elif maxp < pit:
        maxp = pit
        
print(maxp)