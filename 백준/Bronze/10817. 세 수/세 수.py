a = list(input().split())

for x in range(len(a)):
    a[x] = int(a[x])

a.sort()

print(a[1])