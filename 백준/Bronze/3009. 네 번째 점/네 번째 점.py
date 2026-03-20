a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

if a==c:
    if f==b:
        print(e, d)
    else:
        print(e, b)
elif c==e:
    if b==d:
        print(a, f)
    else:
        print(a, d)
else:
    if d==b:
        print(c, f)
    else:
        print(c, b)
        