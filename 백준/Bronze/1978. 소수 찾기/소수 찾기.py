def judgeprime(a):
    if a == 1:
        return False
    for x in range(2, a):
        if a%x == 0:
            return False
    return True
        
cnt = 0        
n = int(input())
s = list(map(int, input().split()))

for x in range(n):
    if judgeprime(s[x]) == True: # 소수일 경우
        cnt = cnt + 1
        
print(cnt)
  