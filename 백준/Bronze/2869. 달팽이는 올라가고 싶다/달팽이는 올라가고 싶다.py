a, b, v = map(int, input().split())

velo = a - b # 하루 올라가는 양

rv = v - a # 실제 올라가야하는 높이

temp = rv%velo

if temp == 0:
    print(rv//velo+1)
else:
    print(rv//velo+2)