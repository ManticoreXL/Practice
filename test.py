import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[False for _ in range(1, N + 1)] for _ in range(1, N + 1)]

for _ in range(M):
    u, v = map(int, input().split())