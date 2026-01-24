import sys
input = sys.stdin.readline

count = [0] * 257

rows, cols, blocks = map(int, input().split())

minh = float('inf')
maxh = 0

for _ in range(rows):
    area = list(map(int, input().split()))

    for a in area:
        count[a] += 1

        if a > maxh:
            maxh = a
        elif a < minh:
            minh = a

time = float('inf')
height = 0

for h in range(minh, maxh + 1):
    t = 0
    b = blocks

    for x in range(minh, maxh + 1):
        if x > h:
            t += ((x - h) * 2) * count[x]
            b += (x - h) * count[x]
        else:
            t += ((h - x) * 1) * count[x]
            b -= (h - x) * count[x]

    if b < 0:
        continue
    
    if t <= time:
        time = t
        height = h

print(time, height)