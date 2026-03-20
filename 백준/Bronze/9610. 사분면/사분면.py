qa = 0
qb = 0
qc = 0
qd = 0
ax = 0

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a>0:
        if b>0: # 제1사분면
            qa = qa + 1
        elif b<0: # 제4사분면
            qd = qd + 1
        else: # 축선
            ax = ax + 1
    elif a<0:
        if b>0: # 제2사분면
            qb = qb + 1
        elif b<0: # 제3사분면
            qc = qc + 1
        else: # 축선
            ax = ax + 1
    else: # 축선
        ax = ax + 1
        
print("Q1:", qa)
print("Q2:", qb)
print("Q3:", qc)
print("Q4:", qd)
print("AXIS:", ax)
