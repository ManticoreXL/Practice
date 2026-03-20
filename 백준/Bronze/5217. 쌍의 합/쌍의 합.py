t = int(input())

for _ in range(t):
    a = int(input())
    if a % 2 == 0:
        count = a//2 - 1
    else:
        count = a//2
    print("Pairs for {0}:".format(a), end=" ")
    for x in range(1, (a//2)+1):
        if x != (a-x):
            count = count - 1
            print("{0} {1}".format(x, (a-x)), end="")
            if count != 0:
                print("", end=", ")
    print()