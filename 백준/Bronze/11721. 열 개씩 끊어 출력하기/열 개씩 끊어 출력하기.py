a = input()

for x in range(len(a)):
    if (x+1)%10 == 0:
        print(a[x])
    else:
        print(a[x], end="")