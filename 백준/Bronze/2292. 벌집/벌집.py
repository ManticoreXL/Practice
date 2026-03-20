n = int(input())

count = 1

while (True):
    if n == 1:
        break
    if count == 1:
        n = n - 1
        count = count + 1
    else:
        n = n - 6*(count-1)
        if n <= 0:
            break
        count = count + 1

print(count)
