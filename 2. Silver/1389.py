import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = float('inf')

dp = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 0

for _ in range(m):
    u, v = map(int, input().split())
    dp[u][v] = 1
    dp[v][u] = 1

for m in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][m] + dp[m][j])

connect = []
connect.append(0)

for i in range(1, n + 1):
    sum = 0
    for j in range(1, n + 1):
        if dp[i][j] != INF:
            sum += dp[i][j]
    connect.append(sum)

min = INF
assa = 0

for i in range(1, n + 1):
    sum = 0
    for j in range(1, n + 1):
        if dp[i][j] != INF:
            sum += dp[i][j]

    if sum < min:
        min = sum
        assa = i

print(assa)