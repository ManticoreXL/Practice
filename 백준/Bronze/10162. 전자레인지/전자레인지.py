t = int(input())

a = t//300
t = t - a*300

b = t//60
t = t - b*60

c = t//10
t = t - c*10

if t==0: # 딱 떨어져서 조건 부합
    print(a, b, c)
else: # 조건 부적합
    print(-1)
