n = int(input())
name = input()

name = list(name)

# r, s, e, f, a, q, t, d, w, c, z, x, v, g
case = ['r', 's', 'e', 'f', 'a', 'q', 't', 'd', 'w', 'c', 'z', 'x', 'v', 'g']

if name[n-1] in case:
    print(1)
else:
    print(0)
