n = int(input())

for _ in range(n):
    r, e, c = map(int, input().split())

    pro = e - c # 광고 효용성

    if r > pro: # 광고해도 수익이 평상시보다 적다 (광고X)
        print("do not advertise")
    elif r < pro: # 광고하면 수익이 더 생긴다 (광고O)
        print("advertise")
    else: # 광고하나마나 같음
        print("does not matter")