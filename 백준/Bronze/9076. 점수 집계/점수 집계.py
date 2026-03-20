t = int(input())

for _ in range(t):
    s = list(map(int, input().split()))
    s.sort()
    temp = s[-1] - s[1]
    if temp>=4:
        print("KIN")
    else:
        s = s[1:]
        s = s[:3]
        print(s[0]+s[1]+s[2])