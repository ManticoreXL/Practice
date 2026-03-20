s = input()
answer = ""

for x in s:
    if "a"<=x and x<="z": # 소문자일 때
        x = ord(x) + 13
        if x>122:
            x = x - 26
        answer = answer + chr(x)
    elif "A"<=x and x<="Z":
        x = ord(x) + 13
        if x>90:
            x = x - 26
        answer = answer + chr(x)
    else:
        answer = answer + x

print(answer)