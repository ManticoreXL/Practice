n = int(input())

s = list(input().split())

res = 0
temp = 1

for x in range(n):
    if s[x]=="1":
        res = res + temp
        temp = temp + 1
    else:
        temp = 1
    
print(res)