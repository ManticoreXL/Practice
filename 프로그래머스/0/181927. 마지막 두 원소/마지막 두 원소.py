def solution(num_list):
    answer = []
    
    l = len(num_list)
    
    for i in range(l):
        curr = num_list[i]
        
        answer.append(curr)
        
        if i == l - 1:
            prev = num_list[i - 1]
            if prev < curr:
                answer.append(curr - prev)
            else:
                answer.append(curr * 2)

    return answer