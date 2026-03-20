per = 0
mp = 0

for x in range(3):
    m, p = map(int, input().split())
    per = per - m
    per = per + p
    if mp==0:
        mp = per
    elif mp<per:
        mp = per
    
print(mp)
    