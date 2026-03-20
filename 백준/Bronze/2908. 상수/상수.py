a, b = map(int, input().split())

def rhnum(n):
    trd = n//100
    snd = (n-trd*100)//10
    fst = n%10
    result = fst*100 + snd*10 + trd
    return result

print(max(rhnum(a), rhnum(b)))