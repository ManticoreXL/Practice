highst = 0

# AAA, AAB, ABA, BAA, ABC
for _ in range(int(input())):
    d = list(map(int, input().split()))
    if d[0]==d[1]:
        if d[1]==d[2]: # AAA
            price = 10000 + d[0]*1000
            if price>highst:
                highst = price
        else: # AAB
            price = 1000 + d[0]*100
            if price>highst:
                highst = price
    elif d[0]==d[2]: # ABA
        price = 1000 + d[0]*100
        if price>highst:
            highst = price
    else:
        if d[1]==d[2]: # BAA
            price = 1000 + d[1]*100
            if price>highst:
                highst = price
        else: # ABC
            price = 100*max(d)
            if price>highst:
                highst = price
            
print(highst)