for _ in range(int(input())):
    yonsei = 0
    korea = 0
    for _ in range(9):
        a, b = map(int, input().split())
        yonsei = yonsei + a
        korea = korea + b
    if yonsei>korea:
        print("Yonsei")
    elif yonsei<korea:
        print("Korea")
    else:
        print("Draw")