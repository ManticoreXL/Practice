year = int(input())

if year%4 == 0 :
    if year%100 == 0:
        if year%400 ==0:
            print(1) #4, 100, 400의 배수인 연도 ex)2000년
        else :
            print(0) # 4, 100의 배수이면서 400의 배수가 아닌 연도 ex)1900년
    else : 
        print(1) # 4의 배수이면서 100의 배수가 아닌 연도 ex) 2012년
else:
    print(0) # 4의 배수가 아니면 윤년이 아님.