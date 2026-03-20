h, m, s = map(int, input().split())
time = int(input())

ph = time//3600
pm = (time%3600)//60
ps = time%60

s = s + ps
if s>=60:
    s = s%60
    m = m + 1

m = m + pm
if m>=60:
    m = m%60
    h = h + 1
    
h = h + ph
if h>=24:
    h = h%24
    
print(h, m, s)