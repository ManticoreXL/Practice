t = int(input())

s = [list(input().split()) for _ in range(t)]

s.sort(key = lambda x: (x[1], x[0]))

print(s[0][0])