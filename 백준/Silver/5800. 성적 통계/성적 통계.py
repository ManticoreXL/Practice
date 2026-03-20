t = int(input())

for x in range(1, t+1):
    s = list(map(int, input().split()))
    s = s[1:]
    s.sort()
    gap = 0
    for y in range(len(s)-1):
        if gap == 0:
            gap = s[y+1] - s[y]
        elif gap < s[y+1] - s[y]:
            gap = s[y+1] - s[y]
    print("Class", x)
    print("Max {0}, Min {1}, Largest gap {2}".format(max(s), min(s), gap))
    s.clear()