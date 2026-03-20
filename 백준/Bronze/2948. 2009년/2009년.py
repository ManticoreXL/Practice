import calendar

d, m = map(int, input().split())

t = calendar.weekday(2009, m, d)

if t == 0:
    print("Monday")
elif t == 1:
    print("Tuesday")
elif t == 2:
    print("Wednesday")
elif t == 3:
    print("Thursday")
elif t == 4:
    print("Friday")
elif t == 5:
    print("Saturday")
elif t == 6:
    print("Sunday")