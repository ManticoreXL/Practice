t = int(input())

for x in range(t):
    a, b = input().split()
    c = []
    for y in range(len(b)):
        print(b[y]*int(a), end="")
    print()