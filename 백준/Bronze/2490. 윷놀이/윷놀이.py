for _ in range(3):
    a, b, c, d = map(int, input().split())
    va = a + b + c + d
    if va == 0: # 윷
        print("D")
    elif va == 1: # 걸
        print("C")
    elif va == 2: # 개
        print("B")
    elif va == 3: # 도
        print("A")
    elif va == 4: # 모
        print("E")