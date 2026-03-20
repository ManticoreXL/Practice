def rev(x):
    if x >=1000:
        return x//1000 + ((x%1000)//100)*10 + (((x%1000)%100)//10)*100 + (x%10)*1000
    elif x>=100:
        return x//100 + ((x%100)//10)*10 + (x%10)*100
    elif x>=10:
        return x//10 + (x%10)*10
    else:
        return x


a, b = map(int, input().split())

print(rev(rev(a)+rev(b)))