def solution(num):
    answer = 0
    
    # 500번 반복해도 1이 되지 않으면 -1 리턴
    while answer < 500:
        if num == 1:
            return answer
        
        # 짝수인 경우
        if num % 2 == 0:
            num = num / 2
            
        # 홀수인 경우
        else:
            num = num * 3 + 1
            
        answer += 1
        
    if answer == 500:
        answer = -1
        
    return answer