import calendar

m, d = map(int, input().split())

t = calendar.weekday(2007, m, d)

if t == 0:
    print("MON")
elif t == 1:
    print("TUE")
elif t == 2:
    print("WED")
elif t == 3:
    print("THU")
elif t == 4:
    print("FRI")
elif t == 5:
    print("SAT")
elif t == 6:
    print("SUN")