st = list(input())
blk = st.count(" ")

if st[0] == " ": # 
    if st[-1] == " ":
        # 양 끝이 공백인 경우
        print(blk-1)
    else:
        # 공백으로 시작한 경우
        print(blk)

elif st[-1] == " ":
    # 끝에만 공백이 있을 경우
    print(blk)
    
else:
    # 모두 문자로 시작하고 끝난 경우
    print(blk+1)
        
    