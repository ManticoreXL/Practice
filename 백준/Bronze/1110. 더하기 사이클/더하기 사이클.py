sum = int(input()) # 26

a = sum//10 # 10의 자리, 2
b = sum%10  # 1의 자리, 6

ans = 0
cnt = 0

while (True):
    ans = a + b # 2+6 = 8
    ans = ans%10
    cnt = cnt + 1
    
    if ((10*b)+ans)==sum: # 68 !- 26
        break
    
    a = b
    b = ans
    
print(cnt)    