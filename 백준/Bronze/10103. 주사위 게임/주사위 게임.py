cy = 100
sd = 100

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a>b: # 창영 승, 상덕 점수 까기
        sd = sd - a
    elif a<b: # 상덕 승, 창영 점수 까기
        cy = cy - b
        
print(cy)
print(sd)