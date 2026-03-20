x = int(input())
y = int(input())

if x>0:
    if y>0: # 1사분면
        print(1)
    else: # 4사분면
        print(4)
else: # x<0
    if y>0: # 2사분면
        print(2)
    else: # 3사분면
        print(3)