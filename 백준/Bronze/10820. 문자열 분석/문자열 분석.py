while(True):
    try:
        s = input()
        lw = 0
        up = 0
        n = 0
        sp = 0
        for x in s:
            if ord(x) >= 97 and ord(x) <= 122:
                lw = lw + 1
            elif ord(x) >= 65 and ord(x) <= 90:
                up = up + 1
            elif ord(x) >= 48 and ord(x) <= 57:
                n = n + 1
            elif ord(x) == 32:
                sp = sp + 1
        print(lw, up, n, sp)
    except EOFError:
        break