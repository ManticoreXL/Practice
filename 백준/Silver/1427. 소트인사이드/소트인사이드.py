s = input()
s = list(s)
s.sort()
s.reverse()

for x in range(len(s)):
    print(s[x], end="")