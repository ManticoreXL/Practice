n = int(input())

for x in range(1, n+1):
    print((("* "*x).center(2*n-1)).rstrip())