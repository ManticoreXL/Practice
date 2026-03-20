t = int(input())
s = list(map(int, input().split()))
se = set(s)
s = list(se)
s.sort()

print(*s)