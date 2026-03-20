a, b, c = map(int, input().split())

if a == b:
    if b == c: # a=b=c 인 경우, 3개 상금
        reward = 10000 + 1000*a
    else: # a=b!=c 인 경우, 2개 상금
        reward = 1000 + 100*a
elif a == c: # a=c!=b 인 경우, 2개 상금
    reward = 1000 + 100*a
elif b == c: # b=c!=a 인 경우, 2개 상금
    reward = 1000 + 100*b
else: # 3개 모두 다른 경우, 가장 큰 눈 상금
    high = a
    if a<b: # 최댓값 찾기
        if b<c:
            high = c
        else:
            high = b
    elif a<c:
        high = c
    reward = 100*high
    
print(reward)
    
        
 