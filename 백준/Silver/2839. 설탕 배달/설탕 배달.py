n = int(input())

r = n%5

q = n//5 

if r == 0: # 5로 딱 떨어지는 경우
    print(q)
elif r == 1: # 나머지 1, 5kg 봉지 하나 빼고 3kg봉지 2개 추가
    if q >= 1:
        print(q+1)
    else:
        print(-1) # 1kg일 경우 불능.
elif r == 2: # 나머지 2, 5kg 봉지 2개 빼고 3kg봉지 4개 추가
    if q >= 2:
        print(q+2)
    else:
        print(-1) # 2kg, 7kg일 경우 불능.
elif r == 3: # 나머지 3, 3kg봉지 하나 추가. 불능 없음
    print(q+1)
elif r == 4: # 나머지 4, 5kg 봉지 1개 빼고 3kg 봉지 3개 추가
    if q >= 1:
        print(q+2)
    else:
        print(-1) # 4kg일 경우 불능.
