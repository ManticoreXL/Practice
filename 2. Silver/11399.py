import sys
input = sys.stdin.readline

n = int(input())

p = list(map(int, input().split()))
p.sort()

c = [0] * 1001

total = 0

for i in range(1, n + 1):
    c[i] = c[i - 1] + p.pop(0)
    total += c[i]

print(total)