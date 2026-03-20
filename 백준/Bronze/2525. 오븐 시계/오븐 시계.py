h, m = map(int, input().split())
ct = int(input())

ch = ct//60 # 더할 시간
cm = ct%60 # 더할 분

m = m + cm

if m >= 60:
    m = m - 60
    h = h + 1
    
h = h + ch

if h >= 24:
    h = h - 24
    
print(h, m)