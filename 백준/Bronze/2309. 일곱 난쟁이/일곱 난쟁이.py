s = []

for _ in range(9):
    a = int(input())
    s.append(a)

for x in range(len(s)):
    for y in range(x+1, len(s)):
        if sum(s) - (s[x] + s[y]) == 100:
            s.pop(max(x, y))
            s.pop(min(x, y))
            break

s.sort()

for x in s:
    print(x)