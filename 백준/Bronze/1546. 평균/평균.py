n = int(input())

score = list(map(int, input().split()))
nsum = 0

maxs = max(score)

for x in range(0, n):
    newscore = score[x]/int(maxs)*100
    nsum = nsum + newscore
    
print(nsum/n)