t = int(input()) # 테스트 케이스 횟수

for x in range(t):
    n = int(input()) # 조사 학교 갯수
    cl = 0 # 술 소비량 비교값
    for x in range(n):
        s, l = input().split()
        l = int(l)
        if l > cl:
            cl = l
            bs = s
    print(bs)
        