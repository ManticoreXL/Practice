sn = 0
mn = 0

for _ in range(7):
    a = int(input())
    if a%2==1: # 홀수인 경우
        sn = sn + a
        if mn==0:
            mn = a
        elif mn>a:
            mn = a

if sn==0:
    print(-1)
else:
    print(sn)
    print(mn)