import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
max = 0

cards.sort()

for i in range(0, len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)): 
            sum = cards[i] + cards[j] + cards[k]
            if sum > max and sum <= m:
                max = sum

print(max)