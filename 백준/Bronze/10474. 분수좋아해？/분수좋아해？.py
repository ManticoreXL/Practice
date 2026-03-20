while(True):
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    q = a//b
    r = a%b
    print("{0} {1} / {2}".format(q, r, b))