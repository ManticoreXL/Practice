n = int(input())

s = list(map(int, input().split()))

y = 0
m = 0

for x in s:
    y = y + ((x//30)+1)*10
    m = m + ((x//60)+1)*15
    
if y==m:
    print("Y", "M", y)
elif y>m:
    print("M", m)
else:
    print("Y", y)