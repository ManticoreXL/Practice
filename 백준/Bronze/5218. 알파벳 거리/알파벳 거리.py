t = int(input())
d = []

for _ in range(t):
    a, b = input().split()
    for x in range(len(a)):
        if ord(a[x])<ord(b[x]):
            dis = ord(b[x]) - ord(a[x])
            d.append(dis)
        elif ord(a[x])>ord(b[x]):
            dis = (ord(b[x]) + 26) - ord(a[x])
            d.append(dis)
        else:
            d.append("0")
    print("Distances: ", end="")
    for x in d:
        print(x, end=" ")
    print()
    d.clear()