import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    closet = {}

    for _ in range(n):
        dress, type = input().split()
        closet.setdefault(type, []).append(dress)

    comb = []
    
    for type in closet.keys():
        comb.append(len(closet[type]) + 1)
    
    count = 1

    for c in comb:
        count *= c

    print(count - 1)