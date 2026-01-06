import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    str = input().strip()

    count = 0
    flag = True

    for i in range(len(str)):
        if str[i] == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            print("NO")
            flag = False
            break
    
    if flag == False:
        continue
    elif count == 0:
        print("YES")
    else:
        print("NO")
