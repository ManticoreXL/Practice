import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list_a = set()

for _ in range(n):
    list_a.add(input().strip())

list_b = set()

for _ in range(m):
    list_b.add(input().strip())

intsec = list_a.intersection(list_b)
intsec = sorted(intsec)

print(len(intsec))
for name in intsec:
    print(name)