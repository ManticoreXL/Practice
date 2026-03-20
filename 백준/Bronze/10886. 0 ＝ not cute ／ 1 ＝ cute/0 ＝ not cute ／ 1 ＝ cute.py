n = int(input())
vu = 0
vd = 0

for _ in range(n):
    a = int(input())
    if a==1:
        vu = vu + 1
    else: # a==0
        vd = vd + 1
        
if vu>vd:
    print("Junhee is cute!")
elif vu<vd:
    print("Junhee is not cute!")
        