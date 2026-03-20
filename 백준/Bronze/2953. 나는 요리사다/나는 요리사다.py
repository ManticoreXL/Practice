maxs = 0
winner = 0

for x in range(1, 6):
    a, b, c, d = map(int, input().split())
    score = a + b + c + d
    if maxs == 0:
        maxs = score
        winner = x
    elif maxs < score:
        maxs = score
        winner = x

print(winner, maxs)