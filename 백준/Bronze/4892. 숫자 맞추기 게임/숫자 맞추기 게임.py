count = 0

while(True):
    count = count + 1
    n = int(input())
    if n == 0:
        break
    a = 3 * n
    if a % 2 == 1: # 홀수
        b = (a + 1) / 2
        c = 3 * b
        d = int(c / 9)
        print(str(count) + ". odd " + str(d))
    else:
        b = a / 2
        c = 3 * b
        d = int(c / 9)
        print(str(count) + ". even " + str(d))