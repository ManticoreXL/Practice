import sys
input = sys.stdin.readline

num = int(input())

cons = []
flag = False

for i in range(1, num + 1):
    n = num - i
    str_num = str(n)

    digits = [int(digit) for digit in str_num]

    sum = n
    for d in digits:
        sum += d

    if sum == num:
        cons.append(n)
        flag = True
    
if flag:
    print(min(cons))
else:
    print(0)