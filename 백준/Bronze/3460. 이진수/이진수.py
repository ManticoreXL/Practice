t = int(input())

for _ in range(t):
    n = int(input())
    n = str(bin(n))
    n = n[2:]
    n = list(n)
    n.reverse()
    for x in range(len(n)):
        if n[x] == "1":
            print(x, end=" ")