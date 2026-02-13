def hansu(n):
    if n<100:
        return True
    else:
        n = str(n)
        a = int(n[0]) - int(n[1])
        b = int(n[1]) - int(n[2])
        if a==b:
            return True
        else:
            return False

n = int(input())

count = 0

for x in range(n):
    if hansu(x+1)==True:
        count = count + 1

print(count)