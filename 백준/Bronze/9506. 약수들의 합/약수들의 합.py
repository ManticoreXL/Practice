while(True):
    a = int(input())
    if a==-1:
        break

    nsum = 0
    s = []

    for x in range(1, a):
        if a%x==0: # 나눠지면 약수다.
            s.append(x)
            nsum = nsum + x

    if nsum==a:
        print(a, "=", end=" ")
        for x in range(len(s)):
            print(s[x], end="")
            if x!=len(s)-1:
                print(" + ", end="")
            else:
                print("")
    else:
        print(a, "is NOT perfect.")