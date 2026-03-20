t, a = map(int, input().split())

if t >= 12 and t <= 16: # 점심
    if a == 0:
        print("320")
    else:
        print("280")
elif t > 16 or t < 12:
    print("280")