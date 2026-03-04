def solution(a, b):
    answer = 0
    
    sum1 = int(str(a) + str(b))
    sum2 = a * b * 2
    
    answer = max(sum1, sum2)
    
    return answer