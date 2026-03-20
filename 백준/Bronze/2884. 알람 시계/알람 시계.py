h, m = map(int, input().split())

if m >= 45:
    m = m - 45
else: # 입력 분이 45보다 작을 때 (시간이 줄어들 때)
    temp1 = m - 45
    temp2 = abs(temp1)
    m = 60 - temp2
    
    if h == 0:
        h = 23
    else:
        h = h - 1

        
print(h, m)
    