while(True):
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    if a%b==a:
        if b%a==0:
            print("factor")
        else: 
            print("neither")
    elif a%b==0:
        print("multiple")
    else:
        print("neither")